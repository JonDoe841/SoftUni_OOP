from project.social_media import SocialMedia
from unittest import TestCase,main

class SocialMediaTest(TestCase):
    def setUp(self):
        self.m = SocialMedia("Test","YouTube",100,"idktwin")
    def test_init(self):
        self.assertEqual(self.m._username,"Test")
        self.assertEqual(self.m._platform, "YouTube")
        self.assertEqual(self.m._followers, 100)
        self.assertEqual(self.m._content_type, "idktwin")
        self.assertEqual(self.m._posts, [])
    def test_invalid_platform(self):
        with self.assertRaises(ValueError) as ex:
            self.m._validate_and_set_platform("Facebook")
        self.assertEqual(str(ex.exception), f"Platform should be one of ['Instagram', 'YouTube', 'Twitter']")
    def test_invalid_followers(self):
        with self.assertRaises(ValueError) as ex:
            self.m.followers = -1
        self.assertEqual(str(ex.exception),"Followers cannot be negative.")
    def test_invalid_platform_for_validate_and_set_platform(self):
        with self.assertRaises(ValueError)as ex:
            self.m._validate_and_set_platform("Facebook")
        self.assertEqual(str(ex.exception),f"Platform should be one of ['Instagram', 'YouTube', 'Twitter']")
    def test_create_post(self):
        self.assertEqual(self.m._posts, [])
        result = self.m.create_post("Testing")
        self.assertEqual(result,f"New idktwin post created by Test on YouTube.")
        self.assertEqual(self.m._posts,[{'content': "Testing", 'likes': 0, 'comments': []}])
    def test_like_post_liked(self):
        self.m._posts = [{'content': "Testing", 'likes': 0, 'comments': []}]
        result = self.m.like_post(0)
        self.assertEqual(result,f"Post liked by Test.")
    def test_like_post_max_likes(self):
        self.m._posts = [{'content': "Testing", 'likes': 10, 'comments': []}]
        result = self.m.like_post(0)
        self.assertEqual(result,f"Post has reached the maximum number of likes.")
    def test_like_post_out_of_index(self):
        result = self.m.like_post(100)
        self.assertEqual(result,"Invalid post index.")
    def test_comment_on_post_valid(self):
        self.m._posts = [{'content': "Testing", 'likes': 10, 'comments': []}]
        self.assertEqual(self.m._posts,[{'content': "Testing", 'likes': 10, 'comments': []}])
        result = self.m.comment_on_post(0,"Lock in twin")
        self.assertEqual(result,f"Comment added by Test on the post.")
        self.m._posts = [{'content': "Testing", 'likes': 10, 'comments': ["Lock in twin"]}]
    def test_comment_on_post_invalid(self):
        self.m._posts = [{'content': "Testing", 'likes': 10, 'comments': []}]
        result = self.m.comment_on_post(0,"Lock in")
        self.assertEqual(result,"Comment should be more than 10 characters.")

if __name__ == "__main__":
    main()