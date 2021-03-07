# Generated by Django 3.1.5 on 2021-03-07 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_add_person_photo_rel'),
        ('movies', '0007_movie_posters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.person'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='actor_in_movies', through='movies.Actor', to='person.Person'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='composers',
            field=models.ManyToManyField(related_name='composed_movies', to='person.Person'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(related_name='directed_movies', to='person.Person'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='editors',
            field=models.ManyToManyField(related_name='edited_movies', to='person.Person'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='operators',
            field=models.ManyToManyField(related_name='operated_movies', to='person.Person'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='producers',
            field=models.ManyToManyField(related_name='produced_movies', to='person.Person'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='production_designers',
            field=models.ManyToManyField(related_name='production_designed_movies', to='person.Person'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='writers',
            field=models.ManyToManyField(related_name='wrote_movies', to='person.Person'),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
