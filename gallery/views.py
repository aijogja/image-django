# Create your views here.

from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from gallery.models import Gallery, Comment
from gallery.forms import AddGalleryForm, AddCommentForm
from django.conf import settings

def custom_proc(request):
    return {
        'title': 'Image',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR'],        
    }

def gallery_index(request):
	gallery = Gallery.objects.all()
	return render_to_response('gallery.html', {'data_query':gallery}, context_instance=RequestContext(request, processors=[custom_proc]))

def gallery_detail(request, idgallery):
	gallery = Gallery.objects.get(pk=idgallery)
	comment = Comment.objects.filter(gallery=idgallery)
	if request.method == 'POST':
		form = AddCommentForm(request.POST) 
		if form.is_valid():
			user = User.objects.get(pk=request.user.id)
			gallery = Gallery.objects.get(pk=idgallery)
			komen = Comment()
			komen.user = user
			komen.gallery = gallery
			komen.comment = form.cleaned_data['comment']
			komen.save()
			form = AddCommentForm()
	else:
		form = AddCommentForm()

	return render_to_response('gallery_detail.html', {'data_query':gallery, 'data_comment':comment, 'form':form}, context_instance=RequestContext(request, processors=[custom_proc]))

@login_required
def add_gallery(request):
	if request.method == 'POST':
		form = AddGalleryForm(request.POST) 
		if form.is_valid():
			user = User.objects.get(pk=request.user.id)
			gallery = Gallery()

			f = request.FILES['image']
			path = Upload_Image(filename=f)

			gallery.image = path
			gallery.user = user
			gallery.save()

			return HttpResponseRedirect('/')
	else:
		form = AddGalleryForm() 
	return render_to_response('add_gallery.html', {'form':form}, context_instance=RequestContext(request, processors=[custom_proc]))

def Upload_Image(filename):
	path = '%s/%s' % ('gallery', str(filename.name))
	fd = open('%s/%s' % (settings.MEDIA_ROOT,path), 'wb')
	for chunk in filename.chunks():
		fd.write(chunk)
	fd.close()
	return path
