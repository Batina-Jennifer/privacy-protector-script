# 🔒 Automated PII(Personally Identifiable Information) Masking Tool

A Python-based security automation script designed to protect user privacy by anonymizing sensitive data in CSV files.

## 🚀 The Challenge
In a high-growth engineering environment, developers need realistic data to test features. However, using real Production data (PII) is a significant security and compliance risk. 

## 🛠️ The Solution
Data masking is one of the strategies mentioned in CompTIA Security+ books to hide sensitive information. This tool creates a "Security Layer" between production data and development environments. Using **Pandas** and **Faker**, it:
1. **Extracts** raw data from a CSV.
2. **Transforms** sensitive columns (Names, Emails) into realistic "synthetic" data.
3. **Maintains** data utility while ensuring 100% anonymity.

## 🧪 Technical Stack
* **Python 3**
* **Pandas**: For high-performance data manipulation.
* **Faker**: For deterministic synthetic identity generation.

## 📖 How to Run
1. Install dependencies:
   ```bash
   pip install pandas faker
