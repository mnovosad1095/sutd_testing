# Generated by Django 2.1.7 on 2019-02-20 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MatchQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(default=None, max_length=50)),
                ('choice', models.CharField(default=None, max_length=50)),
                ('points', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='MatchTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=30)),
                ('match_task_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MultiChoiceQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=30)),
                ('question_name', models.CharField(max_length=20)),
                ('question', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('test_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TFStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.CharField(max_length=50)),
                ('True?', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TFTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='tfstatement',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tf_stats', to='studying.TFTask'),
        ),
        migrations.AddField(
            model_name='multichoicequestion',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multis', to='studying.Testing'),
        ),
        migrations.AddField(
            model_name='matchtask',
            name='test',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='studying.Testing'),
        ),
        migrations.AddField(
            model_name='matchquestion',
            name='match_task',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='match_options', to='studying.MatchTask'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='multis_choices', to='studying.MultiChoiceQuestion'),
        ),
    ]
