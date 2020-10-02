# Generated by Django 3.1.1 on 2020-10-02 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='rollno',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='Warden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4096)),
                ('warden_id', models.CharField(max_length=20)),
                ('mess', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mess.mess')),
            ],
        ),
    ]
