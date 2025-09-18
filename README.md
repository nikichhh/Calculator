# 🧮 Calculator

A **Photomath-like calculator app** with support for parsing, tokenizing, and evaluating mathematical expressions.  
Built with precision using Python’s `decimal.Decimal` instead of floats.  

---

## ✨ Features
-  🔢 Expression tokenizer and parser (Shunting Yard algorithm).
- ➕➖✖️➗ Support for operators (`+`, `-`, `*`, `/`, `^`, …).
-  🔄 Unary operators (e.g., `-7`, `+5`).
-  🧮 Built-in math functions:
   - Absolute value (`abs`)
   - Logarithms (`log`, `ln`)
   - Trigonometric functions (`sin`, `cos`, `tan`, etc.)
   - Square root (`sqrt`)
-  📐 Variable support using **Sympy**:
   - Define variables (e.g., `x = 5`)
   - Use them in expressions (`2 * x + 3`)
-  🚨 Custom error handling for invalid expressions.
-  Evaluation with `decimal.Decimal` for accurate results.

---

## Roadmap
- [x] Core evaluator engine.
- [x] Variable support with Sympy.
- [x] Extended math functions (logarithms, trig, etc.).
- [ ] Frontend (desktop app with GUI).
- [ ] Mobile app (Android & iOS).
- [ ] Step-by-step solution breakdowns.

---

##  🧪 Usage
Example calculations:
```txt
2 + 3 * 4 -> 14
abs(-7) -> 7
log(100, 10) -> 2
x = 5
2 * x + 3 -> 13
```
---

## ⚙️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/calculator.git
   cd calculator
   ```
2. **Create a virtual environment (recommended)**
    ```bash
   python -m venv venv
   source venv/bin/activate   # on Linux/Mac
   venv\Scripts\activate      # on Windows
   ```
3. **Install dependencies**
    ```bash
   pip install -r requirements.txt
    ```
4. **Run the calculator (CLI)**
    ```bash
    python main.py
    ```
5. **Run the tests**
    ```bash
   pytest
    ```
---

## 👨‍💻 Development
**🚧 This is a work in progress (WIP) project.**

💡Contributions, ideas, and suggestions are welcome!

---

## 🚀 Future Vision

The long-term goal is to build a cross-platform Photomath alternative with:

📝 Step-by-step solutions

🎨 Clean, interactive UI

📱 Mobile support (Android & iOS)