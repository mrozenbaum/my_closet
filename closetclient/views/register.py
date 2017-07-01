from django.shortcuts import render

# import forms and models from this app
from closetclient.forms import UserForm, ProfileForm
from closetclient.views import login_user

def register(request):
    """
    purpose: Handles the creation of a new user for authentication
    author: miriam rozenbaum
    args: request -- The full HTTP request object
    returns: render of a registration from or invocation of django's login() method
    """

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()   

            user.profile.profile_name = profile_form.cleaned_data['profile_name'] 
            user.profile.birth_date = profile_form.cleaned_data['birth_date']
            user.profile.zip_code = profile_form.cleaned_data['zip_code']
            user.profile.bio = profile_form.cleaned_data['bio']
            user.save()            

            # Update our variable to tell the template registration was successful.
            registered = True        

        return login_user(request)

    elif request.method == 'GET':
        user_form = UserForm()
        profile_form = ProfileForm()
        template_name = 'register.html'
        return render(request, template_name, {
            'user_form': user_form,
            'profile_form': profile_form})