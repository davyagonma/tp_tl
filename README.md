Parfait Davy 🔥 Voici un **README bilingue (🇬🇧 English / 🇫🇷 Français)** complet, structuré, clair et professionnel pour documenter ton projet Streamlit sur les **machines de Turing multitêtes, multi-rubans, déterministes et non-déterministes** (Exercices 7 à 10).

---

## 📄 `README.md`

````markdown
# 🧠 Turing Machine Simulator – Multi-tape, Nondeterministic & Arithmetic MT

This project is a pedagogical simulator implemented with **Streamlit** to explore advanced Turing Machine concepts through interactive examples.

🎓 Designed to support Exercises 7–10 from a theoretical computer science curriculum.

---

## 🇬🇧 Features

- ✅ Palindrome recognition using 1-tape & 2-tape Turing Machines  
- ➕ Arithmetic operations (unary) with simulated MT (Add/Sub/Mul/Div)  
- 🧩 Universal MT and multitape simulation  
- 🌀 Nondeterministic Turing Machine (with backtracking)  
- 📊 Visual comparison of time/complexity for 1-tape vs multi-tape machines  

---

## 🇫🇷 Fonctionnalités

- ✅ Reconnaissance de palindromes avec MT à 1 ou 2 rubans  
- ➕ Calculatrice en unaire : addition, soustraction, multiplication, division  
- 🧩 Simulateur de machine universelle multitête  
- 🌀 Machine de Turing non-déterministe avec backtracking  
- 📊 Comparaison des performances (temps, complexité) entre MT à 1 et k rubans  

---

## 🚀 How to launch / Lancer le simulateur

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
````

---

## 📁 Project Structure / Structure du projet

```bash
.
├── app.py             # Main Streamlit interface
├── simulators/
│
├── requirements.txt
└── README.md
```

---

## 🧪 Example Inputs / Exemples à tester

### 🔄 Palindromes

| Input  | Result |
| ------ | ------ |
| `abba` | ✅      |
| `abab` | ❌      |

### ➕ Unary Arithmetic

| Input     | Operation      | Output                    |
| --------- | -------------- | ------------------------- |
| `111#11`  | Addition       | `11111`                   |
| `111#11`  | Subtraction    | `1`                       |
| `11#111`  | Multiplication | `111111`                  |
| `1111#11` | Division       | `Quotient: 11` `Reste: 0` |

### 🧩 L = {w#w}

| Input     | Result |
| --------- | ------ |
| `101#101` | ✅      |
| `110#011` | ❌      |

### 📊 Sorting (input: space-separated integers)

```txt
Input: 5 1 4 2  
Output: 1 2 4 5
```

---

## 📘 Use case / Cas d’usage

* 🏫 Educational Turing Machine playground
* 📚 Support for theoretical CS assignments
* 🧠 Deep dive into multitape vs single-tape Turing complexity
* 🎓 Suitable for oral presentations / soutenances

---

## 🧾 License

MIT – Free to use, modify, and distribute.

---

## ✨ Authors / Auteurs

**Davy Agonma & Priscille Dona**
Projet développé dans le cadre d’un TP avancé en théorie des langages et des automates.

```

