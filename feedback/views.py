from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'feedback/01-index.html')  # Redirect to a thank-you page
    else:
        form = FeedbackForm()
    return render(request, 'feedback/02-index.html', {'form': form})
