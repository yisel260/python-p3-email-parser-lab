# your code goes here!
import re 


class EmailAddressParser:

    def __init__(self, emails):
        self.emails = emails

    def parse(self):
         
        addresses = re.split(r'\s*[,]\s*|\s', self.emails)
        addresses = [address.strip() for address in addresses]  
        valid_addresses = []
        for address in addresses:
            if re.match(r'[A-z]([A-z0-9][\.]{0,1})+[A-z0-9]+@[A-z0-9]+\.[a-z]{2,}', address):
                    valid_addresses.append(address)
        valid_addresses = list(set(valid_addresses))
        valid_addresses.sort()
        return valid_addresses

