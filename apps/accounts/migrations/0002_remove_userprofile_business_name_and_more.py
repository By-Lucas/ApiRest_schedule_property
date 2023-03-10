# Generated by Django 4.1.5 on 2023-01-05 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='business_name',
        ),
        migrations.AlterField(
            model_name='user',
            name='permission',
            field=models.CharField(blank=True, choices=[('adm_imob_access', 'Administrador Imob'), ('user_imob_access', 'Usuário Imob')], max_length=100, null=True, verbose_name='Nivel de permissão do usuário'),
        ),
    ]
