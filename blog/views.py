from django.shortcuts import render, HttpResponse,redirect
from blog.models import Post,BlogComment
from django.contrib import messages
from blog.templatetags import extras

def bloghome(request):
	allPosts = Post.objects.all()
	context = {'allPosts': allPosts}
	return render(request,'blog/bloghome.html',context)

def blogPost(request,slug):
	post = Post.objects.filter(slug=slug).first()
	comments = BlogComment.objects.filter(post=post, parent=None)
	replies = BlogComment.objects.filter(post=post).exclude(parent=None)
	repDict={}
	for reply in replies:
		if reply.parent.sno not in repDict.keys():
			repDict[reply.parent.sno] = [reply]
		else:
			repDict[reply.parent.sno].append(reply)

	print(request.user)
	context = {'post':post, 'comments': comments , 'user': request.user, 'repDict':repDict}
	return render(request,'blog/blogPost.html',context)

def postComment(request):
	if(request.method == "POST"): 
		comment = request.POST.get("comment")
		user = request.user
		postSno = request.POST.get("postSno")
		post = Post.objects.get(sn0 = postSno)
		parentSno = request.POST.get("parentSno")
		if parentSno == "":
			comment = BlogComment(comment=comment,user=user,post=post)
			comment.save()
			messages.success(request,"Your Comment posted")
		else:
			parent = BlogComment.objects.get(sno=parentSno)
			comment = BlogComment(comment=comment,user=user,post=post,parent=parent)
			comment.save()
			messages.success(request,"Your Reply posted successfully")
	return redirect(f"/blog/{post.slug}")

# Create your views here.
