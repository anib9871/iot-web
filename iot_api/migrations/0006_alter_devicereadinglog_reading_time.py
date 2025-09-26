# iot_api/migrations/0006_alter_devicereadinglog_reading_time.py

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('iot_api', '0005_alter_devicereadinglog_reading_date_and_more'),
    ]

    operations = [
        # Step 1: Django ko field type ka update batao
        migrations.AlterField(
            model_name='devicereadinglog',
            name='READING_TIME',
            field=models.TimeField(),
        ),
        # Step 2: PostgreSQL me integer -> time conversion
        migrations.RunSQL(
            """
            ALTER TABLE iot_api_devicereadinglog
            ALTER COLUMN "READING_TIME" TYPE time
            USING make_time(
                "READING_TIME" / 10000,
                ("READING_TIME" / 100) % 100,
                "READING_TIME" % 100
            );
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
