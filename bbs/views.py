from django.shortcuts import render,redirect

from django.views import View

from .models import Review
from .forms import ReviewForm

class IndexView(View):

    def get(self, request, *args, **kwargs):

        context             = {}
        context["reviews"]  = Review.objects.all()



        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        form    = ReviewForm(request.POST)

        if form.is_valid():
            form.save()


        return redirect("bbs:index")

index   = IndexView.as_view()
