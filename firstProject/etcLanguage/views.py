from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm
from .models import etcPost

# Create your views here.
def etcLanguage(request):
    posts = etcPost.objects.all().order_by('-created_at')
    return render(request, 'etcLanguage.html', {'posts':posts})

def create_e(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('etcLanguage')
    else:
        form = PostModelForm()
    return render(request, 'form_create_e.html', {'form':form})


def post_detail_e(request, id): # 글 들어가서 자세히 보는 거
    post = get_object_or_404(etcPost, pk=id)
    context={
        'etcPost':post
    }
    return render(request, 'post_detail_e.html', context)

def post_update_e(request, id): # 수정하기
    post = get_object_or_404(etcPost, pk=id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post) #instance는 기존내용 가져오기
        if form.is_valid():
            form.save()
            return redirect('etcLanguage')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'form_create_e.html',{'form':form, 'id':id})
    
    
def post_delete_e(request, id): # 삭제하기
    post = etcPost.objects.get(pk=id)
    post.delete()
    return redirect('etcLanguage')
