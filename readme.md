# 🚀 Numeral System Converter (Any Base ↔ Any Base)A **Python-based numeral system converter** that allows conversion between **any base (2 to 36)**, including support for **fractional numbers**.

This project demonstrates core concepts of **number systems, base conversions, and floating-point handling**, making it useful for **students, developers, and digital electronics learners**.

---

## 📌 Features

- 🔄 Convert **any base → any base**
- 🔢 Supports bases from **2 to 36**
- 🧮 Handles both:
  - Integer values
  - Fractional values (up to fixed precision)
- ⚡ Lightweight and fast (no external dependencies)
- 🧠 Clean logic for learning and understanding number systems

---

## 🛠️ Tech Stack

- **Language:** Python 3  
- **Concepts Used:**
  - Number System Conversion
  - Positional Notation
  - Floating Point Arithmetic
  - String Manipulation

---

## 📂 Project Structure
📁 numeral-system-converter/
│── main.py # Main conversion logic
│── README.md # Documentation


---

## ⚙️ How It Works

The conversion is done in **two steps**:

1. **Source Base → Decimal**
2. **Decimal → Target Base**

---

## 🔑 Core Functions

### 1. `dec_to_any_base(num, base)`
Converts a **decimal number → any base**

- Handles integer + fractional parts  
- Uses repeated division (integer part)  
- Uses repeated multiplication (fractional part)  

---

### 2. `any_base_to_decimal(num_str, base)`
Converts a **number from any base → decimal**

- Validates digits based on base  
- Uses positional power expansion  

---

### 3. `convert_any_to_any(num_str, from_base, to_base)`
Main function that:

- Converts from source base → decimal  
- Then decimal → target base  

---

## ▶️ Usage

```python
print("Binary '1010.101' to Hex:", convert_any_to_any("1010.101", 2, 16)) 
print("Hex 'A' to Octal:", convert_any_to_any("A", 16, 8))               
print("Decimal '15' to Binary:", convert_any_to_any("15", 10, 2))