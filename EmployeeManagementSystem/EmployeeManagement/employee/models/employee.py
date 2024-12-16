from django.db import models
from django.utils.translation import gettext_lazy as _


class Employee(models.Model):
    class GenderChoices(models.TextChoices):
        male = "M", _("Male")
        female = "F", _("Female")
        others = "O", _("Others")

    emp_id = models.BigAutoField(primary_key=True)
    forename = models.CharField(max_length=150, blank=True, null=False,
                                default="")
    surname = models.CharField(max_length=100, blank=True, null=False, default="")
    title = models.CharField(max_length=60, blank=True, null=False, default="")
    gender = models.CharField(max_length=8, choices=GenderChoices.choices,
                              default=GenderChoices.male)
    age = models.IntegerField(null=True)
    # date_of_birth = models.DateField()
    #
    # address = models.TextField(max_length=250, blank=True, default="")
    #email = models.EmailField(blank=True, null=False, default="")

    def __str__(self):
        return self.surname
