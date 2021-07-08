from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from . models import createQ, staff_reg, stu_rec,stud_reg,stud_res
import easygui
from django.contrib.auth import logout as log

# Create your views here.
crt_ans=0
wrong_ans=0
count=0
staff_username=''
stud_username=''
answer=''

def index(request):
    return render(request,'index.html')

def createquestion(request):
    staff_user=staff_reg.objects.get(username=staff_username)
    return render(request,'createquestion.html',{'staff_user':staff_user})

def createquestion_DB(request):
    if request.method == 'POST':
        var1=createQ(question=request.POST['question'],
                      option1=request.POST['option1'],
                      option2=request.POST['option2'],
                      option3=request.POST['option3'],
                      option4=request.POST['option4'],
                      correctans=request.POST['correctans'])
        var1.save()
        easygui.msgbox("Question Created...")
        return redirect(createquestion)
    
def get_data(request):
    global crt_ans
    global count
    global wrong_ans
    global answer
    if request.method=='POST':
        var4=stud_res(question=request.POST['question'],
                      youranswer=request.POST['answer'],
                      correctans=request.POST['crt_answer'])
        var4.save()
        answer=request.POST['answer']
        crt_answer=request.POST['crt_answer']
        if answer == crt_answer:
            crt_ans=crt_ans+1
            count=count+1
        else:
            wrong_ans=wrong_ans+1
            count=count+1
    return render(request,'answerquestion.html')

def stud_record(request):
    if request.method == 'POST':
        var4=stu_rec(question=request.POST['question'],
                     option1=request.POST['option1'],
                     option2=request.POST['option2'],
                     option3=request.POST['option3'],
                     option4=request.POST['option4'],
                     correctans=request.POST['crt_answer'])
        var4.save()
        easygui.msgbox("Question Saved Successfully!...")
    return render(request,'answerquestion.html')
    
def taketest(request):
    stud_name=stud_reg.objects.get(firstname=stud_username)
    delete_res=stud_res.objects.all()
    delete_res.delete()
    return render(request,'taketest.html',{'stud_name':stud_name})

def staff_dash(request):
    staff_user=staff_reg.objects.get(username=staff_username)
    stud_count=staff_reg.objects.count()
    return render(request,'staff_dashborad.html',{'staff_user':staff_user,'stud_count':stud_count})

def stud_dashboard(request):
    var_count=createQ.objects.count()
    stud_name=stud_reg.objects.get(firstname=stud_username)
    delete_res=stud_res.objects.all()
    delete_res.delete()
    return render(request,'stud_dash.html',{'var_count':var_count,'stud_name':stud_name})

def stud_result(request):
    global crt_ans
    global wrong_ans
    global count
    global stud_username
    global answer
    context = {}
    context['disp1'] = stud_res.objects.all()
    context['correctanswer'] = crt_ans
    context['wronganswer'] = wrong_ans
    context['count'] = count
    context['username'] = stud_username
    return render(request,'stud_result.html',context)

def staff_login(request):
    if request.method == 'POST':
        if staff_reg.objects.filter(username=request.POST['username'],password=request.POST['password']).exists():
            ex1=staff_reg.objects.get(username=request.POST['username'],password=request.POST['password'])
            global staff_username
            staff_username = ex1.username
            staff_user=staff_reg.objects.get(username=staff_username)
            easygui.msgbox("Login Successful..")
            return redirect(staff_dash)
        else :
            easygui.msgbox("Login Failed")
            return redirect(staff_login)
    return render(request,'staff_login.html')

def stud_re(request):
    return render(request,'stud_reg.html')

def stud_login(request):
    if request.method == 'POST':
        if stud_reg.objects.filter(email_id=request.POST['email_id'],password=request.POST['password']).exists():
            ex1=stud_reg.objects.get(email_id=request.POST['email_id'],password=request.POST['password'])
            global stud_username
            stud_username=ex1.firstname
            stud_name=stud_reg.objects.get(firstname=stud_username)
            easygui.msgbox("Login Successful..")
            return redirect(stud_dashboard)
        else :
            easygui.msgbox("Login Failed")
            return redirect(stud_login)
    return render(request,'stud_login.html')

def stud_reg_DB(request):
    if request.method == 'POST':
        var2=stud_reg(firstname=request.POST['first_name'],
                       lastname=request.POST['last_name'],
                       email_id=request.POST['email_id'],
                       password=request.POST['password'])
        var2.save()
        easygui.msgbox("Registration Successful!...")
        return redirect(stud_login)

def logout(request):
    log(request)
    easygui.msgbox("Logged Out..")
    return redirect(stud_login)

def staff_logout(request):
    log(request)
    easygui.msgbox("Loggedout Successfully!...")
    return redirect(staff_login)

def qno_disp(request):
    disp1=createQ.objects.all()
    return render(request,'qno_display.html',{'disp1':disp1})

def answerquestion(request,id):
    qa=createQ.objects.get(id=id)
    return render(request,'answerquestion.html',{'qa':qa})

def staff_result(request):
    global crt_ans
    global wrong_ans
    global count
    global stud_username
    context = {}
    context['correctanswer'] = crt_ans
    context['wronganswer'] = wrong_ans
    context['count'] = count
    context['username'] = stud_username
    
    return render(request,'staff_result.html',context)

def recorded_ques(request):
    rec_q=stu_rec.objects.all()
    return render(request,'recorded_question.html',{'rec_q':rec_q})