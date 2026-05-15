from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import TopStudentsAnalyser, CountryAnalyser

FILE_NAME = 'global_university_students_performance_habits_10000.csv'

fm = FileManager(FILE_NAME)
if fm.check_file():
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