from src.analyzer import Analyzer

def test_analyzer_initialization():
    analyzer = Analyzer()
    assert analyzer.lint_file == "lint_report.txt"
