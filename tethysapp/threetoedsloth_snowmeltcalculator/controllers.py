from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    """
    Controller for the app home page.
    """

    context = {
    }

    return render(request, 'threetoedsloth_snowmeltcalculator/home.html', context)

@login_required()
def proposal(request):
    """
    Controller for the app proposal page.
    """

    context = {
    }

    return render(request, 'threetoedsloth_snowmeltcalculator/proposal.html', context)

@login_required()
def mockup(request):
    """
    Controller for the app mockup page.
    """

    context = {
    }

    return render(request, 'threetoedsloth_snowmeltcalculator/mockup.html', context)

@login_required()
def map(request):
    """
    Controller for the app map page.
    """

    context = {
    }

    return render(request, 'threetoedsloth_snowmeltcalculator/map.html', context)