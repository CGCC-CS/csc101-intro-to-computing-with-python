# Introduction to Classes & Objects

## Objectives

- Defining a class
- Creating objects (instances) from a class
- The `__init__` constructor and `self`
- Instance attributes vs. class attributes
- Writing and calling methods
- Inheritance: creating a child class and calling the parent constructor with `super()`

## Example code

### [class.py](./class.py)

The simplest possible class: a class with a constructor (`__init__`) that stores two attributes with default values

### [attributes.py](./attributes.py)

A `BankAccount` class showing the difference between class attributes (shared by every object) and instance attributes (unique to each object)

### [animals.py](./animals.py)

An `Animal` class with `Dog` and `Cat` child classes. Shows inheritance, calling the parent constructor with `super().__init__()`, overriding methods, and adding a new method (`fetch()`) to a child class.

## Related class examples

- [Spring 2026 Module 10 - Classes](../../classexamples/spring2026/csc101_s26_module_10_classes.py)
