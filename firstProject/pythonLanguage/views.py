from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm
from .models import pythonPost
# Create your views here.

def pythonLanguage(request):
    posts = pythonPost.objects.all().order_by('-created_at')
    return render(request, 'pythonLanguage.html', {'posts':posts})

def create_p(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pythonLanguage')
    else:
        form = PostModelForm()
    return render(request, 'form_create_p.html', {'form':form})


def post_detail_p(request, id): # 글 들어가서 자세히 보는 거
    post = get_object_or_404(pythonPost, pk=id)
    context={
        'pythonPost':post
    }
    return render(request, 'post_detail_p.html', context)

def post_update_p(request, id): # 수정하기
    post = get_object_or_404(pythonPost, pk=id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post) #instance는 기존내용 가져오기
        if form.is_valid():
            form.save()
            return redirect('pythonLanguage')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'form_create_p.html',{'form':form, 'id':id})
    
    
def post_delete_p(request, id): # 삭제하기
    post = pythonPost.objects.get(pk=id)
    post.delete()
    return redirect('pythonLanguage')