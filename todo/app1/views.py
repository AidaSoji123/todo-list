from django.shortcuts import redirect, render

from app1.models import TaskList, UserDetails

# Create your views here.
def signup(request):
    message = ''
    status = False
    if request.method == 'POST':  
        name = request.POST['name'] 
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print(name+username+email+password)    
        user_exist = UserDetails.objects.filter(email = email).exists()

        if not user_exist: 
            user = UserDetails(name = name, username = username,email = email,password = password)
            user.save()
            message = 'Registration Successful'
            status = True
        
        else:
            message = 'Email Exists please login'
    return render(request, 'signup.html', {'msg': message})

def login(request):
    
    message=''
    if request.method=='POST':
        username_get=request.POST['username']
        password_get=request.POST['password']
        
        try: 
            admin=UserDetails.objects.get(username=username_get,password=password_get)
            return redirect('app1:index')
        except Exception as e:
            print(e)
            message='Invalid username or password'
    return render(request,'login.html',{'msg':message})


def index(request):
    tasks= TaskList.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def task(request):
   
    message = ''
    
    if request.method == 'POST':
      
        title = request.POST['title'].lower()
        description = request.POST['description']
        due_date = request.POST['duedate']
    
        print(description)
        task_exist = TaskList.objects.filter(title = title).exists()

        if not task_exist:
            task = TaskList(title = title, description = description, due_date = due_date)
            task.save()
            message = 'task Added'
            
        else:
            message = 'Already Added'
    return render(request,'task.html', {'message': message, })

  
def reset(request):
    
    return render(request, 'reset.html')

def delete_task(request,task_id):
    task=TaskList.objects.get(id=task_id)
    task.delete()
    return redirect ('app1:index')

def update_status(request,task_id):
    task=TaskList.objects.get(id=task_id)
    task.status=True
    task.save()
    print(task)
    return redirect ('app1:index')

def edit_task(request,task_id):
    task=TaskList.objects.get(id=task_id)
    task.save()
    return redirect ('app1:index')