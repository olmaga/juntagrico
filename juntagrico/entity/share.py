# encoding: utf-8

from django.db import models

from juntagrico.mailer import *
from juntagrico.entity.billing import *
from juntagrico.util.bills import *
from juntagrico.config import Config


class Share(Billable):
    member = models.ForeignKey("Member", null=True, blank=True, on_delete=models.SET_NULL)
    paid_date = models.DateField("Bezahlt am", null=True, blank=True)
    issue_date = models.DateField("Ausgestellt am", null=True, blank=True)
    booking_date = models.DateField("Eingebucht am", null=True, blank=True)
    cancelled_date = models.DateField("Gekündigt am", null=True, blank=True)
    termination_date = models.DateField("Gekündigt auf", null=True, blank=True)
    payback_date = models.DateField("Zurückbezahlt am", null=True, blank=True)
    number = models.IntegerField("Anteilschein Nummer", null=True, blank=True)
    notes = models.TextField("Notizen", max_length=1000, default="", blank=True)
    
    @classmethod
    def create(cls, sender, instance, created, **kwds):
        if created and Config.billing():
            bill_share(instance)
    def __str__(self):
        return "Anteilschein #%s" % self.id

    class Meta:
        verbose_name = "Anteilschein"
        verbose_name_plural = "Anteilscheine"