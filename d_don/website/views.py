from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddDonationForm
from .models import Record

def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in successfully!")
            return redirect('home')
        else:
            messages.error(request, "There was an error. Please try again.")
            return redirect('home')
    else:  
        return render(request, 'home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered!")
            return redirect('home')  # Consider redirecting to a different view
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})



# def donation_record(request, pk):
#     if request.user.is_authenticated:
#         donation_record = get_object_or_404(Record, id=pk)
#         return render(request, 'record.html', {'donation_record': donation_record})
#     else:
#         messages.error(request, "You must be logged in")
#         return redirect('home')

def donation_record(request, pk):
    donation_record = get_object_or_404(Record, id=pk)
    return render(request, 'record.html', {'donation_record': donation_record})

def records_list(request):
    records = Record.objects.all()
    return render(request, 'records_list.html', {'records': records})




def delete_donation(request, pk):
    if request.user.is_authenticated:
        try:
            delete_it = get_object_or_404(Record, id=pk)
            delete_it.delete()
            messages.success(request, "Record deleted successfully!")
        except Record.DoesNotExist:
            messages.error(request, "Record not found.")
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
        return redirect('home')
    else:
        messages.error(request, "You must be logged in to delete a record.")
        return redirect('home')
    



def add_donation(request):
    form = AddDonationForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_donation = form.save()
                messages.success(request, "donation added successfully")
                return redirect('home')
        return render(request, 'add_donation.html', {'form' : form})
    else:
        messages.error(request, " you must be logged in to add") 


def update_donation(request, pk):
    donation = get_object_or_404(Record, pk=pk)
    
    if request.method == 'POST':
        form = AddDonationForm(request.POST, instance=donation)
        if form.is_valid():
            form.save()
            messages.success(request, "Donation updated successfully.")
            return redirect('home')
    else:
        form = AddDonationForm(instance=donation)
    
    return render(request, 'update_donation.html', {'form': form})