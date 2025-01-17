import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.timezone import now

"""
Course content had me import utc from django.utils.timezone, but it didn't
work. I assume because it is deprecated from the older version. I instead
brought in the now function from that location, and used it to create
a datetime value based on the setting of UTC timezone, and I was able
to look up the tzinfo value from that datetime object.
"""

from blogging.models import Post, Category


class FrontEndTestCase(TestCase):
    """test views privided in the front-end"""

    fixtures = [
        "blogging_test_fixture.json",
    ]

    def setUp(self):
        self.now = datetime.datetime.now(datetime.timezone.utc).replace(
            tzinfo=now().tzinfo
        )
        """
        above line instead of doing datetime.datetime.utcnow(), which was
        deprecated, I did the now function and passed into that function
        the datetime.timezone.utc timezone value.
        """
        self.timedelta = datetime.timedelta(15)
        author = User.objects.get(pk=1)
        for count in range(1, 11):
            post = Post(title="Post %d Title" % count, text="foo", author=author)
            if count < 6:
                # publish the first five posts
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate
            post.save()

    def test_list_only_published(self):
        resp = self.client.get("/")
        # The content of the renered response is always a byte-string
        resp_text = resp.content.decode(resp.charset)
        self.assertTrue("All Posts" in resp_text)
        for count in range(1, 11):
            title = "Post %d Title" % count
            if count < 6:
                self.assertContains(resp, title, count=1)
            else:
                self.assertNotContains(resp, title)

    def test_details_only_published(self):
        for count in range(1, 11):
            title = "Post %d Title" % count
            post = Post.objects.get(title=title)
            resp = self.client.get("/posts/%d" % post.pk, follow=True)
            """
            Note to self

            I had to add follow=True to my client.get call above or else
            the resp was not getting any content and was a response of a
            redirect url. setting follow=True, the redirect gets us to the
            url we actually want to return, a 200 response and the content
            of the details page for our blogging site.
            """
            if count < 6:
                self.assertEqual(resp.status_code, 200)
                self.assertContains(resp, title)
            else:
                self.assertEqual(resp.status_code, 404)


class PostTestCase(TestCase):
    fixtures = [
        "blogging_test_fixture.json",
    ]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)


class CategoryTestCase(TestCase):

    def test_string_representation(self):
        expected = "A Category"
        c1 = Category(name=expected)
        actual = str(c1)
        self.assertEqual(actual, expected)
