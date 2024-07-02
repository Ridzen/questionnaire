from django.db import models

# Create your models here.


class Questionnaire(models.Model):
    name = models.CharField(
        max_length=255, null=False, blank=False, help_text='name'
    )
    phone = models.CharField(
        max_length=20, null=False, blank=False, help_text='Phone number'
    )
    zip = models.IntegerField(
        null=False, blank=False, help_text='Zip'
    )
    time = models.CharField(
        max_length=10, null=True, blank=True, help_text='Time'
    )
    message = models.TextField(
        null=True, blank=True, help_text='Message'
    )

    class Meta:
        verbose_name = 'Questionnaire'
        verbose_name_plural = 'Questionnaires'