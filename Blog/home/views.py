from django.shortcuts import render,redirect
from home.forms import HomeForm
from django.views.generic import TemplateView
from .models import Post
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        post = Post.objects.all().order_by('-created_date')
        args = {'post':post,'form':form}
        return render(request, self.template_name,args)


    def post(self,request):
        form = HomeForm
        if request.method == 'POST':
            form = HomeForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                text = form.cleaned_data['text']
                title = form.cleaned_data['title']
                form = HomeForm(request.GET)
                return redirect('/home')

            return render(request, self.template_name,{'form': form,'title':title,'text':text })
