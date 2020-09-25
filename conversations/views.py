from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import CreateConversation, CreateMessage, CreateThought

def home(request):
    """
    Home view with all conversations' titles + their creation dates
    """
    conversations = Conversation.objects.all().order_by('-start_date')
    context = {'conversations':conversations}
    return render(request, 'conversations/home.html', context)


def addConversation(request):
    """
    View to create a new conversation
    """
    form = CreateConversation()
    if request.method == 'POST':
        form = CreateConversation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'conversations/addconversation.html', context)


def convoDetail(request, id):
    """
    View to read messages + thoughts (content) in a conversation
    """
    convo = Conversation.objects.get(id=id)
    title = convo.title
    start_date = convo.start_date
    messages = Message.objects.filter(conversation=convo).order_by('-date_and_time_sent')
    form = CreateMessage()
    context = {'messages':messages, 'convo': convo, 'form': form}
    return render(request, 'conversations/convodetail.html', context)


def addMessage(request, id):
    """
    Route to create a new message in a conversation
    """
    conversation = get_object_or_404(Conversation, id=id)
    new_message = None

    if request.method == 'POST':
        form = CreateMessage(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.conversation = conversation
            new_message.save()
            return redirect(f'/convodetail/{id}')

    context = {'form': form}
    return render(request, 'conversations/convodetail.html', context)


# def addThought(request):
#     """
#     Route to create a new thought in a message
#     """
#     return render(request, 'conversations/addthought.html')


def search(request):
    """
    Route to enable search bar / searching convos by titles / keywords
    """
    if request.method == 'GET':
        search = request.GET.get('search')
        result = Conversation.objects.all().filter(title__icontains=search)
        if result:
            context = {'result': result}
            return render(request, 'conversations/results.html', context)
        else:
            return HttpResponse("<h3>Result not found... 🕺</h3>")