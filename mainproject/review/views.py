from django.shortcuts import render

# Create your views here.
def add_review(request):
    if request.method == 'POST':
        ratting = request.POST['ratting']
        dis = request.POST['dis']

        review = reviews(ratting=ratting,discription=dis)
        review.save()
        return redirect('/')
    
    return render(request,'add_review.html')
