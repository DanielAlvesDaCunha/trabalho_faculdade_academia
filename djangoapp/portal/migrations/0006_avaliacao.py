# Generated by Django 5.1.3 on 2024-11-25 22:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_alter_agendamento_aluno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_horario', models.DateTimeField()),
                ('disponivel', models.BooleanField(default=True)),
                ('peso', models.FloatField(blank=True, null=True)),
                ('altura', models.FloatField(blank=True, null=True)),
                ('aptidao', models.TextField(blank=True, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('agendamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to='portal.agendamento')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]