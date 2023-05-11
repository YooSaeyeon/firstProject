from django.shortcuts import render
from .forms import PostModelForm

# Create your views here.
def contacted(request):
    if request.method == 'POST':
        # 입력 내용을 DB에 저장
        form = PostModelForm(request.POST)
        # 제대로 입력되었는지 검사하는 코드
        if form.is_valid(): 
            # 유효하다면 저장하는 코드
            form.save() 
            return redirect('home') 
    else:
        form = PostModelForm() 
    return render(request, 'contacted.html', {'form':form})

# def create(request):
#     if request.method == 'POST':
#         # 입력 내용을 DB에 저장
#         form = PostModelForm(request.POST)
#         # 제대로 입력되었는지 검사하는 코드
#         if form.is_valid(): 
#             # 유효하다면 저장하는 코드
#             form.save() 
#             return redirect('home') 
#     else:
#         form = PostModelForm() 
#     return render(request, 'contacted.html', {'form':form})