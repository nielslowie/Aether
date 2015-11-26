import datetime

import isoweek
from django.core.mail import send_mail
from django.http import HttpResponse, BadHeaderError
from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import Subject


def generate_schedule(subject, start_date, end_date, start_time, end_time, date_delta, time_delta):
    start_date_time = datetime.datetime.combine(start_date, start_time)
    end_date_time = datetime.datetime.combine(end_date, end_time)

    schedule = {"days": [], "hours": []}

    while start_date_time <= end_date_time:
        day_schedule = {"name": start_date_time.strftime("%A"), "classes": []}

        while start_date_time.time() <= end_date_time.time():
            course_query = subject.courses.filter(class__start_date_time=start_date_time)

            if course_query:
                lecture = course_query.first().class_set.get(start_date_time=start_date_time)

                start_date_time += lecture.end_date_time - lecture.start_date_time
            else:
                lecture = None

                start_date_time += time_delta

            day_schedule["classes"].append(lecture)

        start_date_time = datetime.datetime.combine((start_date_time + date_delta).date(), start_time)

        schedule["days"].append(day_schedule)

    while start_date_time.time() <= end_date_time.time():
        schedule["hours"].append(start_date_time.strftime('%H:%M'))

        start_date_time += time_delta

    return schedule


def index(request):
    # Test value
    subject = Subject.objects.all()[0]

    week = isoweek.Week.thisweek()

    try:
        week_index = int(request.GET["week"])
    except:
        week_index = 0

    week += week_index

    start_date = week.monday()
    end_date = week.sunday()

    start_time = datetime.time(8)
    end_time = datetime.time(20)

    date_delta = datetime.timedelta(days=1)
    time_delta = datetime.timedelta(minutes=30)

    schedule = generate_schedule(subject, start_date, end_date, start_time, end_time, date_delta, time_delta)

    context = {'schedule': schedule, 'week': week_index}

    return render(request, 'schedule/index.html', context)


def about(request):
    return render(request, "schedule/about.html")


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']

            try:
                send_mail(subject, message, sender, ['project.aeolus.aether@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')

    return render(request, "schedule/contact.html", {'form': form})
