import unittest

from services import UserService


class UserServiceCalculator(unittest.TestCase):
    def test_get_profile_posts(self):
        with self.assertRaises(ValueError):
            UserService.get_profiles_posts(
                "www.linkedin.com/in/andrei-alexandru-ungureanu-8a0a3a1a5/"
            )
            UserService.get_profiles_posts("https://www.nonexistent.com")
            UserService.get_profiles_posts(None)
            UserService.get_profiles_posts(13)
            UserService().get_profiles_posts(
                "https://www.linkedin.com/in/andrei-alexandru-ungureanu-0000000000000/"
            )

    def test_get_personal_profile(self):
        with self.assertRaises(ValueError):
            UserService.get_personal_profile(
                "www.linkedin.com/in/andrei-alexandru-ungureanu-8a0a3a1a5/"
            )
            UserService.get_personal_profile("https://www.nonexistent.com")
            UserService.get_personal_profile(None)
            UserService.get_personal_profile(13)
            UserService().get_personal_profile(
                "https://www.linkedin.com/in/andrei-alexandru-ungureanu-8a0a3a1a5/"
            )


def main():
    unittest.main()


if __name__ == "__main__":
    main()
