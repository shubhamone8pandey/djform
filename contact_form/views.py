from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # process the form data here
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})