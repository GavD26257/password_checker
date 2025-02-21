### Overview ###
This code defines a simple password strength checker that checks for the given password's presence in data leaks via the [Pwned Password API](https://haveibeenpwned.com/API/v3) and it's randomness.\
Feel free to copy and use this code, but please comply with the license in the LICENSE.md file in this repository. 
Included is a driver method that will check both of these criteria and return an informative message. It may also be run through the command line and will prompt  users for a password before checking password strength.\
**This does not guarantee that a password is strong.** This tool is simply for educational use and provides simple, but **not definitive** feedback on the strength of a password.

### Dependencies ###
This code uses `pandas`, `scipy`, `hashlib`, and `requests` which can each be installed using `pip`:\
`
pip install pandas scipy hashlib requests
`

