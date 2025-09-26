from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('iot_api', '0005_previous_migration'),
    ]

    operations = [
        migrations.RunSQL(
            """
            ALTER TABLE iot_api_devicereadinglog
            ALTER COLUMN "READING_TIME" TYPE time
            USING (make_interval(hours => "READING_TIME"/10000, minutes => ("READING_TIME"/100)%100, seconds => "READING_TIME"%100));
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
