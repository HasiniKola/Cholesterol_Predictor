import unittest
from model import predict_cholesterol

class TestCholesterolModel(unittest.TestCase):
    def test_prediction_range(self):
        result = predict_cholesterol(age=30, bmi=25, blood_pressure=120, activity_level=2)
        self.assertTrue(100 <= result <= 300)

    def test_low_activity(self):
        result = predict_cholesterol(age=50, bmi=30, blood_pressure=140, activity_level=1)
        self.assertGreater(result, 200)

if __name__ == '__main__':
    unittest.main()
