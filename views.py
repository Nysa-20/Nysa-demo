from django.shortcuts import render, redirect
from .forms import SubjectForm, FileUploadForm
from .models import Subject

# View to handle subject selection
def subject_input(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject_name = form.cleaned_data['subject']
            
            # Get or create subject, but let's log the results
            subject, created = Subject.objects.get_or_create(name=subject_name)
            
            print(f"Subject created: {created}, Subject: {subject}")  # Debugging output
            
            # Redirect to the file upload page for the selected subject
            return redirect('file_upload', subject_id=subject.id)
    else:
        form = SubjectForm()

    return render(request, 'subjects/subject_input.html', {'form': form})

# View to handle file uploads for the selected subject
def file_upload(request, subject_id):
    try:
        subject = Subject.objects.get(id=subject_id)
    except Subject.DoesNotExist:
        return redirect('subject_input')  # Redirect if subject doesn't exist

    if request.method == 'POST' and request.FILES:
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.subject = subject  # Associate the file with the selected subject
            file.save()
            # Reload the page after upload
            return redirect('file_upload', subject_id=subject.id)
    else:
        form = FileUploadForm()

    files = subject.files.all()  # Retrieve all files associated with the subject
    return render(request, 'subjects/file_upload.html', {'form': form, 'subject': subject, 'files': files})
