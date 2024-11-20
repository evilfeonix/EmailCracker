![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg) 


![EvilFeonix Basic v1.0](https://github.com/evilfeonix/EvilFeonix-Basic/blob/main/basic_setup.png)

# EmailCracker

# EmailCracker (Educational Use Only)

**EmailCracker** is a security testing tool designed for educational purposes. It demonstrates how attackers might attempt to crack email passwords through ethical and responsible penetration testing. The tool is designed for users to test the security of their own accounts or those they have explicit permission to test. 

> **Important: This tool should **only** be used on accounts that you own or have explicit written consent to test. Unauthorized use of this tool on accounts you do not own or have permission to test is illegal and unethical.**

## Disclaimer

This tool is intended **for educational purposes only** and should be used responsibly. By using this tool, you agree to comply with all applicable laws and regulations. Do not use this tool for illegal activities or without the explicit consent of the account holder.

## Features

- **Email Configuration**: The tool uses an easily configurable `config.ini` file where users can specify the email service provider's host and port.
- **Generate list of Passwords**: generate list of passwords based on the information it collecated.
- **Password Cracking Simulation**: Simulates a password cracking process using common attack methods like dictionary or brute force.
- **Educational Purpose**: Helps users understand how email systems might be tested for security weaknesses.

## Prerequisites

Before running **EmailCracker**, ensure you have the following:

- Python 3.x or above
- Required Python libraries (can be installed using `pip`)

## Setup
### Clone the Repository

```bash
git clone https://github.com/evilfeonix/EmailCracker.git
cd EmailCracker
```
## Configure the Tool (config.ini)

The tool requires the configuration of the `config.ini` file before use. The configuration file allows you to specify the email provider's host and port.

The default configuration in `config.ini` is set up for Gmail, but you can modify these settings to test other email providers (such as Yahoo, Outlook, etc.).

### Example config.ini for Gmail:

```ini
[SMTP]
host = smtp.gmail.com
port = 587
```

If you're testing with a different provider, replace the host and port with the appropriate values.

## Install Dependencies

If you haven't already, you can install all the necessary Python dependencies:

## Run the Tool

After configuring the config.ini file, run the tool by passing in the target email address:
```bash
python3 cracker.py
```

## Monitor the Cracking Process

The tool will log its attempts to find the correct password, simulating a password guessing attack (brute force or dictionary). If the password is found, it will be displayed in the output.


### Legal Disclaimer
> By using this tool, you agree that you will not attempt to access email accounts without permission. Any unauthorized use of this tool is illegal and may result in criminal charges.

The creators of this tool are not responsible for any misuse or damage caused by its usage.

### License

This project is licensed under the GPL License - see the LICENSE file for details.
