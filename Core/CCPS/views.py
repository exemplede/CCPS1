from django.shortcuts import render, redirect, get_object_or_404
from .models import SiteVisit
from django.contrib.auth import logout, login, authenticate
from .models import User, Article, Image
from .forms import EditArticleForm, ImageFormSet


def testView(request):
    return render(request, 'CCPS/base.html')

def indexView(request):
    visit_count = SiteVisit.objects.first().count if SiteVisit.objects.exists() else 0
    return render(request, 'CCPS/index.html',
                  context={
                      'visit_count': visit_count,
                      'articles': Article.objects.all()[:3]
                    }
                )
    
def proposView(request):
    return render(request, 'CCPS/propos.html')

def equipementsView(request):
    return render(request, 'CCPS/equipement.html')





def loginView(request):
    if request.user.is_authenticated: # user already login => we log out
        logout(request)
        return redirect(to="home")
        
    
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email = email, password = password)
        
        if user:
            login(
                request,
                user
            )
            return redirect(to='home')
        
        return redirect(to='login') # because authentication failed
        
    return render(request, 'CCPS/login.html')


def registerView(request):
    if request.method == 'POST':
        email = request.POST['email']
        fullname = request.POST['fullname']
        password = request.POST['password']
        re_password = request.POST['re_password']
        
        if password != re_password:
            return redirect(to='register')
        
        try:
            user = User.objects.create(email=email, fullname=fullname)
            user.set_password(password)
            user.save() # persist it in database
        except Exception as e:
            print(e) # for debugging; TO DELETE IF NO LONGER NEEDED
            return redirect(to='register')
        
        return redirect(to='login') 
    
    return render(request, 'CCPS/register.html')


def dashboardView(request):
    if not request.user.is_superuser:
        return redirect(to='home')
    
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Article.objects.create(title=title, content=content, author=request.user).save()
        return redirect(to="dashboard")

    
    return render(request, 'CCPS/dashboard.html',
                  context={
                      'articles': Article.objects.all(),
                  }
                )
    
def articleDetailsView(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'CCPS/article_details.html', context={
        'article': article
    })

def articleEditView(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    if request.method == 'POST':
        form = EditArticleForm(request.POST, request.FILES, instance=article)
        formset = ImageFormSet(request.POST, request.FILES)
        
        if form.is_valid() and formset.is_valid():
            form.save()
            
            images = formset.save(commit=False)
            
            for image in images:
                image.article = article
                image.save()
        
        return redirect(to="dashboard")        
    
    form = EditArticleForm(instance=article)
    formset = ImageFormSet()
        
    return render(request, 'CCPS/article_edit.html', context={
        'article': article,
        'form': form,
        'formset': formset
    })

def articleDeleteView(request, pk):
    article = Article.objects.get(pk=pk)
    
    if not article:
        # redirect to the 404 page
        pass
    
    article.delete()
    
    return redirect(to='dashboard')

def imageDeleteView(request, pk):
    image = Image.objects.get(pk=pk)
    
    if not image:
        # redirect to the 404 page
        pass
    
    image.delete()
    
    return redirect(to='articleEdit', pk=image.article.pk)

def missionView(request):
    return render(request, "CCPS/mission.html")

def equipeView(request):
    return render(request, "CCPS/equipe.html")

def projetsView(request):
    return render(request, 'CCPS/projets.html')

def contView(request):
    return render(request, 'CCPS/cont.html')
def propos1View(request):
    return render(request, 'CCPS/propos1.html')