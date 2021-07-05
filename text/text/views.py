from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    data = {'name':'rushi','location': 'mumbai','age':21}
    return render(request,'index.html',data)

def analyzed(request):
    text = request.POST.get('text','default')
    fullcaps = request.POST.get('fullcaps','off')
    remove_punc = request.POST.get('remove_punc','off')
    new_line = request.POST.get('new_line_remove','off')
    space_remover = request.POST.get('space_remove','off')
    char_count = request.POST.get('char_count','off')
    for_tab = request.POST.get('for_tab','off')

    if fullcaps == "on":
        analyzed_text = ""
        for char in text:
            analyzed_text  = analyzed_text+char .upper()
        params = {'purpose':'upper case',"analyzed_text":analyzed_text}
        return render(request,"result.html",params)

    if char_count == "on" :
        count = 0
        for i in text:
            if i == " ":
                pass
            else:
                count = count + 1
        params = {'purpose':'char_count is:', 'analyzed_text': count}
        return render(request,'result.html',params)

    if space_remover == "on" :
        analyzed_text = ""
        for i in text:
            if i == " ":
                pass
            else:
                analyzed_text += i
        params = {'purpose':'space_remover','analyzed_text':analyzed_text}
        return render(request,'result.html',params)

    if remove_punc == "on":
        analyzed_text = ""
        punc = '''!@#$%^&*()_[]{}|<>?~'''
        for i in text:
            if i not in punc:
                analyzed_text = analyzed_text + i
        params = {'purpose': 'remove_punc', 'analyzed_text':analyzed_text}
        return render(request,'result.html',params)

    if new_line == "on":
        analyzed_text = ""
        for i in text:
            if i != "\n"or"\r":
                analyzed_text = analyzed_text + i
        params = {'purpose':'new_line_remove','analyzed_text':analyzed_text}
        return render(request,'result.html',params)