from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Question


def index(request):
    context = {
        'title': 'Home',
        'questions': Question.objects.order_by('-pub_date')[:5]
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    context = {
        'title': 'Polls',
        'question': get_object_or_404(Question, pk=question_id)
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    context = {
        'title': 'Results',
        'question': get_object_or_404(Question, pk=question_id)
    }
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except:
        context = {
            'title': 'Polls',
            'question': question,
            'error_message': 'Please select a choice'
        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(
            reverse('polls:results', args=(question.id,)))
