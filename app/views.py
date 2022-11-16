from django.shortcuts import render
from django.core.paginator import Paginator

poptags = [
    'django',
    'python',
    'javascript',
    'html',
]

bestmembers = [
    {
        'username': 'John Doe',
        'id': 1,
    },
    {
        'username': 'krainikov',
        'id': 2,
    },
    {
        'username': 'admin',
        'id': 3,
    },
]

questions = [
        {
            'id': i,
            'title': 'How to sleep more than '+ str(i) +' hours?',
            'likes': 10,
            'answers': 5,
            'tags': ['sleep', 'rest', 'health'],
            'text': "I'm a student and I have a lot of homework. I need to sleep more than 2 hours. How can I do it? I'm a student and I have a lot of homework. I need to sleep more than 2 hours. How can I do it? I'm a student and I have a lot of homework. I need to sleep more than 2 hours. How can I do it? I'm a student and I have a lot of homework. I need to sleep more than 2 hours. How can I do it? I'm a student and I have a lot of homework. I need to sleep more than 2 hours. How can I do it?",
            'author': {
                'name': 'John Doe',
                'avatar': 'https://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50',
            },
            'answers': [
                {
                    'text': 'You need to sleep more than 2 hours',
                    'author': {
                        'name': 'John Doe',
                        'avatar': 'https://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50',
                    },
                    'likes': 10,
                },
                {
                    'text': 'You need to sleep more than 2 hours',
                    'author': {
                        'name': 'John Doe',
                        'avatar': 'https://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50',
                    },
                    'likes': 10,
                },
            ],
        } for i in range(1, 100)
    ]

def index(request, title="AskKrainikov"):
    paginator = Paginator(questions, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'title': title, 'poptags': poptags, 'bestmembers': bestmembers, 'questions': page_obj})
    

def hot(request):
    return index(request, title="Hot questions")

def tag(request, tag):
    return render(request, 'taglisting.html', {'tag': tag, 'poptags': poptags, 'bestmembers': bestmembers, 'questions': questions})

def question(request, question_id):
    return render(request, 'questionpage.html', {'question': questions[int(question_id)], 'poptags': poptags, 'bestmembers': bestmembers})

def login(request):
    return render(request, 'login.html', {'poptags': poptags, 'bestmembers': bestmembers})

def signup(request):
    return render(request, 'registration.html', {'poptags': poptags, 'bestmembers': bestmembers})

def ask(request):
    return render(request, 'question.html', {'poptags': poptags, 'bestmembers': bestmembers})