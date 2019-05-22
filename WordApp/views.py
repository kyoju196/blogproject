from django.shortcuts import render

def word_home(request):
    return render(request, 'word_home.html')
def word_detail(request):
    return render(request, 'word_detail.html')
def word_result(request):
    text = request.GET['fulltext']
    #전체 텍스트 받아오고 싶어요
    words = text.split()
    #총 단어수 갯수 받아온거야
    word_dic = {}
    #안녕 : 1 <--이걸 하고싶은거야
    for word in words:
        if word in word_dic:
            word_dic[word] +=1 #카운트 하나 더
        else:
            word_dic[word] =1 #한번 나왔구나
    return render(request, 'word_result.html', {'full' : text, 'total' : len(words), 'dictionary' : word_dic.items}) 

# Create your views here.
