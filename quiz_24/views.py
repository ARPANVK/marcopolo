from django.shortcuts import render
from slide_quiz.models import UniqCode

def Login(request):
    # print('hello')

    return render(request, 'home.html')

def StExam(request):
    return render(request,'start_exam.html')

def SysEli(request):
    lic = ''
    ucode = UniqCode.objects.all()
    if request.method == 'POST':
        code_input = request.POST.get('code_input')
        for obj in ucode:
            if obj.code == code_input:
            # Perform any action with the matched code here
            # For example, you can delete the matched object
                obj.delete()
                print(ucode)
                lic = 'pass'
            else:
                lic = 'fail'
    return render(request,'system_eligibility.html',{'lic':lic})