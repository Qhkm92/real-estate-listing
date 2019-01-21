from django.shortcuts import render

# Create your views here.
def contact(request):
	# Content from database request extracted here
	# and passed to the template for display
	return render(request, 'about/contact.html')