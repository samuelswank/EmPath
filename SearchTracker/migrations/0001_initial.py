import SearchTracker.models
import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('action_group', models.CharField(choices=[('Interview Prep', 'INTERVIEW_PREP'), (
                    'Follow Up', 'FOLLOW_UP'), ('Networking', 'NETWORKING')], max_length=16)),
                ('action_type', models.CharField(max_length=32)),
                ('description', tinymce.models.HTMLField()),
                ('description_plain', models.TextField(blank=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('given_name', models.CharField(max_length=64)),
                ('surname', models.CharField(blank=True, max_length=64)),
                ('relationship', models.CharField(choices=[('Classmate', 'CLASSMATE'), ('Coworker', 'COWORKER'), ('Instructor', 'INSTRUCTOR'), ('Family', 'FAMILY'), ('教友', 'JIAO_YOU'), (
                    'Professional', 'PROFESSIONAL'), ('Workplace Superior', 'WORKPLACE_SUPERIOR')], default=SearchTracker.models.Contact.RelationshipOptions['PROFESSIONAL'], max_length=32)),
                ('primary_contact', models.CharField(max_length=200)),
                ('contact_method', models.CharField(choices=[('Email', 'EMAIL'), (
                    'Facebook', 'FACEBOOK'), ('LinkedIn', 'LINKEDIN'), ('Phone', 'PHONE')], max_length=8)),
                ('citizen_type', models.CharField(choices=[('Worker', 'WORKER'), ('Talent', 'TALENT'), ('Drone', 'DRONE'), ('Technician', 'TECHNICIAN'), ('Doctor', 'DOCTOR'), ('Librarian', 'LIBRARIAN'), (
                    'Empath', 'EMPATH'), ('Thinker', 'THINKER'), ('Transcend', 'TRANSCEND'), ('Nerve Stapled', 'NERVE_STAPLED')], default=SearchTracker.models.Contact.CitizenClassOptions['WORKER'], max_length=16)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('file', models.FileField(upload_to='')),
                ('document_type', models.CharField(choices=[('Cover Letter', 'COVER_LETTER'), ('Resume', 'RESUME'), (
                    'Other', 'OTHER')], default=SearchTracker.models.Document.DocumentTypeOptions['RESUME'], max_length=16)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('location_name', models.CharField(max_length=128)),
                ('line1', models.CharField(blank=True, max_length=32, null=True)),
                ('line2', models.CharField(blank=True, max_length=32, null=True)),
                ('city', models.CharField(blank=True, max_length=128, null=True)),
                ('country', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TemplateSnippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('content', tinymce.models.HTMLField()),
                ('snippet_type', models.CharField(choices=[('Cover Letter', 'COVER_LETTER'), (
                    'Direct Message', 'DIRECT_MESSAGE'), ('Resume', 'RESUME')], max_length=16)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=256)),
                ('contacts', models.ManyToManyField(
                    related_name='contacts_by_employer', to='SearchTracker.contact')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('precise_position_title', models.CharField(
                    blank=True, max_length=128, null=True)),
                ('requisition_number', models.CharField(
                    blank=True, max_length=64, null=True)),
                ('original_post_link', models.URLField()),
                ('description', tinymce.models.HTMLField()),
                ('description_plain', models.TextField(blank=True, editable=False)),
                ('min_payment', models.DecimalField(blank=True,
                 decimal_places=2, max_digits=8, null=True)),
                ('max_payment', models.DecimalField(blank=True,
                 decimal_places=2, max_digits=8, null=True)),
                ('payment_period', models.CharField(choices=[('Annual', 'ANNUAL'), ('Monthly', 'MONTHLY'), ('Hourly', 'HOURLY'), (
                    'Duration', 'DURATION')], default=SearchTracker.models.JobApplication.PaymentPeriodOptions['ANNUAL'], max_length=8)),
                ('date_sourced', models.DateTimeField()),
                ('date_applied', models.DateTimeField(blank=True, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Sourced', 'SOURCED'), ('Applied', 'APPLIED'), ('Interviewing', 'INTERVIEWING'), (
                    'Negotiating', 'NEGOTIATING'), ('Accepted', 'ACCEPTED')], default=SearchTracker.models.JobApplication.StatusOptions['SOURCED'], max_length=16)),
                ('notes', tinymce.models.HTMLField()),
                ('employer', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='SearchTracker.employer')),
                ('resume', models.ForeignKey(blank=True, null=True,
                 on_delete=django.db.models.deletion.CASCADE, to='SearchTracker.document')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CareerAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('action_title', models.CharField(max_length=64)),
                ('description', tinymce.models.HTMLField()),
                ('description_plain', models.TextField(blank=True, editable=False)),
                ('action_type', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='SearchTracker.actiontype')),
                ('contact', models.ForeignKey(blank=True, null=True,
                 on_delete=django.db.models.deletion.CASCADE, to='SearchTracker.contact')),
                ('job_application', models.ForeignKey(blank=True, null=True,
                 on_delete=django.db.models.deletion.CASCADE, to='SearchTracker.jobapplication')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobApplicationLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('job_application', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='SearchTracker.jobapplication')),
                ('location', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='SearchTracker.location')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='job_application_location',
            field=models.ManyToManyField(
                related_name='job_application_location', to='SearchTracker.jobapplicationlocation'),
        ),
        migrations.CreateModel(
            name='ResumeTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('resume', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='SearchTracker.document')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='document',
            name='resume_title',
            field=models.ManyToManyField(
                related_name='resume_title', to='SearchTracker.resumetitle'),
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128)),
                ('min_salary', models.DecimalField(blank=True,
                 decimal_places=2, max_digits=8, null=True)),
                ('max_salary', models.DecimalField(blank=True,
                 decimal_places=2, max_digits=8, null=True)),
                ('resumes_for_title', models.ManyToManyField(
                    related_name='resumes_for_title', to='SearchTracker.resumetitle')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='resumetitle',
            name='title',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='SearchTracker.title'),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='position_title',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='SearchTracker.title'),
        ),
        migrations.CreateModel(
            name='ContactEmployerTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('current', models.BooleanField(default=True)),
                ('contact', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='SearchTracker.contact')),
                ('employer', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='SearchTracker.employer')),
                ('title', models.ForeignKey(blank=True, null=True,
                 on_delete=django.db.models.deletion.CASCADE, to='SearchTracker.title')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
