from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count, Min, Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth import authenticate

# Create your views here.

def index(request):
	if request.method == "POST":
		form = JournalForm(request.POST,)
		if form.is_valid():
			new_journal = form.save(commit=False)
			new_journal.save()
			return redirect('index')
	else:

		form = JournalForm()

	context = {
		'form': form,
    	'acc_debit': Account.objects.all(),
    	'acc_ccy': Ccy.objects.all(),    
        }

	return render(request, 'finapp/index.html', context)

def balance(request):

	context = {
		'journal_entries': Journal.objects.all(),
	}


	return render(request, 'finapp/balance-sheet.html', context)

