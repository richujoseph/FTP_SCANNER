# Anonymous FTP Scanner

This project is a simple web application built with Flask that checks if anonymous FTP login is allowed for a given target. The application attempts to connect to the target's FTP service and logs in using the `anonymous` user credentials. It then provides feedback on whether the FTP service allows anonymous access or not.

## Features

- **Check anonymous FTP access:** Enter a domain or IP address to check if it allows anonymous FTP login.
- **Web Interface:** A simple form where users can input a target domain or IP address and receive results on the web page.
- **Error Handling:** The app gracefully handles errors like invalid hostnames and unreachable targets.

## Requirements

- Python 3.x
- Flask
- `ftplib` (standard library)
- `socket` (standard library)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/anonymous-ftp-scanner.git
    ```

2. Navigate to the project folder:

    ```bash
    cd anonymous-ftp-scanner
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your browser and go to `http://127.0.0.1:5000/`.

3. Enter a domain or IP address in the provided form and click on the "Check" button to see the results.

## How It Works

The application uses the Python `ftplib` library to connect to the FTP service of the provided target. The following checks are performed:

- **Anonymous FTP Login:** The application attempts to log in using `anonymous` as the username and `anonymous` as the password. If successful, it will indicate that anonymous FTP access is allowed.
- **Access Denied:** If the login attempt is denied, it will show that access is denied.
- **No FTP Service:** If no FTP service is detected, it will display that the target does not have FTP services running.

## Example

- If the target is a valid FTP server that allows anonymous login:
    ```
    target: ftp.example.com
    result: Anonymous FTP Allowed
    ```
  
- If the target denies anonymous login:
    ```
    target: ftp.example.com
    result: Access Denied
    ```

- If the target does not have an FTP service running:
    ```
    target: ftp.example.com
    result: No FTP Service
    ```

## Contributing

If you want to contribute to this project, feel free to fork it and submit a pull request with your improvements.

## License

This project is open-source and available under the MIT License.

