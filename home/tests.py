from django.test import TestCase
from home.models import *
import datetime
from django.utils import timezone

# =====Modal Test Cases========

class TestModal(TestCase):
    def setUp(self):

        self.category1=Category.objects.create(
            name='articles',
            description='this is test description',
        )
        self.tag1=Tag.objects.create(
            name='startup'
        )
        self.user1=User.objects.create(username='dailynews',email='contact@dailynews.com')

    def test_category(self):
        self.assertEquals(self.category1.name, 'articles' )
        self.assertEquals(self.category1.description,'this is test description')
    

    def test_tag(self):
        self.assertEquals(self.tag1.name,'startup')

    def test_user(self):
        self.assertEquals(self.user1.username,'dailynews')
        self.assertEquals(self.user1.email,'contact@dailynews.com')

    def test_post(self):
        time=datetime.datetime.now(tz=timezone.utc)
        post1=Post.objects.create(
            title='this is test title',
            content='<p>this is content</p>',
            publish_date=time,
            tag=self.tag1,
            category=self.category1,
            writer=self.user1,
            meta_description='this is dailynews article meta description',
            meta_keyword='articles,book,lerning,dalilynews',
        )

        all=Post.objects.all()
        for obj in all:
            self.assertEquals(post1,obj)
            self.assertEquals(obj.title,'this is test title')
            self.assertEquals(obj.slug,'this-is-test-title')
            self.assertEquals(obj.content,'<p>this is content</p>')
            self.assertEquals(obj.meta_description,'this is dailynews article meta description')
            self.assertEquals(obj.meta_keyword,'articles,book,lerning,dalilynews')
            self.assertEquals(obj.image,'../static/img/deafult.jpg')
            self.assertEquals(obj.category,self.category1)
            self.assertEquals(obj.tag,self.tag1)
            self.assertEquals(obj.writer,self.user1)
            self.assertEquals(obj.status,0)
        self.assertEquals(all.count() ,1)


