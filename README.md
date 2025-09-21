# Object Oriented Programming (OOP) Repository

This repository contains multiple projects and exercises demonstrating **Object-Oriented Programming (OOP)** concepts in Python. The projects range from implementing basic data structures to graphical applications and simulations.  

---

## Table of Contents

1. [Turtle Functionality](#turtle-functionality)  
2. [List Operations](#list-operations)  
3. [Range Function](#range-function)  
4. [Shape Drawing](#shape-drawing)  
5. [Vector Calculations](#vector-calculations)  
6. [Week 9 Topics](#week-9-topics)  
7. [Week 11 Topics](#week-11-topics)  

---

## Turtle Functionality

This project demonstrates a **Turtle graphics system** using OOP principles. It uses `Tkinter` for the UI and organizes functionality into multiple modules:

### Folder Structure

- **App**
  - `app.py`: The engine to run turtle commands.
- **Geometry**
  - `point.py`: Represents a point in 2D space.
  - `line.py`: Represents a line formed from two points.
- **Drawing**
  - `pen.py`: Uses `Canvas` and `Point` to draw shapes.
  - `canvas.py`: Uses `Point` and `Line` with `Tkinter` UI to draw.
- **Turtle**
  - `turtle.py`: Implements the Turtle with forward, right, and left movements.
  - `command.py`: Handles turtle commands, includes subclasses for `SquareCommand` and `ZigZagCommand`.

### Execution

- **Main File:** `main_app.py` (outside folders)  
  This file initializes the app engine and runs turtle commands using `Tkinter`.

---

## List Operations

This folder demonstrates OOP usage in managing lists and collections:

- `general_list.py`: General list operations using OOP.  
- `main_cars.py`: Main program managing a car list.  
- `garage_list.py`: Represents a garage storing multiple cars.  
- `cars_list.py`: Handles car-related list operations.

---

## Range Function

Demonstrates working with the Python `range()` function:

- `range.py`: Custom range implementation using classes.  
- `main_range.py`: Demonstrates usage and iteration over the custom range.

---

## Shape Drawing

Shows OOP applied to geometric shapes and drawing:

- `circle.py`: Draws a circle using `Point` and `Pen`.  
- `square.py`: Draws a square using `Point` and `Pen`.  
- `triangle.py`: Draws a triangle using `Point` and `Pen`.  

**Execution:**  
- `main_shape.py` (outside folder) runs the shape drawing examples.

---

## Vector Calculations

Implements vector operations and calculations using OOP:

- `vector.py`: Defines vector operations and properties.  
- `main_vector.py`: Demonstrates calculations and vector usage.

---

## Week 9 Topics

### Birthday Paradox

- Folder: `birthday_paradox`  
- Demonstrates probability concepts using OOP.  

### Word Frequency Counter

- Folder: `word_frequency_counter`  
- Implements a word frequency counter using OOP principles.

---

## Week 11 Topics

### Change Calculator

- Folder: `change_calculator`  
- Implements a system to calculate change for transactions using classes.

---

## Requirements

- Python 3.x  
- Tkinter (for Turtle and Shape projects)

---

## How to Run

1. Navigate to the project folder.  
2. Run the main file for the desired module. For example:

```bash
python main_app.py       # Runs the Turtle project
python main_shape.py     # Runs Shape drawing project
python main_vector.py    # Runs Vector calculations
