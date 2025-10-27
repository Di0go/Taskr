# ----------------------------------------------
# projects/tests.py
# Tests for the projects app
# 
# <diogopinto> 2025+
# ----------------------------------------------



from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Project

User = get_user_model()



# EN: Tests for the projects module
class ProjectViewsTests(TestCase):

    # EN: We'll create three users, one to own the project, one has member and another one that shouldn't have any type of access to the project
    def setUp(self):

        self.owner = User.objects.create_user(username="owner", password="pass123")
        self.member = User.objects.create_user(username="member", password="pass123")
        self.other_user = User.objects.create_user(username="stranger", password="pass123")

        # EN: We then assign the created users as owner and members and leave the "stranger" user out of the member list
        self.project = Project.objects.create(
            name="Proj1", description="Test project", owner=self.owner
        )
        self.project.members.add(self.owner, self.member)



    # --------------------------------------------------------
    #   EN: INDEX VIEW
    def test_index_shows_only_member_projects(self):

        # EN: User in project, should be able to see in project list
        self.client.login(username="member", password="pass123")
        response = self.client.get(reverse("projects:index"))

        self.assertContains(response, "Proj1")

        # EM: User not in project, shouldn't be able to see in project list
        self.client.login(username="stranger", password="pass123")
        response = self.client.get(reverse("projects:index"))

        self.assertNotContains(response, "Proj1")



    # --------------------------------------------------------
    # EN: DETAIL VIEW
    def test_detail_access_by_member(self):

        # EN: User in project, should be able to see the project's detail's
        self.client.login(username="member", password="pass123")
        url = reverse("projects:detail", args=[self.project.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Proj1")

    def test_detail_denied_for_non_member(self):

        # EN: User not in project, shouldn't be able to see the project's detail's
        self.client.login(username="stranger", password="pass123")
        url = reverse("projects:detail", args=[self.project.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)



    # --------------------------------------------------------
    # EN: CREATE PROJECT VIEW
    def test_create_project_success(self):

        self.client.login(username="owner", password="pass123")

        response = self.client.post(reverse("projects:create_project"), 
        {
            "name": "NewProj",
            "description": "Brand new project",
        })

        # EN: Should redirect back to index
        self.assertRedirects(response, reverse("projects:index"))

        # EN: Project should exist in DB
        new_project = Project.objects.get(name="NewProj")

        self.assertEqual(new_project.owner, self.owner)
        self.assertIn(self.owner, new_project.members.all())

    def test_create_project_requires_login(self):
        response = self.client.get(reverse("projects:create_project"))

        # EN: Redirect to login
        self.assertEqual(response.status_code, 302)

    # --------------------------------------------------------
    # EN: DELETE PROJECT VIEW
    def test_owner_can_delete_project(self):

        self.client.login(username="owner", password="pass123")
        url = reverse("projects:delete_project", args=[self.project.id])
        response = self.client.post(url)

        # EN: As owner, should be able to delete the project
        self.assertRedirects(response, reverse("projects:index"))
        self.assertFalse(Project.objects.filter(id=self.project.id).exists())

    def test_non_owner_cannot_delete_project(self):

        self.client.login(username="member", password="pass123")
        url = reverse("projects:delete_project", args=[self.project.id])
        response = self.client.post(url)

        # EN: As an non-owner, shouldn't be able to delete the project
        self.assertEqual(response.status_code, 404)
        self.assertTrue(Project.objects.filter(id=self.project.id).exists())

    # --------------------------------------------------------
    # EN: LEAVE PROJECT VIEW
    def test_member_can_leave_project(self):

        self.client.login(username="member", password="pass123")
        url = reverse("projects:leave_project", args=[self.project.id])
        response = self.client.post(url)

        # EN: As a member, should be able to leave the project
        self.assertRedirects(response, reverse("projects:index"))
        self.assertNotIn(self.member, self.project.members.all())

    def test_non_member_cannot_leave_project(self):
        self.client.login(username="stranger", password="pass123")
        url = reverse("projects:leave_project", args=[self.project.id])

        # EN: As a stranger, shouldn't be able to leave the project
        response = self.client.post(url)
        self.assertEqual(response.status_code, 404)
