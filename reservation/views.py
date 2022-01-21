from django.shortcuts import render
from .models import Lawyer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import LawyerSerializer
from django.http import HttpResponseRedirect
from .forms import UploadFileForm

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
# Imaginary function to handle an uploaded file.
from .models import Document
@api_view(['GET','POST'])
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('views.list'))
    else:
        form = UploadFileForm() # A empty, unbound form
    
    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(request,
        'list.html',
        {'documents': documents,'form': form}
    )


# Create your views here.
@api_view(['GET'])
def lawyer_list(request):
    if request.method == 'GET':
        lawyers=Lawyer.objects.get()
        serializer=LawyerSerializer(lawyers)
        return Response(serializer.data)
