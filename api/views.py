from django import forms
from django.shortcuts import render
from .models import FormData
from .forms import EduboardForm
# Create your views here.
from pylatexenc.latex2text import LatexNodes2Text


def convert_latex(latex):
    data = LatexNodes2Text().latex_to_text(latex)
    return data


def create_question(request):
    if request.method == 'POST':
        form = EduboardForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.Question = convert_latex(instance.Question)
            instance.Clue = convert_latex(instance.Clue)
            instance.Solution = convert_latex(instance.Solution)
            instance.Answer = convert_latex(instance.Answer)
            instance.CorrectAnswer = convert_latex(instance.CorrectAnswer)
            instance.save()
            # form.save()
        # Question = convert_latex(request.POST.get('question'))
        # Clue = convert_latex(request.POST.get('clue'))
        # Solution = convert_latex(request.POST.get('solution'))
        # Answer = convert_latex(request.POST.get('answer'))
        # CorrectAnswer = convert_latex(
        #     request.POST.get('correctanswer'))
        # ImageData = request.POST.get('imagedata')

        # formdata = FormData(Question=Question,
        #                     Clue=Clue,
        #                     Solution=Solution,
        #                     Answer=Answer,
        #                     CorrectAnswer=CorrectAnswer,
        #                     ImageData=ImageData,)

        # formdata.save()
        form = EduboardForm()
        data = FormData.objects.all()
        context = {
            'title': 'Soarlogic',
            'form': form,
            'data': data,
        }

        print(context)
    else:
        form = EduboardForm()
        context = {
            'title': 'Soarlogic',
            'form': form,

        }

        
    return render(request, 'api/new.html', context)


def show_question(request):
    data = FormData.objects.get(pk=6)
    print(data)

    return render(request, 'api/data.html', {'title': 'Soarlogic', 'data': data})
