from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Account, Bike, Notes
import datetime

def balanceView(request):
	if request.user.is_authenticated:
		return JsonResponse({'username': request.user.username, 'balance': request.user.account.balance, 'dob':request.user.account.dob})
	else:
		return JsonResponse({'username': 'anonymous', 'balance': 0})

@login_required
def homePageView(request):
	staff = User.objects.get(id=request.user.id).is_staff
	if staff ==1:
		accounts = Account.objects.all()
		bikes = Bike.objects.filter(status=0)
	else:
		accounts = Account.objects.filter(user_id=request.user.id)
		bikes = Bike.objects.filter(owner=request.user.id)
	bikes2 = []
	for i in bikes:
		bikes2.append((i,Notes.objects.filter(bike=i.id)))
	all_bikes = []
	b = Bike.objects.all()
	for i in b:
		all_bikes.append((i,Notes.objects.filter(bike=i.id)))
	return render(request, 'pages/index.html', {'accounts': accounts, 'staff':staff, 'bikes': bikes, 'bikes2':bikes2, 'all_bikes' : all_bikes})


def editView(request):
	if request.method == 'POST' and User.objects.get(id=request.user.id).is_staff == 1: # is_staff tarkistus
		bike = request.POST.get('bike')
		note = request.POST.get('note')
		writer = request.POST.get('writer')
		date = request.POST.get('date') #ei toimi
		status = request.POST.get('status')
		b = Bike.objects.get(id=bike)
		b.status = status
		b.save()
		print(status)
		if note != "":
			Notes.objects.create(note=note,bike=Bike.objects.get(id=bike),writer=User.objects.get(username=writer),date=date)
	return redirect('/')

def newbikeView(request):
	if request.method == 'POST':
		notes = request.POST.get('notes')
		model = request.POST.get('model')
		owner = request.POST.get('owner')
		status = request.POST.get('status')
		writer = request.POST.get('writer')
		writer2 = User.objects.get(username=writer)
		bike = Bike.objects.create(owner=User.objects.get_or_create(username=owner)[0].id,model=model,status=status)
		Notes.objects.create(note=notes,bike=bike,writer=writer2)
	return redirect('/')




def adduserView(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		pw = request.POST.get('password')
		a = User.objects.filter(username=name).count()
		# a = User.objects.get_or_create(is_superuser=0,username=name,password=pw,is_staff=0,is_active=1,date_joined='2020-07-03') #save raw password to db
		if a == 0:
			newuser = User(is_superuser=0,username=name,is_staff=0,is_active=1,date_joined=datetime.datetime.now())
			newuser.set_password(pw)
			newuser.save()
			Account.objects.create(balance=0,dob='2002-01-01',user_id=newuser.pk) # save password to db encrypted
	accounts = Account.objects.all()
	return redirect('/')
