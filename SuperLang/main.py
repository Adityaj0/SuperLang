from runner import run
import sys

print("Welcome to SuperLang!")

# Check if a file is passed
if len(sys.argv) > 1:
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        code = f.read()
    run(code)
else:
    print("Type 'exit' to quit.")
    while True:
        try:
            text = input('SuperLang > ')
            if text == "exit":
                break
            run(text)
        except Exception as e:
            print(f"Error: {e}")
