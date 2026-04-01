from django.shortcuts import render, redirect
from .etl import run_etl
from .models import CleanStudent

def upload_and_run(request):
    message = None
    
    if request.method == "POST":
        if 'csvfile' not in request.FILES:
            message = "Please select a CSV file."
        else:
            file = request.FILES['csvfile']
            
            if not file.name.endswith('.csv'):
                message = "Please upload a valid CSV file."
            else:
                with open("students.csv", "wb+") as f:
                    for chunk in file.chunks():
                        f.write(chunk)
                
                run_etl()
                return redirect("success")
    
    return render(request, "upload.html", {"message": message})

def success(request):
    students = CleanStudent.objects.all()
    count = students.count()
    return render(request, "success.html", {"students": students, "count": count})