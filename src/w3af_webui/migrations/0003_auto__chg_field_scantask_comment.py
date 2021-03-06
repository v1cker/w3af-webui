# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'ScanTask.comment'
        db.alter_column(u'scan_tasks', 'comment', self.gf('django.db.models.fields.TextField')(max_length=500, null=True))

    def backwards(self, orm):
        
        # Changing field 'ScanTask.comment'
        db.alter_column(u'scan_tasks', 'comment', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'w3af_webui.profile': {
            'Meta': {'object_name': 'Profile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang_ui': ('django.db.models.fields.CharField', [], {'default': "'ru'", 'max_length': '4'}),
            'list_per_page': ('django.db.models.fields.PositiveIntegerField', [], {'default': '50'}),
            'notification': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': "orm['auth.User']"})
        },
        'w3af_webui.profilestargets': {
            'Meta': {'object_name': 'ProfilesTargets', 'db_table': "u'profiles_targets'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scan_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['w3af_webui.ScanProfile']", 'blank': 'True'}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['w3af_webui.Target']", 'blank': 'True'})
        },
        'w3af_webui.profilestasks': {
            'Meta': {'object_name': 'ProfilesTasks', 'db_table': "u'profiles_tasks'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scan_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['w3af_webui.ScanProfile']"}),
            'scan_task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['w3af_webui.ScanTask']", 'blank': 'True'})
        },
        'w3af_webui.scan': {
            'Meta': {'object_name': 'Scan', 'db_table': "u'scans'"},
            'data': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True'}),
            'finish': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1991, 1, 1, 0, 0)', 'null': 'True'}),
            'pid': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'null': 'True'}),
            'result_message': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000', 'null': 'True'}),
            'scan_task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['w3af_webui.ScanTask']"}),
            'start': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 3, 22, 10, 16, 37, 502496)'}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        'w3af_webui.scanprofile': {
            'Meta': {'object_name': 'ScanProfile', 'db_table': "u'scan_profiles'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'short_comment': ('django.db.models.fields.CharField', [], {'max_length': '240', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'w3af_profile': ('django.db.models.fields.TextField', [], {'default': "'\\n'", 'blank': 'True'})
        },
        'w3af_webui.scantask': {
            'Meta': {'object_name': 'ScanTask', 'db_table': "u'scan_tasks'"},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'cron': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'repeat_at': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'repeat_each': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'repeat_each_day': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'repeat_each_weekday': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['w3af_webui.Target']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'w3af_webui.target': {
            'Meta': {'object_name': 'Target', 'db_table': "u'targets'"},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_scan': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '240'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['w3af_webui']
