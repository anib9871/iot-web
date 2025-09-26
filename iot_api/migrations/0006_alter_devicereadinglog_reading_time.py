from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('iot_api', '0005_alter_devicereadinglog_reading_date_and_more'),
    ]

    operations = [
        # Step 1: Add temporary column as time
        migrations.RunSQL(
            """
            ALTER TABLE iot_api_devicereadinglog
            ADD COLUMN temp_reading_time time;
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
        # Step 2: Copy & convert data
        migrations.RunSQL(
            """
            UPDATE iot_api_devicereadinglog
            SET temp_reading_time = make_time(
                "READING_TIME" / 10000,
                ("READING_TIME" / 100) % 100,
                "READING_TIME" % 100
            );
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
        # Step 3: Drop old column
        migrations.RunSQL(
            """
            ALTER TABLE iot_api_devicereadinglog
            DROP COLUMN "READING_TIME";
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
        # Step 4: Rename temp column
        migrations.RunSQL(
            """
            ALTER TABLE iot_api_devicereadinglog
            RENAME COLUMN temp_reading_time TO "READING_TIME";
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
        # Step 5: Update Django model
        migrations.AlterField(
            model_name='devicereadinglog',
            name='READING_TIME',
            field=models.TimeField(),
        ),
    ]
