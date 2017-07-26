import json
from django.http import HttpResponse
from django.shortcuts import render
from .forms import Access_Token
from .utils import grab_data_from_facebook


def Homepage(request):

    template_name="grab_data/home.html"

    return render(request,template_name,{})

def Instructions(request):

    template_name="grab_data/instructions.html"

    return render(request,template_name,{})


def About(request):

    template_name="grab_data/about.html"

    return render(request,template_name,{})

def Developer(request):

    template_name="grab_data/developer.html"

    return render(request,template_name,{})



def GetData(request):

    form=Access_Token(request.POST or None)

    if form.is_valid():

        qs=grab_data_from_facebook(
                                    token=form.cleaned_data.get("token"),
                                    types_of_data=form.cleaned_data.get("types_of_data"),
                                    data_fields=form.cleaned_data.get("data_fields"),
                                    number_of_data=form.cleaned_data.get("number_of_data")

                                    )
        data=json.dumps(qs)
        return HttpResponse(data, content_type = "application/json")


    template_name="grab_data/token_entry.html"
    context={"form":form}

    return render(request,template_name,context)
