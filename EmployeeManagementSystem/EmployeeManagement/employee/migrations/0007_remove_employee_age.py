from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_alter_forename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='age',
        ),
    ]
