import sys
from main import *

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--help":
            print("Usage: python3 codexcelerate.py [language] [options] [filename]")
            print("Options:")
            print("  --help: Show this help message")
            print("  --runtime: Optimize the input code for runtime complexity")
            print("  --explain: Explain the input code's funtionality")
            print("  --plagiarism: Check input file for plagiarised code")
            print("  --lang=[language]: Sets the language of the code to be analyzed")
        filename = sys.argv[-1]

        lang = None
        if filename.endswith(".py"):
            lang = "python"
        elif filename.endswith(".js"):
            lang = "javascript"
        elif filename.endswith(".cpp"):
            lang = "c++"
        elif filename.endswith(".c"):
            lang = "c"

        if len(sys.argv) > 2:
            filename = sys.argv[-1]
            with open(filename, 'r') as f:
                code = f.read()
            for i in range(len(sys.argv) - 1):
                if sys.argv[i][:7] == "--lang=":
                    lang = sys.argv[i][7:]
                if sys.argv[i] == "--runtime":
                    if lang is None:
                        print("Error: Language Not Set")
                        break;
                    print("Optimizing code for runtime complexity...")
                    runtime_code = runtime(code, lang)
                    print(f"Optimized Code: \n{runtime_code[0]}")
                    print("Writing to runtime_optimize.py...")
                    with open("runtime_optimize.py", "w") as f:
                        f.write(runtime_code[0])
                elif sys.argv[i] == "--explain":
                    if lang is None:
                        print("Error: Language Not Set")
                        break;
                    print("Analyzing code's function...")
                    explain_code = explain(code, lang)
                    print(f"Explanation: \n{explain_code}")
                elif sys.argv[i] == "--plagiarism":
                    if lang is None:
                        print("Error: Language Not Set")
                        break;
                    print("Checking for plagiarism...")
                    copied_code = copied(code, lang)
                    print(f"Plagiarism Status: {copied_code}")