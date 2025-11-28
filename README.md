# Password Manager 🛡️

![Python](https://img.shields.io/badge/Python-3.13-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange)

A **GUI-based Password Manager** built with Python and Tkinter.  
Easily generate secure passwords, save login credentials, and retrieve them with a search function. Passwords are automatically copied to the clipboard.

---

## 🎯 Features

- Generate **secure, random passwords** with letters, numbers, and symbols.
- **Copy password automatically** to clipboard using `pyperclip`.
- **Save login credentials** (website, email/username, password) to a JSON file.
- **Search for saved credentials** quickly.
- Interactive **Tkinter GUI** with input fields and buttons.
- Input validation for empty fields and proper email format.
---

## 💻 Installation
```bash
**Clone the repository**
git clone https://github.com/your-username/password-manager.git
cd password-manager

**Create and activate a virtual environment (recommended)**
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
.\.venv\Scripts\activate   # Windows

**Install dependencies**
pip install pyperclip

tkinter and json come with Python, no installation required.
```
---
🚀 Usage

1. Run the application:
```bash
python main.py
```
2. Enter website, email/username, and password.
3. Use Generate Password button to create a strong random password.
4. Click Add to save credentials to details_data.json.
5. Use Search to retrieve saved credentials for a specific website.
---
📂 Project Structure
```bash
Password_manager/
│── main.py              # Main GUI application
│── password.py          # PasswordGenerator class
│── logo.png             # App logo
│── details_data.json    # JSON file to store credentials
│── .venv/               # Virtual environment (optional)
```
---

🛠 Technologies Used
1. Python 3.x
2. Tkinter (GUI)
3. JSON (data storage)
4. Pyperclip (clipboard functionality)
---

🔮 Future Improvements
1. Encrypt stored passwords for enhanced security.
2. Add password strength meter.
3. Add ability to update or delete saved credentials.
4. Export/Import credentials for backup.
5. Dark mode for GUI.
---

👤 Author
Rachit Basnet
📧 rachitbasnet184@gmail.com
