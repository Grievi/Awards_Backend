from django.test import TestCase
from backend.models import *

class ProfileTest(TestCase):
    def  setUp(self):
        self.user = User(id=1, username='Admin', password='angular12')
        self.user.save()

    def test_save_user(self):
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

class ProjectTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id=1, username='Admin')
        self.post = Project.objects.create(id=1, project_name='Delani', photo='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e', description='All About the studio', user=self.user, project_url='http://ur.coml')

    def test_save_project(self):
        self.project.save_project()
        project = Project.objects.all()
        self.assertTrue(len(project) > 0)

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))
                                        

    def test_get_project(self):
        self.project.save_project()
        project = Project.objects.all()
        self.assertTrue(len(project) > 0)

class ReviewTest(TestCase):

    def test_instance(self):
        self.assertTrue(isinstance(self.review, Review))

    def test_save_rating(self):
        self.review.save_review()
        review = Review.objects.all()
        self.assertTrue(len(review) > 0)