import os
import csv
import json

FILE_NAME = 'global_university_students_performance_habits_10000.csv'
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found. Please download the file from LMS.")
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
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
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

    def analyse(self, n=10):
        valid_students = []
        for s in self.students:
            try:
                float(s['final_exam_score'])
                valid_students.append(s)
            except ValueError:
                print(f"Warning: could not convert value for student {s.get('student_id', 'Unknown')} - skipping row.")
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
            "analysis": "Top 10 Students by Exam Score",
            "total_students": len(self.students),
            "top_10": top_n_list
        }
        return self.result

    def print_results(self):
        print("\nTop 10 Students by Exam Score")
        for item in self.result.get("top_10", []):
            print(
                f"{item['rank']}. {item['student_id']} | {item['country']} | {item['major']} | Score: {item['final_exam_score']} | GPA: {item['GPA']}")

    def print_extra_filters(self):
        print("\nLambda / Map / Filter")
        try:
            top_scorers = list(filter(lambda s: float(s['final_exam_score']) > 95, self.students))
            print(f"Students with score > 95: {len(top_scorers)}")

            gpa_values = list(map(lambda s: float(s['GPA']), self.students))
            print(f"GPA values (first 5): {gpa_values[:5]}")

            good_assignments = list(filter(lambda s: float(s['assignment_score']) > 90, self.students))
            print(f"Students assignment > 90: {len(good_assignments)}")
        except ValueError:
            print("Skipped extra filters due to invalid float data in some rows.")

class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, mode='w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4)
            print(f"\nResult saved to {self.output_path}")
        except Exception as e:
            print(f"\nError writing to file: {e}")


fm = FileManager(FILE_NAME)
if not fm.check_file():
    print('Stopping program.')
    exit()
fm.create_output_folder()

dl = DataLoader(FILE_NAME)
dl.load()
dl.preview()

analyser = DataAnalyser(dl.students)
analyser.analyse()
analyser.print_results()

analyser.print_extra_filters()

saver = ResultSaver(analyser.result, 'output/result.json')
saver.save_json()