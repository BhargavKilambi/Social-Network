from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm,EditProfileForm,FeedbackForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from accounts.models import Feedback1
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,'accounts/profile.html')

def about(request):
    return render(request,'accounts/about.html')



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts')
    else:
        form = RegistrationForm()


    return render(request,'accounts/reg_form.html',{'form':form})

@login_required
def view_profile(request):
    args = {'user':request.user}
    return render(request,'accounts/profile.html',args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)

        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = EditProfileForm(instance = request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)



class HomeView(TemplateView):
    template_name = 'accounts/about.html'

    def get(self, request):
        feed = FeedbackForm()
        args = {'feed':feed}
        return render(request, self.template_name,args)


    def post(self,request):
        feed = FeedbackForm
        if request.method == 'POST':
            feed = FeedbackForm(request.POST)
            if feed.is_valid():
                post = feed.save(commit=False)
                post.user = request.user
                post.save()
                text = feed.cleaned_data['text']
                feed = FeedbackForm(request.GET)
                return redirect('/accounts/about')

            return render(request, self.template_name,{'feed': feed,'text':text })


# class EditBio(TemplateView):
#     template_name = 'accounts/profile.html'
#
#     def get(self, request):
#         feed = EditBioForm()
#         bio = Bio.objects.all()
#         args = {'feed':feed,'bio':bio}
#         return render(request, self.template_name,args)
#
#
#     def post(self,request):
#         feed = EditBioForm
#         if request.method == 'POST':
#             feed = EditBioForm(request.POST)
#             if feed.is_valid():
#                 post = feed.save(commit=False)
#                 post.user = request.user
#                 post.save()
#                 text = feed.cleaned_data['text']
#                 feed = EditBioForm(request.GET)
#                 return redirect('/accounts/about')
#
#             return render(request, self.template_name,{'feed': feed,'text':text })
