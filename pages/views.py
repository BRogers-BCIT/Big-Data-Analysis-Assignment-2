from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import TemplateView

# Create your views here.


def production_page_view(request):
    # Create production input page.
    return render(request, 'production.html')


def production_post(request):
    try:
        # Extract values from request object by name.
        input1 = request.POST['A']
        input2 = request.POST['B']
    except:
        # Create related error message.
        # Return back with an error message on failure
        return render(request, 'production.html', {'errorMessage': 'Missing Inputs.'})
    else:
        # Return an HttpResponseRedirect to prevent POST being sent twice.
        return HttpResponseRedirect(reverse('prediction_page_view', kwargs={'A': input1, 'B': input2}))


def prediction_page_view(request, input1, input2):
    # Call prediction with input values
    return render(request, "prediction.html", {'A': input1, 'B': input2})
