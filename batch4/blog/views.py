from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .decorators import allowed_user

@login_required(login_url='login')
@allowed_user(allowed_roles=['read','write'])
def Allpost(request,page=1):
	posts = Post.objects.all()
	p1 = Paginator(posts,2)
	posts = p1.page(page)
	context = {'posts': posts}
	return render(request,'blog/all_posts.html', context)

def SpecificPost(request,id1):
	post = Post.objects.filter(id=id1)[0]
	context = {'post':  post}
	return render(request, 'blog/onepost.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['write'])
def CreatePost(request):
	form = PostForm()
	context = {"form":form}
	if request.method=='POST':
		form = PostForm(request.POST)
		if form.is_valid():
			mark1 = form.save(commit=False)
			mark1.author = request.user
			form.save()
			return redirect('Allposts')

	return render (request,'blog/createpost.html', context)

# Create your views here.

##################################################
## Class based view 
from django.views.generic import CreateView, ListView, DetailView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title','content']
	template_name = 'blog/createpost.html'
	login_url = '/login/'
	#success_url = '/post/post/view/'

	def form_valid(self,form):
		form.instance.author = self.request.user 
		return super().form_valid(form)


class PostListView(LoginRequiredMixin,ListView):
	model = Post 
	template_name = 'blog/all_posts_cls.html'
	ordering = ['-date1']
	context_object_name = 'posts'  # by default object_list
	login_url = '/login/'
	paginate_by = 4     

class PostDetailView(LoginRequiredMixin,DetailView):
	model = Post 
	template_name = 'blog/onepost.html'
	context_object_name = 'post'
	login_url = '/login/'

class UserPostListView(LoginRequiredMixin,ListView):
	model = Post 
	template_name = 'blog/all_posts_cls.html'
	ordering = ['-date1']
	context_object_name = 'posts'  # by default object_list
	login_url = '/login/'
	paginate_by = 4

	def get_queryset(self):
		return Post.objects.filter(author=self.request.user)


class OtherUserPostListView(LoginRequiredMixin,ListView):
	model = Post 
	template_name = 'blog/all_posts_cls.html'
	ordering = ['-date1']
	context_object_name = 'posts'  # by default object_list
	login_url = '/login/'
	paginate_by = 4

	def get_queryset(self):
		#user = get_object_or_404(User,username = self.kwargs.get('u1') )
		#return Post.objects.filter(author=user)
		return Post.objects.filter(author=self.kwargs.get('u1'))


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Post
	fields = ['title','content']
	template_name = 'blog/createpost.html'
	login_url = '/login/'
	#success_url = '/post/post/view/'

	def form_valid(self,form):
		form.instance.author = self.request.user 
		return super().form_valid(form)

	def test_func(self):

		post = self.get_object()
		if self.request.user == post.author:
			return True 
		else :
			return False 

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
	model = Post 
	success_url ='/post/post/view/'

	def test_func(self):

		post = self.get_object()
		if self.request.user == post.author :
			return True 
		else :
			return False 

@login_required(login_url='login')
def CommentPost(request,id1):
	form = CommentForm()
	post = Post.objects.filter(id=id1)[0]
	comments = post.comment_post.all()
	if request.method=='POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			mark1 = form.save(commit=False)
			mark1.post = post
			mark1.author = request.user 
			form.save()
	context = {'form':form, 'post': post,"comments": comments }
	return render(request, 'blog/one_post_func_comment.html', context)


def comment_approve(request,id1):  # This is comment id not the post id 
	comment = get_object_or_404(Comment,id=id1)
	comment.approve()
	return redirect('post-comment',id1=comment.post.id)