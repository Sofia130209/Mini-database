# Add a New Person - Tkinter Application

## Overview
This project is a simple graphical user interface (GUI) application built with Python's Tkinter library. It allows users to enter personal information and save it to a JSON file. Users can also view the saved data in a separate window and clear the input fields for new entries.

## Features
- **Add New Person**: Input fields to enter details such as surname, first name, age, email, and address. The data is saved in a JSON file.
- **View Database**: Opens a new window displaying the saved data in a tabular format.
- **Clear Fields**: Clears the input fields for new entries.
- **Save Confirmation**: Displays a confirmation message when the data is successfully saved.

## Prerequisites
- Python 3.x
- Tkinter library (comes pre-installed with Python)
- JSON library (comes pre-installed with Python)

## Usage
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/add-new-person-tkinter.git
   cd add-new-person-tkinter
   ```

2. **Run the application**:
   ```bash
   python main.py
   ```

3. **Adding a New Person**:
   - Fill in the fields (Surname, First Name, Age, Email, Address).
   - Click the "Add a new person" button to save the data.
   - A confirmation message will appear indicating the data was successfully saved.

4. **Viewing the Database**:
   - Click the "View Database" button.
   - A new window will open displaying the saved data in a table.

5. **Clearing the Fields**:
   - Click the "Clear" button to clear all input fields for new entries.

## Project Structure
- **main.py**: The main script containing the GUI and functionalities.
- **images/**: Directory containing icon files used in the application.
- **_user.json**: JSON file where the data is saved.

## Screenshots
![Add a New Person](path-to-screenshot.png)
![View Database](path-to-screenshot.png)

## Contributing
If you want to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Short Description
This project is a Tkinter-based GUI application for adding personal details such as surname, first name, age, email, and address to a JSON file. Users can view the saved data in a tabular format, clear input fields, and receive confirmation messages upon successful data entry.
