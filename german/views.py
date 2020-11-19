from django.shortcuts import render, redirect
import random

txt_path = '/home/qxw8310/ranjith/udemy/web_development/learngerman-project/german/static/german/dictionary.txt'
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
        return render(request, 'german/artikelquiz.html', {'noun':noun})
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

class word():
    name = ''
    meaning = ''
    artikel = ''