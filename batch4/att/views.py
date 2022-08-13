from django.shortcuts import render
from .forms import StudentMasterForm, StudentAttForm, StudentAttFormDisplay
from django.shortcuts import render
from django.contrib import messages 
import time 
from .models import Mark_Attendance2, MasterData2

# Create your views here.

def StudentMaster(request):
	form = StudentMasterForm()
	context = {'form' : form, 'legend' :" Register today"}
	if request.method =='POST':
		form =  StudentMasterForm(request.POST)
		if form.is_valid():
			mark1 =form.save(commit=False)
			form.save()
			messages.success(request,f"Record added ")
		else:
			messages.warning(request,f"Error in the form")
	return render(request,"att/disform.html", context)

def e_h(t1):
	t9=time.localtime(t1)
	return time.strftime("%d-%m-%Y-%H",t9)

def Mark_Att(request):
	form = StudentAttForm()
	context = {'form' : form, 'legend' :"Mark your Attendance"}
	try :
		if request.method=='POST':

			form = StudentAttForm(request.POST)
			if form.is_valid():
				print ("Hello ")
				mark1 =form.save(commit=False)
				mark1.time1 = int(time.time())
				mark1.ip_address = request.META.get('REMOTE_ADDR')
				mark1.platform = request.META.get('HTTP_USER_AGENT',"Unknown")
				mark1.date1 = e_h(mark1.time1)
				form.save()
				messages.success(request,f"{mark1.uid}, your Attendance is marked ")
			else:
				messages.warning(request,f"Error in the form")
	except Exception as e :
		messages.warning(request,f"{e}")
	return render(request,"att/disform.html", context)


def display_attendance(request):
	posts = Mark_Attendance2.objects.all()
	context = {"data": posts}
	return render(request,'att/displayallatt.html',context)


def display_attendanceone(request):
	form = StudentAttFormDisplay()
	context = {'form' : form}
	if request.method=='POST':
		form = StudentAttFormDisplay(request.POST)
		if form.is_valid():
			d1 = form.cleaned_data
			u1 = d1.get('UID')
			posts = Mark_Attendance2.objects.filter(uid=u1)
			context = {"data": posts}
			return render(request,'att/displayallatt.html',context)


	#posts = Mark_Attendance2.objects.all()
	#context = {"data": posts}
	return render(request,'att/disform.html',context)

############################################# REST Function API################
from .serializer import AttSerializer, AttSerializer1
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io


def studentdetails(request,pk):
	try:
		stu = MasterData2.objects.get(id=pk) # model complex object 
		serializer = AttSerializer(stu)
		json_data = JSONRenderer().render(serializer.data)
		print(json_data)
	except Exception as e :
		print (e)
		json_data = '{"Not get": "NIL"}'
	return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def student_api(request):
	if request.method=="GET":
		json_data = request.body  # data from myapp.py
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)  # python dictionary 
		id1  = pythondata.get('id',None)
		if id1 is not None:
			print ("id",id1)
			stu = MasterData2.objects.get(id=id1) # model complex object 
			serializer = AttSerializer(stu)
			json_data = JSONRenderer().render(serializer.data)
			print(json_data)
			return HttpResponse(json_data, content_type='application/json')  # json reponse 

	if request.method=='POST':
		json_data = request.body  # data from myapp.py
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		serial = AttSerializer(data=pythondata)
		if serial.is_valid():
			serial.save()
			res = {'msg': 'Data create'}
			return JsonResponse(res,safe=False)

		json_data = JSONRenderer().render(serial.error)
		return HttpResponse(json_data, content_type='application/json')  # json reponse 

	if request.method=='PUT':
		json_data = request.body  # data from myapp.py
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id1  = pythondata.get('stuid',None)
		stu = MasterData2.objects.get(stuid=id1)
		serial = AttSerializer(stu,data=pythondata,partial=True)
		if serial.is_valid():
			serial.save()
			res = {'msg': 'Data updated'}
			return JsonResponse(res,safe=False)

		json_data = JSONRenderer().render(serial.error)
		return HttpResponse(json_data, content_type='application/json')


	if request.method== 'DELETE':
		json_data = request.body  # data from myapp.py
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id1  = pythondata.get('stuid',None)
		stu = MasterData2.objects.get(stuid=id1)
		stu.delete()
		res = {'msg': 'Data deleted'}
		return JsonResponse(res,safe=False)

######################### GENERIC class API #############
from rest_framework.generics import ListAPIView  # viewing purpose 
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly, DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from .permissions import MohitPermission

class MasterListAPI(ListAPIView):
	queryset = MasterData2.objects.all()
	serializer_class = AttSerializer1
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]



from rest_framework.generics import CreateAPIView 
class MasterCreateAPI(CreateAPIView):
	queryset = MasterData2.objects.all()
	serializer_class = AttSerializer

from rest_framework.generics import RetrieveAPIView 
class MasterRetrieveAPI(RetrieveAPIView):
	queryset = MasterData2.objects.all()
	serializer_class = AttSerializer

from rest_framework.generics import UpdateAPIView 
class MasterUpdateAPI(UpdateAPIView):
	queryset = MasterData2.objects.all()
	serializer_class = AttSerializer


from rest_framework.generics import DestroyAPIView 
class MasterDestroyAPI(DestroyAPIView):
	queryset = MasterData2.objects.all()
	serializer_class = AttSerializer

from rest_framework.generics import ListCreateAPIView  # view and create #########3
class MasterListCreateAPI(ListCreateAPIView):
	queryset = MasterData2.objects.all()
	serializer_class = AttSerializer
	#authentication_classes = [BasicAuthentication]
	authentication_classes =[TokenAuthentication]
	#permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
	#permission_classes = [IsAuthenticated,MohitPermission]
	permission_classes = [IsAuthenticated]


from rest_framework.generics import RetrieveUpdateAPIView 
class MasterRetUpdate(RetrieveUpdateAPIView):
	queryset = MasterData2.objects.all()
	serializer_class = AttSerializer

from rest_framework.generics import RetrieveDestroyAPIView 
class MasterRetDes(RetrieveDestroyAPIView):
	queryset = MasterData2.objects.all()
	serializer_class = AttSerializer

from rest_framework.generics import RetrieveUpdateDestroyAPIView 
class MasterRUD(RetrieveUpdateDestroyAPIView):
	queryset = MasterData2.objects.all()
	serializer_class = AttSerializer



