import pandas as pd
import scipy.stats
import hashlib
import requests

class Password_Check():
    def dataleak_check(pwd):
        """Checks for the presense of pwd in data leaks and reports the number of findings (if any).

        Args:
            pwd (str): password to check for the presense of in data leaks.

        Returns:
            str: If pwd was found in data leaks, returns message with number of leaks; otherwise, \
                returns message stating the password was not found in data leaks.
        """
        hash = hashlib.sha1(pwd.encode()).hexdigest().upper()
        prefix, suffix = hash[:5], hash[5:]

        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(url)
        leaked_hashes = response.text.splitlines()

        for line in leaked_hashes:
            leak_suffix, count = line.split(":")
            if leak_suffix == suffix:
                return f"We found your password in {count} data leaks! Please choose a different one."
        
        return "Your password was not found in any data leaks"

    def entropy_check(pwd):
        """Checks the entropy of pwd. 

        Args:
            pwd (str): Password to check the entropy of.

        Returns:
            int: Entropy score of pwd. Max values of 6.00, 5.00, 4.00, and 3.00 for passwords of length \
                64, 32, 16, and 8, respectively.
        """
        probs = pd.Series(list(pwd)).value_counts()/sum(pd.Series(list(pwd)).value_counts().values)
        ent = scipy.stats.entropy(probs) # max value of 5.00 for a 32 character password
        return ent

    def check_password(pwd):
        """Driver method. Determines and reports the strength of pwd.

        Args:
            pwd (str): password whose strength is being checked

        Returns:
            str: Message describing the strength/safety of the given password. Max strength score \
                of 6.00, 5.00, 4.00, and 3.00 for passwords of length 64, 32, 16, and 8, respectively.
        """
        leak_status = Password_Check.dataleak_check(pwd)
        if ("We" in leak_status[:2]):
            return leak_status
        ent = Password_Check.entropy_check(pwd)

        return f"{leak_status} and has an strength score of {ent}"

if __name__ == "__main__":
    pwd = input("Enter password:")
    print(Password_Check.check_password(pwd))