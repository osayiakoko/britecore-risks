# Generated by Django 3.2 on 2021-04-24 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RiskType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='RiskTypeField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=150)),
                ('field_type', models.CharField(choices=[('text', 'Text'), ('number', 'Number'), ('date', 'Date'), ('enum', 'Enum')], max_length=50)),
                ('risk_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risk_type_fields', to='risk.risktype')),
            ],
            options={
                'ordering': ('pk',),
                'unique_together': {('risk_type', 'field_name', 'field_type')},
            },
        ),
        migrations.CreateModel(
            name='TextFieldValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('risk_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='textfieldvalues', to='risk.risktype')),
                ('risk_type_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='textfieldvalues', to='risk.risktypefield')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NumberFieldValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('risk_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='numberfieldvalues', to='risk.risktype')),
                ('risk_type_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='numberfieldvalues', to='risk.risktypefield')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EnumFieldValueChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=150)),
                ('risk_enum_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='risk.risktypefield')),
            ],
        ),
        migrations.CreateModel(
            name='DateFieldValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DateField()),
                ('risk_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='datefieldvalues', to='risk.risktype')),
                ('risk_type_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datefieldvalues', to='risk.risktypefield')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EnumFieldValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=150)),
                ('risk_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enumfieldvalues', to='risk.risktype')),
                ('risk_type_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enumfieldvalues', to='risk.risktypefield')),
            ],
            options={
                'unique_together': {('risk_type_field', 'value')},
            },
        ),
    ]
