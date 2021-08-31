from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


class UploadFilesModel(models.Model):
    id = models.AutoField(primary_key = True, db_column = 'upload_file_id')
    upload_file_name = models.CharField(max_length = 100, null = False, db_column = 'upload_file_name')
    register_date = models.DateField(auto_now_add = True, db_column = 'register_date')

    user_id = models.ForeignKey(AUTH_USER_MODEL, on_delete = models.DO_NOTHING, db_column = 'user_id')

    class Meta:
        managed = False
        db_table = 'upload_files'

    def __str__(self):
        return '{}/{}'.format(self.user_id, self.upload_file_name)
