import unittest
from analytics.analyser import TopStudentsAnalyser

class TestAnalyser(unittest.TestCase):
    def setUp(self):
        self.sample = [
            {"student_id": "1", "GPA": "3.8", "final_exam_score": "95", "country": "USA", "major": "CS"},
            {"student_id": "2", "GPA": "2.5", "final_exam_score": "72", "country": "India", "major": "Math"},
            {"student_id": "3", "GPA": "3.9", "final_exam_score": "98", "country": "USA", "major": "Physics"},
            {"student_id": "4", "GPA": "1.8", "final_exam_score": "55", "country": "Canada", "major": "Arts"},
            {"student_id": "5", "GPA": "3.5", "final_exam_score": "88", "country": "India", "major": "CS"}
        ]

    def test_result_is_not_empty(self):
        analyser = TopStudentsAnalyser(self.sample)
        analyser.analyse()
        self.assertNotEqual(analyser.result, {})

    def test_total_students(self):
        analyser = TopStudentsAnalyser(self.sample)
        analyser.analyse()
        self.assertEqual(analyser.result["total_students"], 5)

    def test_result_has_required_keys(self):
        analyser = TopStudentsAnalyser(self.sample)
        analyser.analyse()
        self.assertIn("top_10", analyser.result)

    def test_analyse_twice(self):
        analyser = TopStudentsAnalyser(self.sample)
        analyser.analyse()
        result1 = analyser.result.copy()
        analyser.analyse()
        self.assertEqual(analyser.result, result1)