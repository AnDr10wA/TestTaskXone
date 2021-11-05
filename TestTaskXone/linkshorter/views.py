from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
import uuid
from .form import LinkForm
from .models import Link
from django.contrib.auth.decorators import login_required

domain = 'http://127.0.0.1:8000/'


def generate_token():
    uid = str(uuid.uuid4())[:5]
    return uid


def main_page(request):

    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            input_link = form.cleaned_data['input_link']
            output_link = generate_token()

            if request.user.is_authenticated:
                user = request.user
            else:
                user = None
            final_link = Link(input_link = input_link, output_link=output_link, user = user)
            final_link.save()
            new_form = LinkForm(initial= {'input_link':domain+output_link})
            return render(request, 'main_page.html', {'form': new_form})
    else:

        form = LinkForm()
        return render(request, 'main_page.html', {'form':form})


def folow_link(request, token):
    input_link = get_object_or_404(Link, output_link=token)

    return HttpResponseRedirect(input_link.input_link)

@login_required(login_url = 'login')
def user_links(request):
    user = request.user
    userslink = Link.objects.filter(user= user)
    userslink = userslink[::-1]


    return render(request, 'usersliks.html', {'liks':userslink, 'domain': domain})




