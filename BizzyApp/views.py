from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import DiscountEntryForm
from shopifyDiscCreate import begin

created = False
coupCode = "NO CODE"

def entry(request):
    if request.method == "POST":
        form = DiscountEntryForm(request.POST)
        # Copy since immutable
        form.data = form.data.copy()
        cT = form.data["couponType"]
        cV = form.data["couponVal"]
        mA = form.data["minimumAmt"]
        form.data["couponCode"] = begin(cT, cV, mA)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            global created
            created = True
            global coupCode
            coupCode = form.data["couponCode"]
            return redirect("code")
        else:
            return redirect("code")
    else:
        form = DiscountEntryForm()
    return render(request, "BizzyApp/entry.html", {'form': form})
    

def code(request):
    response = """<form><fieldset><legend>Coupon Code</legend>
                  %s</fieldset></form><br>Coupon valid at
                  https://billiams-bazaar.myshopify.com/"""
    if (created):
        global created
        created = False
        return HttpResponse(response % coupCode)
    else:
        return HttpResponse(response % "Coupon does not exist!")
