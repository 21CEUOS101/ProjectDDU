# Generated by Django 4.1.5 on 2023-02-20 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=50)),
                ('reciverId', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='userId',
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='reciverId',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='MobileInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.IntegerField(max_length=10)),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_main.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='LoginInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=8)),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_main.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='GroupInfo',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=50)),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_main.userinfo')),
            ],
        ),
    ]
