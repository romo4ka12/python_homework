import os
import csv
import json

FILE_NAME = 'practice4/global_university_students_performance_habits_10000.csv'

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file..")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found.")
            return False

    def create_output_folder(self, folder='output'):
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")

class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.students.append(row)
            print(f"Data loaded successfully: {len(self.students)} students")
        except Exception as e:
            print(f"Error: {e}")
        return self.students

    def preview(self, n=5):
        print(f"First {n} rows:")
        for i in range(min(n, len(self.students))):
            s = self.students[i]
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")
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
            except ValueError:
                continue

        top_n = sorted(valid_students, key=lambda x: float(x['final_exam_score']), reverse=True)[:n]

        top_n_list = []
        for i, student in enumerate(top_n):
            top_n_list.append({
                "rank": i + 1,
                "student_id": student['student_id'],
                "country": student['country'],
                "final_exam_score": float(student['final_exam_score'])
            })

        self.result = {
            "total_students": len(self.students),
            "top_10": top_n_list
        }

    def print_results(self):
        print("\n--- TOP STUDENTS ANALYSIS REPORT ---")
        super().print_results()
        print("--- END OF REPORT ---")
    def __str__(self):
        return f"TopStudentsAnalyser: Ranking analysis, {len(self.students)} students"

class CountryAnalyser(DataAnalyser):
    def analyse(self):
        countries = [s['country'] for s in self.students]
        self.result = {"unique_countries": len(set(countries))}

    def __str__(self):
        return f"CountryAnalyser: Country Analysis, {len(self.students)} students"

class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        with open(self.output_path, mode='w', encoding='utf-8') as f:
            json.dump(self.result, f, indent=4)
        print(f"Result saved to {self.output_path}")

class Report:
    def __init__(self, analyser, saver):
            self.analyser = analyser
            self.saver = saver

    def generate(self):
        print("Generating report...")
        self.analyser.analyse()
        self.analyser.print_results()
        self.saver.save_json()
        print("Report complete.")

fm = FileManager(FILE_NAME)
if not fm.check_file():
    exit()
fm.create_output_folder()

dl = DataLoader(FILE_NAME)
dl.load()
dl.preview()

print("\nRunning all analysers:")
analysers = [
    TopStudentsAnalyser(dl.students[:20]),
    CountryAnalyser(dl.students[:20])
]

for a in analysers:
    print(a)
    a.analyse()
    a.print_results()

final_analyser = TopStudentsAnalyser(dl.students)
saver = ResultSaver(final_analyser.result, 'output/result.json')
report = Report(final_analyser, saver)
report.generate()