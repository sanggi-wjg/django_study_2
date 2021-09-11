import datetime

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 100, blank = True, default = '')
    code = models.TextField()
    linenos = models.BooleanField(default = False)
    language = models.CharField(choices = LANGUAGE_CHOICES, default = 'python', max_length = 100)
    style = models.CharField(choices = STYLE_CHOICES, default = 'friendly', max_length = 100)

    class Meta:
        ordering = ['created']


class StatPartner(models.Model):
    idx = models.BigAutoField(primary_key = True)
    logYear = models.PositiveSmallIntegerField(db_column = 'logYear')
    logMonth = models.PositiveSmallIntegerField(db_column = 'logMonth')
    logWeek = models.PositiveSmallIntegerField(db_column = 'logWeek')
    logDay = models.PositiveSmallIntegerField(db_column = 'logDay')
    logDayOfWeek = models.PositiveSmallIntegerField(db_column = 'logDayOfWeek')
    logDate = models.CharField(db_column = 'logDate', max_length = 8)
    statId = models.CharField(db_column = 'statId', max_length = 100)

    inST01 = models.PositiveIntegerField(db_column = 'inST01', default = 0)
    inST02 = models.PositiveIntegerField(db_column = 'inST02', default = 0)
    inST03 = models.PositiveIntegerField(db_column = 'inST03', default = 0)
    inST04 = models.PositiveIntegerField(db_column = 'inST04', default = 0)
    inST05 = models.PositiveIntegerField(db_column = 'inST05', default = 0)
    inST06 = models.PositiveIntegerField(db_column = 'inST06', default = 0)
    inST41 = models.PositiveIntegerField(db_column = 'inST41', default = 0)
    inST42 = models.PositiveIntegerField(db_column = 'inST42', default = 0)
    inST43 = models.PositiveIntegerField(db_column = 'inST43', default = 0)
    inST44 = models.PositiveIntegerField(db_column = 'inST44', default = 0)
    inST99 = models.PositiveIntegerField(db_column = 'inST99', default = 0)

    outOT01 = models.PositiveIntegerField(db_column = 'outOT01', default = 0)
    outOT31 = models.PositiveIntegerField(db_column = 'outOT31', default = 0)
    outOT33 = models.PositiveIntegerField(db_column = 'outOT33', default = 0)
    outOT35 = models.PositiveIntegerField(db_column = 'outOT35', default = 0)
    outOT44 = models.PositiveIntegerField(db_column = 'outOT44', default = 0)
    outOT99 = models.PositiveIntegerField(db_column = 'outOT99', default = 0)

    outTC01 = models.PositiveIntegerField(db_column = 'outTC01', default = 0)
    outTC02 = models.PositiveIntegerField(db_column = 'outTC02', default = 0)
    outTC03 = models.PositiveIntegerField(db_column = 'outTC03', default = 0)
    outTC04 = models.PositiveIntegerField(db_column = 'outTC04', default = 0)
    outTC05 = models.PositiveIntegerField(db_column = 'outTC05', default = 0)
    outTC06 = models.PositiveIntegerField(db_column = 'outTC06', default = 0)
    outTC07 = models.PositiveIntegerField(db_column = 'outTC07', default = 0)
    outTC08 = models.PositiveIntegerField(db_column = 'outTC08', default = 0)
    outTC09 = models.PositiveIntegerField(db_column = 'outTC09', default = 0)
    outTC11 = models.PositiveIntegerField(db_column = 'outTC11', default = 0)
    outTC15 = models.PositiveIntegerField(db_column = 'outTC15', default = 0)
    outTC16 = models.PositiveIntegerField(db_column = 'outTC16', default = 0)
    outTC21 = models.PositiveIntegerField(db_column = 'outTC21', default = 0)
    outTC23 = models.PositiveIntegerField(db_column = 'outTC23', default = 0)
    outTC24 = models.PositiveIntegerField(db_column = 'outTC24', default = 0)
    outTC25 = models.PositiveIntegerField(db_column = 'outTC25', default = 0)
    outTC27 = models.PositiveIntegerField(db_column = 'outTC27', default = 0)
    outTC28 = models.PositiveIntegerField(db_column = 'outTC28', default = 0)
    outTC29 = models.PositiveIntegerField(db_column = 'outTC29', default = 0)
    outTC36 = models.PositiveIntegerField(db_column = 'outTC36', default = 0)
    outTC98 = models.PositiveIntegerField(db_column = 'outTC98', default = 0)
    outTC99 = models.PositiveIntegerField(db_column = 'outTC99', default = 0)

    outPackageTC01 = models.PositiveIntegerField(db_column = 'outPackageTC01', default = 0)
    outPackageTC02 = models.PositiveIntegerField(db_column = 'outPackageTC02', default = 0)
    outPackageTC03 = models.PositiveIntegerField(db_column = 'outPackageTC03', default = 0)
    outPackageTC04 = models.PositiveIntegerField(db_column = 'outPackageTC04', default = 0)
    outPackageTC05 = models.PositiveIntegerField(db_column = 'outPackageTC05', default = 0)
    outPackageTC06 = models.PositiveIntegerField(db_column = 'outPackageTC06', default = 0)
    outPackageTC07 = models.PositiveIntegerField(db_column = 'outPackageTC07', default = 0)
    outPackageTC08 = models.PositiveIntegerField(db_column = 'outPackageTC08', default = 0)
    outPackageTC09 = models.PositiveIntegerField(db_column = 'outPackageTC09', default = 0)
    outPackageTC11 = models.PositiveIntegerField(db_column = 'outPackageTC11', default = 0)
    outPackageTC15 = models.PositiveIntegerField(db_column = 'outPackageTC15', default = 0)
    outPackageTC16 = models.PositiveIntegerField(db_column = 'outPackageTC16', default = 0)
    outPackageTC21 = models.PositiveIntegerField(db_column = 'outPackageTC21', default = 0)
    outPackageTC23 = models.PositiveIntegerField(db_column = 'outPackageTC23', default = 0)
    outPackageTC24 = models.PositiveIntegerField(db_column = 'outPackageTC24', default = 0)
    outPackageTC25 = models.PositiveIntegerField(db_column = 'outPackageTC25', default = 0)
    outPackageTC27 = models.PositiveIntegerField(db_column = 'outPackageTC27', default = 0)
    outPackageTC28 = models.PositiveIntegerField(db_column = 'outPackageTC28', default = 0)
    outPackageTC29 = models.PositiveIntegerField(db_column = 'outPackageTC29', default = 0)
    outPackageTC36 = models.PositiveIntegerField(db_column = 'outPackageTC36', default = 0)
    outPackageTC98 = models.PositiveIntegerField(db_column = 'outPackageTC98', default = 0)
    outPackageTC99 = models.PositiveIntegerField(db_column = 'outPackageTC99', default = 0)

    regDate = models.DateTimeField(db_column = 'regDate', blank = True, null = True, default = datetime.datetime.now)
    remark = models.TextField(db_column = 'remark', blank = True, null = True)

    class Meta:
        managed = True
        db_table = 'stat_partner'
        unique_together = (('logDate', 'statId'),)
        ordering = ['idx']
