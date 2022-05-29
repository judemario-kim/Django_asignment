from multiprocessing import context
from re import template
from tokenize import String
from webbrowser import get
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice, Exam

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'qa/index.html'
    context_object_name = 'latest_exam_list'
    
    def get_queryset(self):
        return Exam.objects.order_by()[:5]

class DetailView(generic.DetailView):
    model = Exam
    template_name = 'qa/detail.html'

class ResultsView(generic.DetailView):
    model = Exam
    template_name = 'qa/results.html'

class StatisticView(generic.DetailView):
    model = Exam
    template_name = 'qa/statistic.html'

class Exam_mainView(generic.DetailView):
    model = Exam
    template_name = 'qa/exam_main.html'
    
def make_exam(request):
    return render(request, 'qa/make_exam.html')

def make_question(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    return render(request, 'qa/make_question.html', {'exam': exam, })

def create_exam(request):
    exam = Exam.objects.create(exam_name=request.POST['exam_name'])
    exam.save()
    return render(request, 'qa/make_question.html', {'exam': exam, })

def create_question(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    question = Question.objects.create(question_text=request.POST['question_text'], content = request.POST['question_content'], exam = Exam.objects.get(pk=exam_id))
    choice1 = question.choice_set.create(choice_text=request.POST['choice_text_1'])
    choice2 = question.choice_set.create(choice_text=request.POST['choice_text_2'])
    choice3 = question.choice_set.create(choice_text=request.POST['choice_text_3'])
    choice4 = question.choice_set.create(choice_text=request.POST['choice_text_4'])
    if request.POST["answer"]=="c1":
        choice1.answer=1
    elif request.POST["answer"]=="c2":
        choice2.answer=1
    elif request.POST["answer"]=="c3":
        choice3.answer=1
    elif request.POST["answer"]=="c4":
        choice4.answer=1
    choice1.save()
    choice2.save()
    choice3.save()
    choice4.save()
    question.save()
    if request.POST["new_question"]=="true":
        return render(request, 'qa/make_question.html', {'exam': exam, })
    else:
        return HttpResponseRedirect(reverse('qa:index'))
    
    
def score(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    correctnum = 0
    exam.num_of_question = 0
    for selected_question in exam.question_set.all():
        num_of_votes = 0
        exam.num_of_question += 1
        exam.save()
        try:
            selected_choice = selected_question.choice_set.get(pk=request.POST[selected_question.question_text])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'qa/detail.html',{
                'exam': exam,
                'error_message': "You didn't select a choice.",
            })
        else:
            if selected_choice.answer == 1:
                selected_question.correct = 1
                correctnum += 1
            else:
                selected_question.correct = 0
            selected_choice.votes += 1
            selected_question.save()
            selected_choice.save()
        for choice in selected_question.choice_set.all():
            num_of_votes += choice.votes
            if choice.answer == 1:
                answer_votes = choice.votes
        selected_question.correct_rate = (100/num_of_votes)*answer_votes
        exam.score = (100/exam.num_of_question)*correctnum
        selected_question.save()
        exam.save()
    return HttpResponseRedirect(reverse('qa:results', args = (exam.id,)))
