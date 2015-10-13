from django import forms

from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length = 20)
    password1 = forms.CharField(max_length = 200, 
                                label='Password', 
                                widget = forms.PasswordInput())
    password2 = forms.CharField(max_length = 200, 
                                label='Confirm password',  
                                widget = forms.PasswordInput())


    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        # Calls our parent (forms.Form) .clean function, gets a dictionary
        # of cleaned data as a result
        cleaned_data = super(RegistrationForm, self).clean()

        # Confirms that the two password fields match
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords did not match.")

        # Generally return the cleaned data we got from our parent.
        return cleaned_data

    # Customizes form validation for the username field.
    def clean_username(self):
        # Confirms that the username is not already present in the
        # User model database.
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact=username):
            raise forms.ValidationError("Username is already taken.")

        # Generally return the cleaned data we got from the cleaned_data
        # dictionary
        return username

class CreateStudentForm:
    andrew_id = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    
    def clean(self):
        cleaned_data = super(CreateStudentForm, self).clean()
        andrew_id = cleaned_data.get('andrew_id')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if !andrew_id || !first_name || !last_name:
            raise forms.ValidationError("Input Can't Be Empty!")
        return cleaned_data

    def clean_andrew_id(self):
        # Confirms that the username is not already present in the
        # User model database.
        andrew_id = self.cleaned_data.get('andrew_id')
        if Student.objects.filter(andrew_id__exact=andrew_id):
            raise forms.ValidationError("Andrew id is already taken.")
                                                                         
        # Generally return the cleaned data we got from the cleaned_data
        # dictionary
        return andrew_id 

class CreateCourseForm:
    course_number = forms.CharField(max_length=20)
    course_name = formes.CharField(max_length=100)
    
    def clean(self):
        cleaned_data = super(CreateCourseForm, self).clean()
        course_number = cleaned_data.get('course_number')
        course_name = cleaned_data.get('course_name')
        
        if !course_number || !course_name:
            raise forms.ValidationErrof("Input Can't Be Empty!")
        return cleaned_data

    def clean_course_number(self):
        course_number = self.cleaned_data.get("course_number")
        if Course.filter





'''
<form action="/sio/create-student" method="post">
    Andrew ID:  <input type="text" name="andrew_id"><br>
    First name: <input type="text" name="first_name"><br>
    Last name:  <input type="text" name="last_name"><br>
                {% csrf_token %}
                <input type="submit" value="Submit">
</form>

<hr>
<p>Create a course:</p>
<form action="/sio/create-course" method="post">
    Course #:    <input type="text" name="course_number"><br>
    Course name: <input type="text" name="course_name"><br>
    Instructor:  <input type="text" name="instructor"><br>
                 {% csrf_token %}
                 <input type="submit" value="Submit">
</form>

<hr>
<p>Register a student for a course:</p>
<form action="/sio/register-student" method="post">
    Andrew ID: <input type="text" name="andrew_id"><br>
    Course #:  <input type="text" name="course_number"><br>
               {% csrf_token %}
               <input type="submit" value="Submit">
</form>
'''
