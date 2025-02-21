### Overview ###
This code defines a simple password strength checker that checks for the given password's presence in data leaks via the [Pwned Password API](https://haveibeenpwned.com/API/v3) and it's randomness.\
Feel free to copy and use this code as is, or as a starting point for a more complex password checker, but please comply with the GNU General Public License detailed in the LICENSE.md file in this repository. 
Included is a driver method that will check both of these criteria and return an informative message. It may also be run through the command line and will prompt users for a password before checking password strength.\
**Running a password through this program does not guarantee that the password is strong.** This tool is meant for educational use and provides simple, but **not definitive** feedback on the strength of a password by checking it against a collection of leaked passwords and mathematically computing the entropy of the password.

### Dependencies ###
This code uses `pandas`, `scipy`, `hashlib`, and `requests` which can each be installed using `pip`:\
`
pip install pandas scipy hashlib requests
`

