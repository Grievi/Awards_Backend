# Generated by Django 3.2.8 on 2021-10-26 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_alter_review_project_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='project_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='proj_performance', serialize=False, to='backend.project'),
        ),
    ]
