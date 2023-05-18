from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm
from .models import cPost

# Create your views here.
def cLanguage(request):
    posts = cPost.objects.all().order_by('-created_at')
    return render(request, 'cLanguage.html', {'posts':posts})
    #return render(request, "cLanguage.html")

def create_c(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cLanguage')
    else:
        form = PostModelForm()
    return render(request, 'form_create_c.html', {'form':form})


def post_detail_c(request, id): # 글 들어가서 자세히 보는 거
    post = get_object_or_404(cPost, pk=id)
    context={
        'cPost':post
    }
    return render(request, 'post_detail_c.html', context)

def post_update_c(request, id): # 수정하기
    post = get_object_or_404(cPost, pk=id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post) #instance는 기존내용 가져오기
        if form.is_valid():
            form.save()
            return redirect('cLanguage')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'form_create_c.html',{'form':form, 'id':id})
    
    
def post_delete_c(request, id): # 삭제하기
    post = cPost.objects.get(pk=id)
    post.delete()
    return redirect('cLanguage')