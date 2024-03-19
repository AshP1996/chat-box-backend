


import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone

# Define language choices
LANGUAGE_CHOICES = [
    ('af', 'Afrikaans'),
    ('ar', 'Arabic'),
    ('ar-dz', 'Algerian Arabic'),
    ('ast', 'Asturian'),
    ('az', 'Azerbaijani'),
    ('bg', 'Bulgarian'),
    ('be', 'Belarusian'),
    ('bn', 'Bengali'),
    ('br', 'Breton'),
    ('bs', 'Bosnian'),
    ('ca', 'Catalan'),
    ('ckb', 'Central Kurdish (Sorani)'),
    ('cs', 'Czech'),
    ('cy', 'Welsh'),
    ('da', 'Danish'),
    ('de', 'German'),
    ('dsb', 'Lower Sorbian'),
    ('el', 'Greek'),
    ('en', 'English'),
    ('en-au', 'Australian English'),
    ('en-gb', 'British English'),
    ('eo', 'Esperanto'),
    ('es', 'Spanish'),
    ('es-ar', 'Argentinian Spanish'),
    ('es-co', 'Colombian Spanish'),
    ('es-mx', 'Mexican Spanish'),
    ('es-ni', 'Nicaraguan Spanish'),
    ('es-ve', 'Venezuelan Spanish'),
    ('et', 'Estonian'),
    ('eu', 'Basque'),
    ('fa', 'Persian'),
    ('fi', 'Finnish'),
    ('fr', 'French'),
    ('fy', 'Frisian'),
    ('ga', 'Irish'),
    ('gd', 'Scottish Gaelic'),
    ('gl', 'Galician'),
    ('he', 'Hebrew'),
    ('hi', 'Hindi'),
    ('hr', 'Croatian'),
    ('hsb', 'Upper Sorbian'),
    ('hu', 'Hungarian'),
    ('hy', 'Armenian'),
    ('ia', 'Interlingua'),
    ('id', 'Indonesian'),
    ('ig', 'Igbo'),
    ('io', 'Ido'),
    ('is', 'Icelandic'),
    ('it', 'Italian'),
    ('ja', 'Japanese'),
    ('ka', 'Georgian'),
    ('kab', 'Kabyle'),
    ('kk', 'Kazakh'),
    ('km', 'Khmer'),
    ('kn', 'Kannada'),
    ('ko', 'Korean'),
    ('ky', 'Kyrgyz'),
    ('lb', 'Luxembourgish'),
    ('lt', 'Lithuanian'),
    ('lv', 'Latvian'),
    ('mk', 'Macedonian'),
    ('ml', 'Malayalam'),
    ('mn', 'Mongolian'),
    ('mr', 'Marathi'),
    ('ms', 'Malay'),
    ('my', 'Burmese'),
    ('nb', 'Norwegian Bokmål'),
    ('ne', 'Nepali'),
    ('nl', 'Dutch'),
    ('nn', 'Norwegian Nynorsk'),
    ('os', 'Ossetic'),
    ('pa', 'Punjabi'),
    ('pl', 'Polish'),
    ('pt', 'Portuguese'),
    ('pt-br', 'Brazilian Portuguese'),
    ('ro', 'Romanian'),
    ('ru', 'Russian'),
    ('sk', 'Slovak'),
    ('sl', 'Slovenian'),
    ('sq', 'Albanian'),
    ('sr', 'Serbian'),
    ('sr-latn', 'Serbian Latin'),
    ('sv', 'Swedish'),
    ('sw', 'Swahili'),
    ('ta', 'Tamil'),
    ('te', 'Telugu'),
    ('tg', 'Tajik'),
    ('th', 'Thai'),
    ('tk', 'Turkmen'),
    ('tr', 'Turkish'),
    ('tt', 'Tatar'),
    ('udm', 'Udmurt'),
    ('ug', 'Uyghur'),
    ('uk', 'Ukrainian'),
    ('ur', 'Urdu'),
    ('uz', 'Uzbek'),
    ('vi', 'Vietnamese'),
    ('zh-hans', 'Simplified Chinese'),
    ('zh-hant', 'Traditional Chinese')
]

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a new user with the given email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a new superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='en')  # Add language field
    # Define other fields as needed

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.id

