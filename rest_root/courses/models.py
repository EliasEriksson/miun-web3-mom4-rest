from django.db import models
from django.utils.html import strip_tags


class Course(models.Model):
    """
    This model will create a table in the databse.
    If changes to this model is made they need to be happen on the database as well,
    this is done by running `python manage.py makemigrations` and then `python manage.py migrate`

    This class can then be used as a way to make queries to the database and get objects back with the classes
    attributes / methods i.e: Course.objects.all() would get all the courses in the database.
    """
    code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=128)
    progression = models.CharField(max_length=1)
    plan = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.__class__.__name__}(code={self.code})"

    def save(self, *args, **kwargs):
        """
        saves the model object to the database

        before saving the fields are stripped from html tags to prevent XXS
        and other not so nice things.
        """
        self.code = strip_tags(self.code)
        self.name = strip_tags(self.name)
        self.progression = strip_tags(self.progression)
        self.plan = strip_tags(self.plan)
        return super().save(*args, **kwargs)
