# MLOps — Lab 1 Submission

## Student Information
- **Name:** Sushritha Bharadwaj  
- **Course:** MLOps  
- **Lab:** Lab 1 — Testing and Continuous Integration

---

## Project Overview

This project implements basic statistical utility functions in Python and demonstrates automated testing and Continuous Integration (CI) using GitHub Actions.

The main goal of this lab is to practice:
- Writing unit tests
- Using pytest and unittest
- Setting up CI pipelines
- Managing code using GitHub

---

## Implemented Features

### Statistical Utilities (`src/stats_utils.py`)
The following functions were implemented:

- `mean(data)` — Computes the average of a list of numbers
- `variance(data)` — Computes the variance
- `std_dev(data)` — Computes the standard deviation
- `summary_stats(data)` — Returns all statistics together

---

### Testing

Two testing frameworks were used:

#### 1. Pytest (`test/test_pytest.py`)
- Tests all statistical functions
- Validates correct outputs for sample inputs

#### 2. Unittest (`test/test_unittest.py`)
- Implements class-based unit tests
- Tests the `mean` function

All tests pass successfully.

---

### Continuous Integration (CI)

GitHub Actions was configured to automatically run tests on every push and pull request.

Two workflows were created:

- `pytest_action.yml` — Runs pytest tests
- `unittest_action.yml` — Runs unittest tests

These workflows ensure that the code is automatically validated before integration.

---

## Modifications from Starter Repository

Compared to the original template repository, the following changes were made:

- Replaced the calculator example with a custom `stats_utils` module
- Implemented statistical functions instead of arithmetic operations
- Added comprehensive tests using both pytest and unittest
- Created separate GitHub Actions workflows for each test framework
- Added project documentation in this README file

These modifications make the project unique and demonstrate independent implementation.

---
