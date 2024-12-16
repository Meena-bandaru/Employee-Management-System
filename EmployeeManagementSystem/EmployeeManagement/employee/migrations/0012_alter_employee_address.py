from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0011_add_email_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.TextField(blank=True, default='', max_length=250),
        ),
    ]
