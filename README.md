<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&duration=2500&pause=900&color=F7C948&center=true&vCenter=true&width=650&lines=Factorial+Calculator+%F0%9F%94%A2;n!+%3D+n+%C3%97+(n-1)+%C3%97+...+%C3%97+1;Simple.+Fast.+Pythonic.+%E2%9C%A8" alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3.6%2B-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B&labelColor=1a1a2e)
![Status](https://img.shields.io/badge/Status-Active-2ECC71?style=for-the-badge&labelColor=1a1a2e)
![License](https://img.shields.io/badge/License-MIT-9B59B6?style=for-the-badge&labelColor=1a1a2e)
![Made with](https://img.shields.io/badge/Made%20with-%E2%9D%A4-FF4B4B?style=for-the-badge&labelColor=1a1a2e)

</div>

<p align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Abacus.png" width="90"/>
</p>

<h1 align="center">🎩✨ The Factorial Calculator ✨🎩</h1>

<p align="center">
  <em>A tiny, elegant Python script that turns a single number into its full factorial — instantly.</em>
</p>

<p align="center">
  <img src="https://media.giphy.com/media/xTiTnxpQ3ghPiB2Hp6/giphy.gif" width="380" alt="magic animation"/>
</p>

---

## 📖 Table of Contents

- [What is a Factorial?](#-what-is-a-factorial)
- [How the Code Works](#-how-the-code-works)
- [Program Flow](#-program-flow)
- [Full Source Code](#-full-source-code)
- [Live Output Examples](#-live-output-examples)
- [Getting Started](#-getting-started)
- [Edge Cases Handled](#-edge-cases-handled)
- [License](#-license)

---

## 🧮 What is a Factorial?

The **factorial** of a non-negative integer `n`, written `n!`, is the product of every positive integer from `1` up to `n`.

<div align="center">

### n! = n × (n−1) × (n−2) × … × 2 × 1

| n | n! |
|:-:|:--:|
| 0 | 1 |
| 1 | 1 |
| 2 | 2 |
| 3 | 6 |
| 4 | 24 |
| 5 | 120 |
| 10 | 3,628,800 |

</div>

Factorials show up everywhere — combinatorics, probability, permutations, series expansions — which makes this humble little script surprisingly powerful.

---

## ⚙️ How the Code Works

The script does three things, in order:

1. **Reads** an integer from the user via `input()`.
2. **Branches** on the value of `n`:
   - 🔴 Negative → prints an error message (factorials aren't defined here).
   - 🟡 Zero → prints `1` directly (`0! = 1` by mathematical convention).
   - 🟢 Positive → multiplies its way up from `1` to `n` in a `for` loop.
3. **Prints** the final result.

```python
n = int(input("Enter a number: "))
if n < 0 :
    print("Factorial is not defined for negative numbers.")
elif n == 0 :
    print("Factorial is: 1")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    print("Factorial is:", factorial)
```

Clean, readable, and dependency-free — pure Python standard library, no imports needed.

---

## 🔀 Program Flow

```mermaid
flowchart TD
    A(["🚀 Start"]) --> B["Read integer n"]
    B --> C{"n < 0 ?"}
    C -- "Yes" --> D["❌ Print: not defined for negatives"]
    C -- "No" --> E{"n == 0 ?"}
    E -- "Yes" --> F["✅ Print: Factorial is 1"]
    E -- "No" --> G["🔁 Loop i = 1 → n<br/>factorial *= i"]
    G --> H["✅ Print: Factorial is factorial"]
    D --> I(["🏁 End"])
    F --> I
    H --> I

    style A fill:#2ECC71,stroke:#27AE60,color:#fff
    style I fill:#E74C3C,stroke:#C0392B,color:#fff
    style D fill:#FF6B6B,stroke:#C0392B,color:#fff
    style F fill:#F7C948,stroke:#D4A017,color:#1a1a2e
    style H fill:#4ECDC4,stroke:#1B9C92,color:#1a1a2e
    style G fill:#6C5CE7,stroke:#4834D4,color:#fff
```

> 💡 *GitHub renders Mermaid diagrams natively — this flowchart will animate into view when the README loads.*

---

## 💻 Full Source Code

<details>
<summary><b>Click to expand <code>factorial.py</code></b> 📂</summary>

```python
n = int(input("Enter a number: "))
if n < 0 :
    print("Factorial is not defined for negative numbers.")
elif n == 0 :
    print("Factorial is: 1")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    print("Factorial is:", factorial)
```

</details>

---




</div>

<p align="center"><sub>📸 Screenshots generated from an actual run of <code>factorial.py</code></sub></p>

---

## 🚀 Getting Started

```bash
# 1️⃣ Clone or download this repo
git clone https://github.com/your-username/factorial-calculator.git
cd factorial-calculator

# 2️⃣ Run the script
python3 factorial.py

# 3️⃣ Enter any integer when prompted
Enter a number: 7
Factorial is: 5040
```

**Requirements:** Python 3.6+ — nothing else. No `pip install`, no external packages. 🎉

---

## 🛡️ Edge Cases Handled

| Input | Behavior |
|:-----:|:---------|
| `n < 0` | Prints a friendly error — factorial isn't defined for negatives |
| `n == 0` | Correctly returns `1` (mathematical convention: `0! = 1`) |
| `n > 0` | Computes the product iteratively via a `for` loop |
| Non-integer input | ⚠️ Will raise a `ValueError` — not currently caught |

---

## 📜 License

Released under the **MIT License** — free to use, modify, and share.

<div align="center">

### ⭐ If this helped you understand factorials, consider giving it a star! ⭐


<sub>Made with 🐍 Python and a genuine appreciation for exclamation marks (`n!`)</sub>

</div>
