import os

def evaluate_fixes():
    if not os.path.exists("test_results.txt"):
        print("❌ Error: test_results.txt not found!")
        return
    with open("test_results.txt", "r") as f:
        test_results = f.readlines()
    passed_tests = sum(1 for line in test_results if "PASSED" in line)
    total_tests = len(test_results)
    pass_k = passed_tests / total_tests if total_tests > 0 else 0
    print(f"✅ Pass@1: {pass_k:.2f}")

evaluate_fixes()
