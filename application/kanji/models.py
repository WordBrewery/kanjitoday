from django.db import models

class Kanji(models.Model):
    literal = models.CharField(max_length=255)
    grade = models.IntegerField(blank=True, null=True)
    stroke_count = models.IntegerField()
    date_used = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.literal

    def get_absolute_url(self):
        return "http://www.kanjitoday.com/kanji/%s" % self.id

    class Meta:
        ordering = ['grade']
        verbose_name_plural = 'Kanji'

class Onyomi(models.Model):
    kanji = models.ForeignKey(Kanji, related_name='onyomi')
    literal = models.CharField(max_length=255)

    def __unicode__(self):
        return self.literal

    class Meta:
        verbose_name_plural = 'Onyomi'


class Kunyomi(models.Model):
    kanji = models.ForeignKey(Kanji, related_name='kunyomi')
    literal = models.CharField(max_length=255)

    def __unicode__(self):
        return self.literal

    class Meta:
        verbose_name_plural = 'Kunyomi'

class Meaning(models.Model):
    kanji = models.ForeignKey(Kanji, related_name='meanings')
    text = models.CharField(max_length=255)

    def __unicode__(self):
        return self.text

class Nanori(models.Model):
    kanji = models.ForeignKey(Kanji, related_name='nanori')
    text = models.CharField(max_length=255)

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Nanori'

class Definition(models.Model):
    kanji = models.ForeignKey(Kanji, related_name='definitions')
    text = models.TextField()
    common = models.BooleanField(blank=True)

    def __unicode__(self):
        return self.text
