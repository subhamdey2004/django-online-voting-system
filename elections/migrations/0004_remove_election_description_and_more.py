import django.db.models.deletion
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [('elections', '0003_rename_bio_candidate_description_and_more'),]
operations = [
    migrations.RemoveField(
        model_name='election',
        name='description',
        ),
    migrations.RemoveField(
        model_name='election',
        name='is_active',
        ),
    migrations.AddField(
        model_name='candidate',
        name='election',
        field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='candidates', to='elections.election'),
        preserve_default=False,
        ),
    migrations.AlterField(
        model_name='candidate',
        name='description',
        field=models.TextField(blank=True),
        ),
        ]
