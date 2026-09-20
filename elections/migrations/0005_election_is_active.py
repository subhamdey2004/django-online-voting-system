from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('elections', '0004_remove_election_description_and_more'),
    ]
    operations = [
        migrations.AddField(
            model_name='election',
            name='is_active',
            field=models.BooleanField(default=True),
            ),
            ]
