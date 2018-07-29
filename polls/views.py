from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Questions
from django.template import loader
from django.shortcuts import render

def index(request):
    latest_questions = Questions.objects.order_by('time')[:5];
    output = ','.join([q.question for q in latest_questions]);
    template = loader.get_template('polls/index.html')
    context={
        'latest_question_list':latest_questions
    }
    return HttpResponse(template.render(context,request));

def detail(request,question_id):
    try:
        question = Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
        raise Http404("Question does not exist.")
    context = {
        'question':question
    }
    return render(request,'polls/details.html',context);

def results(request,question_id):
    return HttpResponse("You are looking at results of question %s" % question_id);

def vote(request,question_id):
    return HttpResponse("You are voting on question %s" %question_id);


