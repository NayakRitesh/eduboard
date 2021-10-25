# Generated by Django 3.2.8 on 2021-10-15 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formdata',
            name='fieldData',
        ),
        migrations.AddField(
            model_name='formdata',
            name='AlternateDelimeter',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='formdata',
            name='Answer',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='formdata',
            name='AnswerCheckType',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='formdata',
            name='AnswerType',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='formdata',
            name='BoxDelimeter',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='formdata',
            name='Hint',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='formdata',
            name='ImageData',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='formdata',
            name='NumberOfAnswerBox',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='formdata',
            name='Question',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='formdata',
            name='RangeHigherLimit',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formdata',
            name='RangeLowerLimit',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formdata',
            name='SecondaryAnswer',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='formdata',
            name='SecondaryAnswerType',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='formdata',
            name='Solution',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
