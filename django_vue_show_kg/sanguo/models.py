from django.db import models

# Create your models here.
from django.db import models
from markdown import Markdown
"""
这里是数据库要保存的数据字段，人物编号，姓名，武力值，智力值，特性，必杀技，
义理，相性，种族，性别，头像，图片，简介，完整介绍​
number text, name text, wuli text, zhili text, texing1 text,
texing2 text, texing3 text, bishaji text, yili text, 
xiangxing text, zhongzu text, gender text, img text, 
figure text,desc text, text_all text​
"""
class People(models.Model):
    """人物资料 model"""
    number = models.TextField()
    name = models.TextField()
    wuli = models.TextField()
    zhili = models.TextField()
    texing1 = models.TextField()
    texing2 = models.TextField()
    texing3 = models.TextField()
    bishaji = models.TextField()
    yili = models.TextField()
    xiangxing = models.TextField()
    zhongzu = models.TextField()
    gender = models.TextField()
    img = models.TextField()
    figure = models.TextField()
    desc = models.TextField()
    text_all = models.TextField()
    
    class Meta:
        # 安装字段排序
        ordering = ['name']

    def __str__(self):
        return self.name
    # 创建markdown格式
    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        md_body = md.convert(self.body)
        return md_body, md.toc
