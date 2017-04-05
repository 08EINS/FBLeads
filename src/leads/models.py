from django.db import models
from django.conf import settings

# Create your models here.


YOUNG = 'YOU'
ADULT = 'ADU'
OLD = 'OLD'
CATEGORY_CHOICES = (
    (YOUNG, 'young'),
    (ADULT, 'adult'),
    (OLD, 'old'),
)


class UserProfile(models.Model):
    MAN = 'm'
    WOMAN = 'w'
    GENDER_CHOICES = (
        (MAN, 'man'),
        (WOMAN, 'woman'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)


class Message(models.Model):
    BLOGS = 'BLO'
    INTERNATIONAL = 'INT'
    CULTURE = 'CUL'
    PANORAMA = 'PAN'
    REGION = 'REG'
    TRAVEL = 'TRA'
    SWITZERLAND = 'SWI'
    SPORTS = 'SPO'
    TECHNOLOGY = 'TEC'
    ECONOMIC = "ECO"
    KNOWLEDGE = "KNO"
    ZURICH = "ZRH"
    ZURICHHINT = "ZHI"
    COLUMN_CHOICES = (
        (BLOGS, 'blogs'),
        (INTERNATIONAL, 'international'),
        (CULTURE, 'culture'),
        (PANORAMA, 'panorama'),
        (REGION, 'region'),
        (TRAVEL, 'travel'),
        (SWITZERLAND, 'Switzerland'),
        (SPORTS, 'sports'),
        (TECHNOLOGY, 'technology'),
        (ECONOMIC, 'economic'),
        (KNOWLEDGE, 'knowledge'),
        (ZURICH, 'Zurich'),
        (ZURICHHINT, 'Zurich hints'),
    )

    title = models.CharField(max_length=255)
    text = models.TextField()
    link = models.URLField()
    column = models.CharField(max_length=3, choices=COLUMN_CHOICES)
    target_group = models.CharField(max_length=3, choices=CATEGORY_CHOICES, blank=True)
    sent_timestamp = models.DateTimeField()


class Interaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.ForeignKey(Message)
    read_timestamp = models.DateTimeField(blank=True, null=True)
    clicked_timestamp = models.DateTimeField(blank=True, null=True)
    interacted_timestamp = models.DateTimeField(blank=True, null=True)
