# 🧠 SuperLang

Welcome to **SuperLang** — a beginner-friendly, lightweight, and extensible programming language created fully in **Python**! Designed for fun, education, and practicing language and compiler theory fundamentals.

## ✨ About

SuperLang is a **plain-English-inspired** programming language with a custom **lexer**, **parser**, and **interpreter** built using Python. It helps you understand how real programming languages work internally — from source code to execution — while keeping the syntax simple and human-readable.

## 🚀 Features

* **Plain English Syntax** — Write code like natural sentences
* **Variables** — Use `let` to create variables
* **Basic Arithmetic** — `plus`, `minus`, `times`, `divide`
* **Conditionals** — `if`, `else`, and `greater_than`
* **Loops** — `repeat n times`
* **Functions** — Define and call simple functions
* **Output** — Use `say` to print
* **Interactive REPL** — Test SuperLang live

## 📦 Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/superlang.git
cd superlang
```

2. (Optional) Install locally for easier usage:

```bash
pip install -e .
```

This allows you to use the superlang command globally.

## 🖥️ Usage

### Interactive REPL Mode

```bash
python runner.py
```

Or if installed globally:

```bash
superlang
```

Example REPL session:

```
🧠 Welcome to SuperLang!
Type 'exit' to quit.
SuperLang > let x equal 5
SuperLang > say x plus 10
15
SuperLang > exit
```

### Running Scripts

Create a file program.spl:

```superlang
let a equal 10
let b equal 20
say "Sum is: " plus a plus b

if a greater_than b
    say "A is bigger!"
else
    say "B is bigger!"

repeat 2 times
    say "Repeating the fun!"

do double n
    say n times 2

double a
```

Run it with:

```bash
python runner.py program.spl
```

Or if installed globally:

```bash
superlang program.spl
```

Example output:

```
Sum is: 30
B is bigger!
Repeating the fun!
Repeating the fun!
20
```

## 📚 Language Reference

| Concept | Syntax Example | Description |
|---------|----------------|-------------|
| Variables | `let x equal 5` | Declare variables |
| Printing | `say "Hello"` | Output text |
| Math | `plus`, `minus`, `times`, `divide` | Basic arithmetic |
| Comparisons | `greater_than`, `equals` | Value comparisons |
| Conditionals | `if...else` | Control flow |
| Loops | `repeat 3 times` | Repeat blocks |
| Functions | `do func param then...` | Define and call functions |

## 💡 Roadmap

Planned features:

- Boolean operations (and, or, not)
- Additional comparisons (less_than, not_equal)
- While loops
- Lists and arrays
- File I/O operations
- Basic object support

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## 📜 License

MIT © Aditya Jain

## 👏 Credits

Created by Aditya Jain