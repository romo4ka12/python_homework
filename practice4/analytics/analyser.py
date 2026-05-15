class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented use a child class")

    def print_results(self):
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"

class TopStudentsAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self, n=10):
        valid_students = []
        for s in self.students:
            try:
                float(s['final_exam_score'])
                valid_students.append(s)
            except (ValueError, KeyError):
                continue

        top_n = sorted(valid_students, key=lambda x: float(x['final_exam_score']), reverse=True)[:n]

        top_n_list = []
        for i, student in enumerate(top_n):
            top_n_list.append({
                "rank": i + 1,
                "student_id": student['student_id'],
                "country": student['country'],
                "major": student['major'],
                "final_exam_score": float(student['final_exam_score']),
                "GPA": float(student['GPA'])
            })

        self.result = {
            "total_students": len(self.students),
            "top_10": top_n_list
        }
        return self.result

    def print_results(self):
        print("\n--- TOP STUDENTS ANALYSIS REPORT ---")
        super().print_results()
        print("--- END OF REPORT ---")

    def __str__(self):
        return f"TopStudentsAnalyser: Ranking analysis, {len(self.students)} students"

class CountryAnalyser(DataAnalyser):
    def analyse(self):
        countries = [s['country'] for s in self.students]
        self.result = {"total_countries": len(set(countries))}

    def __str__(self):
        return f"CountryAnalyser: Country Analysis, {len(self.students)} students"