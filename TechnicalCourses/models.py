from django.db import models
#To create a database allcourses in which we have coursename and instructor name
class Allcourses(models.Model):
    coursename = models.CharField(max_length=200)
    insname = models.CharField(max_length = 100)

    def __str__(self):
        return self.coursename
#To create a class with details of the database with the foreign key method such that if any course is deletd 
#details will also be get deleted with it.
class details(models.Model):
    course = models.ForeignKey(Allcourses, on_delete = models.CASCADE)
    sp = models.CharField(max_length = 500)
    il = models.CharField(max_length = 500)
    def __str__(self):
        return self.sp


#Now to perform on the database and to use in on command prompt these are some commands we will use.

#python manage.py makemigrations appname.
#python manage.py sqlmigrate appname idgenerated 
#python manage.py migrate
#python manage.py shell

# ''' Now to access the database on the shell we will perform
# from TechnicalCourses(appname).models import Allcourses,details(classes name)

# Now if we want to see what is there in particular dataset we will do
# Allcourses.objects.all()
# Now to add in to dataset we will peform
# a = Allcourses(coursename="Python",insname = "XYZ")
# a.save (Perform save after moderating in the datatset)

# now we can add as many as data by declaring different varibales and doing the operations.
#  pk is the primary key and we can display the primary key by using a.id or a.pk.
# to filter the data or to get the particular data we can use
# Allcourses.objects.filter(id=1)
# Allcourses.objects.get(id=1)
# 
# 
# We can create a superuser for our app by the command
# python manage.py createsuperuser
# 
# 
# Now if we want to use in the website that you have to created we have to import it in admin section
# rom .models import Allcourses
#admin.site.register(Allcourses)
#  write the above commands in admin.py file and boom we will be able to use it..'''



