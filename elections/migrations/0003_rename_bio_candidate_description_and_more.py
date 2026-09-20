from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('elections', '0002_alter_vote_voter'),
        ]
    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='bio',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='election',
        ),
        migrations.AddField(
            model_name='candidate',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='candidates/'),
        ),
        ]
