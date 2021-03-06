# Generated by Django 2.1.5 on 2020-03-23 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('letsplant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officeName', models.CharField(max_length=20)),
                ('officeCode', models.CharField(max_length=20)),
                ('attribution', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subID', models.CharField(max_length=20)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('officeCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='letsplant.Office')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membershipStart', models.DateField()),
                ('membershipEnd', models.DateField()),
                ('nativeCountry', models.CharField(max_length=20)),
                ('citizenship', models.CharField(max_length=20)),
                ('isdelegate', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceCode', models.CharField(max_length=20)),
                ('serviceName', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=144)),
                ('premium', models.CharField(max_length=20)),
                ('allocation', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subID', models.CharField(max_length=20)),
                ('subRequestDate', models.DateField()),
                ('subStartDate', models.DateField()),
                ('subEndDate', models.DateField()),
                ('cancelationReason', models.CharField(max_length=50)),
                ('subType', models.CharField(max_length=20)),
                ('userName', models.CharField(max_length=20)),
                ('beneficiaryID', models.CharField(max_length=20)),
                ('serviceCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='letsplant.Service')),
            ],
        ),
        migrations.AlterField(
            model_name='organization',
            name='dateJoined',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='organizationmember',
            name='orgCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='letsplant.Organization'),
        ),
        migrations.AddField(
            model_name='organizationmember',
            name='subID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='letsplant.Subscriber'),
        ),
    ]
