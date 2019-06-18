from django.shortcuts import render

# Create your views here.

lst = [
    {'待办事项': '吃饭', '已完成': False},
    {'待办事项': '逛街', '已完成': False}
]

def home(request):
    global  lst
    if request.method == "POST":
        content = request.POST.get('待办事项')
        if content =='':
            return render(request, 'todoapp/home.html', {'清单': lst})
        else:
            lst.append({'待办事项': content, '已完成': False})
            return render(request, 'todoapp/home.html', {'清单': lst})
    else:
        return render(request, 'todoapp/home.html', {'清单': lst})
def edit(request):
    return render(request, 'todoapp/edit.html')
def about(request):
    return render(request, 'todoapp/about.html')