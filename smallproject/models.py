from django.db import models


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    department_image = models.ImageField()
    fees = models.IntegerField(default=0)
    event = models.OneToOneField('Event', on_delete=models.SET_NULL, verbose_name='Events', blank=True, null=True)
    privilege_users = models.ManyToManyField('User', related_name='department_privilege')

    def __str__(self):
        return self.name

    class Meta:
        default_related_name = 'department'


class Language(models.Model):

    id = models.AutoField(primary_key=True)
    language_name = models.CharField(max_length=20)

    def __str__(self):
        return self.language_name

    class Meta:
        default_related_name = 'language'


class User(models.Model):

    class GenderChoices(models.TextChoices):
        FEMALE = "FEMALE", "FEMALE"
        MALE = "MALE", "MALE"

    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices, default=None)
    phone_number = models.CharField(max_length=20)
    languages = models.ManyToManyField('Language', related_name='users')
    advanced_status = models.BooleanField(default=False)
    departments = models.ManyToManyField('Department', related_name='users', )

    class Meta:
        default_related_name = 'user'

    def __str__(self):
        return self.full_name


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    events_name = models.CharField(max_length=50)
    events_date_start = models.DateTimeField()
    events_date_end = models.DateTimeField()

    class Meta:
        default_related_name = 'user'

    def __str__(self):
        return self.events_name





