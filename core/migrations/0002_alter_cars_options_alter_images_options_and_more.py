# Generated by Django 4.0.5 on 2022-06-20 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cars',
            options={'ordering': ['-created_at'], 'verbose_name': 'машина', 'verbose_name_plural': 'машины'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'ordering': ['-created_at'], 'verbose_name': 'фотография', 'verbose_name_plural': 'фотографий'},
        ),
        migrations.AlterField(
            model_name='cars',
            name='description',
            field=models.CharField(help_text='Максимальная количество символов 255', max_length=1200, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='images',
            field=models.ManyToManyField(related_name='cars', to='core.images', verbose_name='фотографий'),
        ),
    ]