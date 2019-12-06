from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User

from .forms import PaymentForm
from .payment_core import make_transaction


def make_payment(request):
    current_user: User = request.user
    if not current_user.is_authenticated:
        return HttpResponseRedirect(redirect_to='/login')
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PaymentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            amount = form.cleaned_data['amount']
            try:
                receiver = form.cleaned_data['receiver']
                receiver: User = User.objects.get_by_natural_key(receiver)
            except Exception as e:
                print(e)
                return render(request, 'payment_error.html')
            # process the data in form.cleaned_data as required
            if make_transaction(str(current_user.username), str(receiver), int(amount)):
                return render(request, 'payment_ok.html', {'form_amount': str(amount), 'form_receiver': str(receiver)})
    return render(request, 'payment_error.html')
