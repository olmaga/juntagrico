# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 11:13
from __future__ import unicode_literals

from django.db import migrations

def forward(apps, schema_editor):
    AbstractJobType = apps.get_model("my_ortoloco", "AbstractJobType")
    JobType = apps.get_model("my_ortoloco", "JobType")
    OneTimeJob = apps.get_model("my_ortoloco", "OneTimeJob")
    print len(JobType.objects.all())
    for jt in JobType.objects.all():
        ajt = AbstractJobType.objects.filter(id = jt.abstractjobtype_ptr_id)[0]
        print ajt.name
        jt.bereicht = ajt.bereich
        jt.namet =ajt.name
        jt.displayed_namet =ajt.displayed_name
        jt.descriptiont =ajt.description
        jt.durationt =ajt.duration
        jt.locationt =ajt.location
        jt.id = jt.abstractjobtype_ptr_id
        jt.save()
    print len(OneTimeJob.objects.all())
    for jt in OneTimeJob.objects.all():
        ajt = AbstractJobType.objects.filter(id = jt.abstractjobtype_ptr_id)[0]
        print ajt.name
        jt.bereichp = ajt.bereich
        jt.namep =ajt.name
        jt.displayed_namep =ajt.displayed_name
        jt.descriptionp =ajt.description
        jt.durationp =ajt.duration
        jt.locationp =ajt.location
        jt.save()
        
def backwards(apps, schema_editor):
    AbstractJobType = apps.get_model("my_ortoloco", "AbstractJobType")
    JobType = apps.get_model("my_ortoloco", "JobType")
    OneTimeJob = apps.get_model("my_ortoloco", "OneTimeJob")
    CT = apps.get_model("contenttypes" "contenttype") 
    jtid = CT.objects.filter(model = 'jobtype')[0].id
    otjid = CT.objects.filter(model = 'onetimejob')[0].id
    for jt in JobType.objects.all():
        ajt = AbstractJobType()
        ajt.name =jt.namet
        ajt.displayed_name =jt.displayed_namet
        ajt.description =jt.descriptiont
        ajt.duration =jt.durationt
        ajt.location =jt.locationt
        ajt.polymorphic_ctype = jtid
        ajt.save()
        jt.abstractjobtype_ptr=ajt.id
        jt.save()
    for jt in OneTimeJob.objects.all():
        ajt = AbstractJobType()
        ajt.name =jt.namep
        ajt.displayed_name =jt.displayed_namep
        ajt.description =jt.descriptionp
        ajt.duration =jt.durationp
        ajt.location =jt.locationp
        ajt.polymorphic_ctype = otjid
        ajt.save()
        jt.abstractjobtype_ptr=ajt.id
        jt.save()

class Migration(migrations.Migration):

    dependencies = [
        ('my_ortoloco', '0002_auto_20160119_0923'),
    ]

    operations = [
        migrations.RunPython(forward, backwards),
    ]