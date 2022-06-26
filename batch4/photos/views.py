from django.shortcuts import render
from .forms import ImageForm
from .models import PhotoGallary
import os 
# Create your views here.

def multiple_upload(request):
	img = PhotoGallary.objects.all()
	fm = ImageForm()
	if request.method == 'POST':
		fm = ImageForm(request.POST,request.FILES)
		files  = request.FILES.getlist('multipleimages')
		if fm.is_valid():
			for f1 in files:
				print ("names", f1)
				gallery = PhotoGallary(multipleimages=f1)
				gallery.save()

	print ("we are at ", os.getcwd())

	context = {"form": fm, "galimg": img}


	return render(request,"photos/upload.html", context)

def multiple_upload_pdf(request):
	list_all= []
	img = PhotoGallary.objects.all()
	fm = ImageForm()
	if request.method == 'POST':
		fm = ImageForm(request.POST,request.FILES)
		files  = request.FILES.getlist('multipleimages')
		if fm.is_valid():
			i = 1
			for f1 in files:
				print ("names", f1)
				#gallery = PhotoGallary(multipleimages=f1)
				#gallery.save()
				img_save_path = "ok/"+str(i)+".jpg"
				list_all.append(img_save_path)
				with open(img_save_path, 'wb+') as f:
					for chunk in f1.chunks():
						f.write(chunk)
					f.close()
				i = i+1

		from PIL import Image
		import os
		list_files = list_all   ## files to be given
		file1 = list_files[0]
		im1 = Image.open(file1)
		im_list = []
		for each in list_files[1:]:
			im_list.append(Image.open(each))
			pdf1_filename = "ok/"+"bbd2.pdf" 
			pdf1_filename1 = "bbd2.pdf"            ## file pdf 
		im1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list)
		context = {"file": pdf1_filename1}
		return render(request, 'photos/download.html', context)

	context = {"form": fm, "galimg": img}
	return render(request,"photos/upload.html", context)

from django.http import FileResponse 

def download_file(request,file):
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	print ("Base", BASE_DIR)
	print ("base1", os.path.dirname(os.path.abspath(__file__)))
	print ("base2", os.path.abspath(__file__))
	file_path = BASE_DIR + "/ok/"+file  
	return FileResponse(open(file_path,'rb'), as_attachment=True, content_type='application/pdf')