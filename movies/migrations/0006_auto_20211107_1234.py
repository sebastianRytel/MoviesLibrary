# Generated by Django 3.2.8 on 2021-11-07 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20211104_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='Location',
            field=models.CharField(choices=[('HARD DRIVE', 'harddrive'), ('CDA', 'cda'), ('NETFLIX', '<img src="https://img.icons8.com/ios/50/000000/netflix--v1.png"/>')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='movies',
            name='Rating',
            field=models.IntegerField(choices=[(5, '<img src="/media/osc_5_ico.jpg"/>'), (4, '<img src="/media/osc_4_ico.jpg"/>'), (3, 'Average'), (2, 'Poor'), (1, '<img src="/media/osc_1_ico.jpg"/>'), (0, 'Piece of shit')], default=''),
        ),
    ]
