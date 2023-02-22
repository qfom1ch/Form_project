from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback
from django.shortcuts import get_object_or_404
# Create your views here.
from django.views import View
from django.views.generic.base import TemplateView

class FeedBackView(View):

    def get(self, request):
        form = FeedbackForm()
        return render(request, 'feedback/feedback.html',context={'form': form})

    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect('/done')
        return render(request, 'feedback/feedback.html', context={'form': form})


class UpdateFeedBack(View):

    def get(self,request, id_feedback):
        feed = get_object_or_404(Feedback,id=id_feedback)
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html',context={'form': form})

    def post(self, request,id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect(f'/{id_feedback}')
        return render(request, 'feedback/feedback.html', context={'form': form})


class DoneView(TemplateView):
    template_name = 'feedback/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name']='Ivanov I.I.'
        context['date']='23.04.2022'
        return context

def index(request):

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect('/done')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback.html',context={'form': form})


def done(request):
    return render(request, 'feedback/done.html')



def update_feedback(request, id_feedback):
    feed = Feedback.objects.get(id=id_feedback)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect(f'/{id_feedback}')
    else:
        form = FeedbackForm(instance=feed)
    return render(request, 'feedback/feedback.html',context={'form': form})

class ListFeedBack(TemplateView):
    template_name = 'feedback/list_feedback.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list'] = Feedback.objects.all()
        return context

class DetailFeedBack(TemplateView):
    template_name = 'feedback/detail_feedback.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['det'] = get_object_or_404(Feedback,id=kwargs['id_feedback'])
        return context