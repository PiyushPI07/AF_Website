from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db.models.signals import post_delete
from django.dispatch import receiver
import datetime

class MyAccountManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, username, password = None):
        if not email:
            raise ValueError('Users must have an mail id')
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
        )
    
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
            

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(verbose_name='name', max_length=50, null=False)
    date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_recruitment_applicant = models.BooleanField(default=False)

    objects = MyAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return self.email
    
    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

class RecruitmentApplicant(models.Model):
    batch_choices = [
        ('firstYear', 'First Year' ),
        ('secondYear', 'Second Year' ),
        ('thirdYear', 'Third Year' ),
        ('fourthYear', 'Final Year' ),
        ('PostGraduate', 'PG' ),
    ]
    branchChoices = [
        ('CSE', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('ECE', 'Electronics and Communication'),
        ('EEE', 'Electronics and Electrical'),
        ('MECH', 'Mechanical'),
        ('CV', 'Civil'),
        ('CH', 'Chemical'),
        ('META', 'Metallurgy and Materials'),
    ]
    statusChoices = [
        ('written', 'Written Test'),
        ('interview', 'Selected for Interview'),
        ('selected', 'Selected')
    ]
    applicant = models.ForeignKey(to=Account, on_delete=models.CASCADE, related_name='applicant')
    application_id = models.IntegerField(verbose_name='application id', primary_key=True)
    name = models.CharField(verbose_name='name', max_length=50, null=False)
    roll_number = models.CharField(max_length=10, unique=True)
    batch = models.CharField(verbose_name='Batch', max_length=20, choices=batch_choices)
    branch = models.CharField(verbose_name='Branch', max_length=20, choices=branchChoices)
    status = models.CharField(verbose_name='Status', max_length=20, choices=statusChoices, default='written')
    phone_regex = RegexValidator(regex=r'^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$', message="Incorrect phone number format")
    phoneNumber = models.CharField(verbose_name='Phone Number', validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    year = datetime.datetime.now().year
    recruitmentYear = models.CharField(default=year, max_length=4)

    #overriden delet for simultenous deletion of reference account
    def delete(self, *args, **kwargs):
        self.account.delete()
        return super(self.__class__, self).delete(*args, **kwargs)

#To delete the acccount when recruimentapplication in deleted post method for admin panel deletion
@receiver(post_delete, sender=RecruitmentApplicant)
def post_delete_user(sender, instance, *args, **kwargs):
    if instance.applicant: 
        instance.applicant.delete()