import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL),]
    operations = [migrations.CreateModel(name='Election',fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),],),
                migrations.CreateModel(name='Candidate',fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.election')),
                ],
                ),
                migrations.CreateModel(name='Vote',fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.candidate')),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.election')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ],
                options={
                    'unique_together': {('voter', 'election')},
                    },
                    ),
                    ]
