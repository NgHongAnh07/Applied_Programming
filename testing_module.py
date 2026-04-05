import unittest

# Import functions from your main module
from module import (
    is_valid_date,
    get_sign_from_date,
    get_sign_index
)

# Minimal zodiac dataset for testing
zodiac_data = {
    "aries": {"start": "3-21", "end": "4-19"},
    "taurus": {"start": "4-20", "end": "5-20"},
    "gemini": {"start": "5-21", "end": "6-20"},
    "capricorn": {"start": "12-22", "end": "1-19"}
}

signs_list = [
    "aries", "taurus", "gemini", "cancer", "leo", "virgo",
    "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"
]


# ---------------------------
# DATE VALIDATION TESTS
# ---------------------------
class TestDateValidation(unittest.TestCase):

    def test_valid_dates(self):
        self.assertTrue(is_valid_date(1, 1))
        self.assertTrue(is_valid_date(12, 31))
        self.assertTrue(is_valid_date(2, 29))  # allowed in your logic

    def test_invalid_months(self):
        self.assertFalse(is_valid_date(0, 10))
        self.assertFalse(is_valid_date(13, 5))

    def test_invalid_days(self):
        self.assertFalse(is_valid_date(4, 31))  # April has 30 days
        self.assertFalse(is_valid_date(2, 30))
        self.assertFalse(is_valid_date(1, 0))


# ---------------------------
# ZODIAC SIGN DETECTION TESTS
# ---------------------------
class TestGetSign(unittest.TestCase):

    def test_middle_dates(self):
        self.assertEqual(get_sign_from_date(3, 25, zodiac_data), "aries")
        self.assertEqual(get_sign_from_date(5, 10, zodiac_data), "taurus")

    def test_boundary_dates(self):
        self.assertEqual(get_sign_from_date(3, 21, zodiac_data), "aries")
        self.assertEqual(get_sign_from_date(4, 19, zodiac_data), "aries")
        self.assertEqual(get_sign_from_date(4, 20, zodiac_data), "taurus")

    def test_capricorn_cross_year(self):
        self.assertEqual(get_sign_from_date(12, 25, zodiac_data), "capricorn")
        self.assertEqual(get_sign_from_date(1, 10, zodiac_data), "capricorn")

    def test_invalid_date_returns_none(self):
        result = get_sign_from_date(2, 31, zodiac_data)
        self.assertIsNone(result)


# ---------------------------
# SIGN INDEX TESTS
# ---------------------------
class TestSignIndex(unittest.TestCase):

    def test_valid_signs(self):
        self.assertEqual(get_sign_index(signs_list, "aries"), 0)
        self.assertEqual(get_sign_index(signs_list, "leo"), 4)
        self.assertEqual(get_sign_index(signs_list, "pisces"), 11)

    def test_invalid_sign(self):
        self.assertEqual(get_sign_index(signs_list, "notasign"), -1)


# ---------------------------
# INTEGRATION TEST (REAL FLOW)
# ---------------------------
class TestIntegration(unittest.TestCase):

    def test_full_flow(self):
        # Step 1: Validate date
        self.assertTrue(is_valid_date(3, 25))

        # Step 2: Get sign
        sign = get_sign_from_date(3, 25, zodiac_data)
        self.assertEqual(sign, "aries")

        # Step 3: Get index
        index = get_sign_index(signs_list, sign)
        self.assertEqual(index, 0)


if __name__ == "__main__":
    unittest.main()