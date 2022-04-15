# Generated by Django 4.0.3 on 2022-03-18 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=400)),
                ('autor', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.perfil')),
                ('publicacion', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.publicacion')),
            ],
        ),
    ]
