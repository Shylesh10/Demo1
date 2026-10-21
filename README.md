# Demo1 – Web UI Test Automation Framework (Playwright + Pytest)

A personal project: an end-to-end UI test automation framework built with **Python, Playwright and Pytest**, using the **Page Object Model (POM)** pattern, **parallel execution**, **HTML reporting** and a **Jenkins CI pipeline**.

> **Application under test:** [SauceDemo](https://www.saucedemo.com) – a public demo e-commerce site built for practicing test automation.

---

## Tech Stack

| Area | Tool |
|---|---|
| Language | Python 3.x |
| Browser automation | Playwright (`pytest-playwright`) |
| Test runner | Pytest |
| Parallel execution | `pytest-xdist` |
| Reporting | `pytest-html` (self-contained HTML report) |
| CI/CD | Jenkins (declarative pipeline) |

## Project Structure

```
Demo1/
├── assets/          # Static files (screenshots, upload files, etc.)
├── data/            # Test data (inputs / expected values)
├── pages/           # Page Object classes (locators + page actions)
├── tests/           # Test cases
├── reports/         # Generated HTML reports
├── conftest.py      # Shared fixtures and Pytest configuration
├── Jenkinsfile      # CI pipeline definition
├── requirements.txt # Python dependencies
└── .gitignore
```

## Key Features

- **Page Object Model** – locators and actions live in `pages/`, keeping tests short and maintainable.
- **Data separated from tests** – test data kept in `data/`, so tests can be extended without code changes.
- **Reusable fixtures** – browser/page setup in `conftest.py`.
- **Parallel runs** – faster feedback using `pytest-xdist`.
- **HTML reports** – a single self-contained report generated after every run.
- **CI pipeline** – Jenkins installs dependencies, installs Playwright browsers, runs the suite and publishes the HTML report.

## Getting Started

### Prerequisites
- Python 3.9+
- Git

### Setup

```bash
git clone https://github.com/Shylesh10/Demo1.git
cd Demo1

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
playwright install
```

## Running Tests

```bash
# Run all tests
pytest

# Run with a visible browser
pytest --headed

# Run in parallel (4 workers)
pytest -n 4

# Choose a browser
pytest --browser firefox

# Generate an HTML report
pytest --html=reports/report.html --self-contained-html
```

## CI/CD (Jenkins)

The `Jenkinsfile` defines a two-stage pipeline:

1. **Install Dependencies** – `pip install -r requirements.txt` and `playwright install`
2. **Run Tests** – `pytest --html=reports/report.html --self-contained-html`

After every build (pass or fail), the HTML report is published in Jenkins as **Playwright Test Report**.

## Test Scenarios Covered

<!-- Keep only the scenarios you have actually automated -->
- Login with valid credentials
- Login with invalid credentials and locked-out user (negative tests)
- Product listing and sorting
- Add to cart / remove from cart
- End-to-end checkout flow
- Logout

## Sample Report

<!-- Add a screenshot of reports/report.html here -->
`![Test Report](assets/report-screenshot.png)`

## Author

**Shylesh** – QA / Automation Engineer
GitHub: [@Shylesh10](https://github.com/Shylesh10) · LinkedIn: `<your link>` · Email: `<your email>`