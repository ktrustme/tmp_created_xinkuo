Homework 3 Feedback
==================

Commit graded: 14d103d182a7e63de1cfc2156601af39e145b18d


### Incremental development using Git (10/10)

### Fulfilling the grumblr specification (18/20)

* -2, Posts should link to the profile of the user who authored it.  On other peoples profile pages, the posts link to your own profile.

### Proper input validation (16/20)

* -4 Your application does not check for missing request parameters.  Line 28 of views.py accesses `request.POST['grumble_text']` without checking existence.  Line 79 of views.py is also an unsafe access, but no points off since this bug was in our authentication_example.

### Request routing and configuration in Django (10/10)

### Appropriate use of web application technologies in the Django framework (39/40)

* -1, For reversing grumbles in memory instead of using ORM.  The code:

`
grumbles = grumble.objects.all()
grumbles.reverse()
`

Should be `grumble.objects.all().order_by("-time")`.  Using the ORM asks the database to sort, which is more performant.
		

### Design

### Additional Information

---

#### Total score (93/100)

---

Graded by: Brian Bergeron (bbergero@andrew.cmu.edu)

To view this file with formatting, visit the following page: https://github.com/CMU-Web-Application-Development/xkuo/blob/master/grades/homework3.md
