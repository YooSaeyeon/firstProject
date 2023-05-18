from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm
from .models import javaPost

# Create your views here.
def javaLanguage(request):
    posts = javaPost.objects.all().order_by('-created_at')
    return render(request, 'javaLanguage.html', {'posts':posts})

def create_j(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('javaLanguage')
    else:
        form = PostModelForm()
    return render(request, 'form_create_j.html', {'form':form})


def post_detail_j(request, id): # 글 들어가서 자세히 보는 거
    post = get_object_or_404(javaPost, pk=id)
    context={
        'javaPost':post
    }
    return render(request, 'post_detail_j.html', context)

def post_update_j(request, id): # 수정하기
    post = get_object_or_404(javaPost, pk=id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post) #instance는 기존내용 가져오기
        if form.is_valid():
            form.save()
            return redirect('javaLanguage')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'form_create_j.html',{'form':form, 'id':id})
    
    
def post_delete_j(request, id): # 삭제하기
    post = javaPost.objects.get(pk=id)
    post.delete()
    return redirect('javaLanguage')