from django.shortcuts import render, redirect, get_object_or_404
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Blog
from .forms import BlogForm
from pathlib import Path

path = Path(__file__).parent.absolute()
txt_path = str(path) +'/static/german/dictionary.txt'
qstns_cnt = 0
ans_cnt = 0
# Create your views here.
def home(request):
    return render(request, 'german/home.html')

def dictionary(request):
    # with open(txt_path) as f:
    #     content = f.readlines()
    #     # you may also want to remove whitespace characters like `\n` at the end of each line
    #     nouns = []
    #     for line in content:
    #         nouns.append(line.strip().split(' ')[1:])
    #     # content = [x.strip() for x in content]
    nouns = readtxt(txt_path)
    return render(request, 'german/dictionary.html', {'nouns':nouns})


def artikelquiz(request):
    global qstns_cnt
    global ans_cnt
    if request.method == "GET":
        qstns_cnt = 0
        ans_cnt = 0
        nouns = readtxt(txt_path)
        noun = random.choice(nouns)
        return render(request, 'german/artikelquiz.html', {'noun':noun, 'score': f'{ans_cnt}/{qstns_cnt}'})
    else:
        qstns_cnt += 1
        nouns = readtxt(txt_path)
        noun = random.choice(nouns)
        artikel = request.POST['answer']
        name = request.POST['nounname']
        # print('*******', request.POST['nounname'])
        if request.POST['answer'] == request.POST['artikel'].lower():
            ans_cnt += 1
            return render(request, 'german/artikelquiz.html', {'noun':noun, 'msg': f'Correct! {artikel} {name}', 'score': f'{ans_cnt}/{qstns_cnt}'})
        else:
            return render(request, 'german/artikelquiz.html', {'noun':noun, 'msg': f'Wrong!   {artikel} {name}', 'score': f'{ans_cnt}/{qstns_cnt}'})



def wordquiz(request):
    all_nouns = readtxt(txt_path)
    four_nouns = []
    for _ in range(4):
        four_nouns.append(random.choice(all_nouns))
    q_noun = four_nouns[0]
    random.shuffle(four_nouns)
    if request.method == "GET":
        return render(request, 'german/wordquiz.html', {'noun1':four_nouns[0], 'noun2':four_nouns[1], 'noun3':four_nouns[2], 'noun4':four_nouns[3], 'qnoun':q_noun})
    else:
        qstn = request.POST['qstn']
        ans = request.POST['ans']
        if request.POST['ans'] == request.POST['selected_option']:
            return render(request, 'german/wordquiz.html', {'result': f'correct! {qstn} : {ans}' , 'noun1':four_nouns[0], 'noun2':four_nouns[1], 'noun3':four_nouns[2], 'noun4':four_nouns[3], 'qnoun':q_noun})
        else:
            return render(request, 'german/wordquiz.html', {'result': f'wrong! {qstn} : {ans}' , 'noun1':four_nouns[0], 'noun2':four_nouns[1], 'noun3':four_nouns[2], 'noun4':four_nouns[3], 'qnoun':q_noun})



def readtxt(path):
    with open(path) as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        nouns = []
        for line in content:
            line = line.strip().split(' ')[1:]
            # print(line)
            w = word()
            w.name = line[3].lower()
            w.meaning = line[0].lower()
            w.artikel = line[2].lower()
            nouns.append(w)
    return nouns

def germanblogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'german/germanblogs.html', {'blogs':blogs})

def detailblog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'german/detailblog.html', {'blog':blog})

@login_required
def createblog(request):
    if request.method == "GET":
        return render(request, 'german/createblog.html', {'form': BlogForm()})
    else:
        try:
            form = BlogForm(request.POST)
            newblog = form.save(commit=False)
            newblog.user = request.user
            newblog.save()
            return redirect('germanblogs')
        except ValueError:
            return render(request, 'german/createblog.html', {'form': BlogForm(), 'error': 'Some error in the creation of Blog'})

@login_required
def deleteblog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == "POST":
        blog.delete()
        return redirect('germanblogs')

@login_required
def editblog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == "GET":
        return render(request, 'german/editblog.html', {'blog':blog})
    else:
        try:
            form = BlogForm(request.POST, instance=blog)
            form.save()
            return redirect('germanblogs')
        except ValueError:
            return render(request, 'german/editblog.html', {'blog':blog, 'error':'Something is wrong! please check again'})

def loginpage(request):
    if request.method == "GET":
        return render(request, 'german/loginpage.html', {'form': AuthenticationForm()})

    else:
        user = authenticate(request, username = request.POST["username"], password = request.POST["password"])
        if user is None:
            return render(request, 'german/loginpage.html', {'form': AuthenticationForm()}, {'error': 'username and password did not match!'})
        else:
            login(request, user)
            return redirect('home')

@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

class word():
    name = ''
    meaning = ''
    artikel = ''