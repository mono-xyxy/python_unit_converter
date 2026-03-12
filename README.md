# 🔄 Simple Unit Converter (Python)

A beginner-friendly Python program that converts:

* **Kilometers → Miles**
* **Kilograms → Pounds**

This project demonstrates basic Python concepts such as:

* User input
* Conditional statements
* Mathematical calculations

---

## 📌 Features

* Convert **Kilometers to Miles**
* Convert **Kilograms to Pounds**
* Simple command-line interface
* Lightweight beginner project

---

## 📂 Project Structure

```
unit-converter
│
├── main.py
└── README.md
```

---

## 🛠 Requirements

* Python **3.x**
* No external libraries required

---

## 🚀 How to Run

1. Clone the repository

```
git clone https://github.com/yourusername/unit-converter.git
```

2. Go to the project folder

```
cd unit-converter
```

3. Run the program

```
python main.py
```

---

## 💻 Example Code

```python
print("Simple Unit Converter")
print("1. KM to Miles")
print("2. KG to Pounds")

choice = input("Choose an option (1-2): ")

if choice == "1":
    km = float(input("Enter kilometers: "))
    miles = km * 0.621371
    print("Miles:", miles)

elif choice == "2":
    kg = float(input("Enter kilograms: "))
    lbs = kg * 2.20462
    print("Pounds:", lbs)

else:
    print("Invalid choice")
```

---

## 🧪 Example Output

```
Simple Unit Converter
1. KM to Miles
2. KG to Pounds

Choose an option (1-2): 1
Enter kilometers: 10

Miles: 6.21371
```

---

## 📚 What You Learn

* Python **input/output**
* **if–elif conditions**
* Basic **unit conversion math**

---

## 📜 License

This project is open-source and available under the **MIT License**.
