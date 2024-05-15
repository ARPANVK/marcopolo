from django.shortcuts import render,redirect
from django.contrib import messages

from .models import QuizQuistions

from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required


@login_required

# <<Create your views here.>>
# actual_answer = []
def Home(request):
    # <<Fetch all data from database>>
    questions = QuizQuistions.objects.all()
    # for i in questions:
    #     actual_answer.append(i.correct_answer)

    # print(actual_answer)

    # <<fetch data from template>>
    if request.method == 'POST':
        my_input_value = request.POST.get('UserInput')
        # print('Received input value:', my_input_value)
        # <<Process the my_input_value as needed. I store the data in the sessional storage to send it another class or functions.>>
        request.session['my_input'] = my_input_value
    numbers = range(1,16)

    # Check if user is authenticated
    if request.user.is_authenticated:
        # Fetch the username
        username = request.user.username
    return render(request, 'exampage.html', {'numbers': numbers,'questions':questions,'username':username})

def Check_Ans(request):
    # <<Fetch all data from database and store in a array>>
    questions = QuizQuistions.objects.all()
    actual_answer = []
    for i in questions:
        actual_answer.append(i.correct_answer)
    # print(actual_answer)

    # <<Fetch all data from template and store in a array>>
    my_input_value = request.session.get('my_input', None)
    user_ans = str(my_input_value).split(',')
    # print(user_ans)

    # <<Now compair user answer with correct answer and calculate score>>
    count = 0
    for i in range(len(user_ans)):
        if (user_ans[i]==actual_answer[i]):
            count = count+1
    message_for_email = f'<b>This is a System generated mail</b>\n\n\n\nHi buddy!\nYou have successfully submit your exam. Your score is {count}.\nDo continious practrice for more better improvement.\nThanks and Regrads,\nArpan Samanta\nFounder,Exam_24'
    if request.method == 'POST':
        send_mail(
            'Exam Feedback',
            message_for_email,
            settings.EMAIL_HOST_USER,
            ['arpanofcsamanta@gmail.com','victrysamanta74797@gmail.com'],
            fail_silently=False,
        )
    return render(request, 'end_session.html',{'score':count})

def send_email(request):
    if request.method == 'POST':
        send_mail(
            'Subject DEMO',
            'Message demo',
            settings.EMAIL_HOST_USER,
            ['arpanofcsamanta@gmail.com'],
            fail_silently=False,
        )
    return render(request, 'end_session.html')


def Login_Exam(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            return redirect('stexam')
        else:
            messages.error(request,'Username or Password is incorrect')
    return render(request,'login.html')

