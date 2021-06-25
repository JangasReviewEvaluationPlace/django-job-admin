# Generated by Django 3.2.4 on 2021-06-24 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text="If it's blank it will get an auto created string.", max_length=40, unique=True)),
                ('description', models.TextField(blank=True, help_text="The description does not have any effect for the job execution. It's just a help for understanding the job.")),
                ('configs', models.JSONField()),
                ('frequency', models.IntegerField(default=1440, help_text='In which time intervalls should the job be executed?\nTime in Minutes.')),
                ('is_one_time_job', models.BooleanField(default=False, help_text='If True job will be just executed once and then deleted.\nIf False job will be executed in given frequency.')),
                ('last_execution', models.DateTimeField(auto_now=True)),
                ('next_execution', models.DateTimeField(blank=True, editable=False, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('-last_execution',),
            },
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobExecutionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(editable=False, max_length=40)),
                ('description', models.TextField(editable=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='execution_logs', to='job.job')),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='jobs', to='job.jobtype'),
        ),
    ]
