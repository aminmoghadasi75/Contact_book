from typing import Dict, Optional

from tabulate import tabulate
from termcolor import colored, cprint


class ContactBook:
    """ContactBook: Build Your Personal Contact Book

    A contact book that can be used to store contact information for a user.
    """
    def __init__(self) -> None:
        self.contacts: Dict[str, Dict[str, Optional[str]]] = {}

    def add_contact(self, *, name: str, phone_number: Optional[str] = None, email: Optional[str] = None, additional_information: str) -> None:
        """
        Adds a contact to the contact list.

        Args:
            name (str): The name of the contact.
            phone_number (str, optional): The phone number of the contact. Defaults to None.
            email (str, optional): The email of the contact. Defaults to None.
            **kwargs: Additional information to be stored for the contact.

        Returns:
            None
        """
        if name in self.contacts:
            print(colored(f'{name} already exists!', 'red', attrs=["reverse", "blink"]))
        else:
            user_information = {
                'Phone Number': phone_number,
                'Email': email,
                'Additional Information' : additional_information # Store additional information
            }
            self.contacts[name] = user_information
            print(colored(f'{name} has been added successfully!' , 'green', attrs=["reverse", "blink"]))

    def view_contacts(self) -> None:
        """
        Displays the list of contacts with their information.

        Returns:
            None
        """
        print(colored('List of contacts:', 'green', attrs=["reverse", "blink"]))
        table = [ ]
        headers = ["Name", "Phone Number", "Email", "Additional Information"]
        for name, information in self.contacts.items():
            table.extend([[name, information.get("Phone Number", ""), information.get("Email", ""),information.get("Additional Information", "")]])
        print(tabulate(table, headers=headers, tablefmt="pretty"))

    def search_contact(self, *, name: str) -> Optional[Dict[str, Optional[str]]]:
        """
        Search for a contact by name in the contact dictionary.

        Parameters:
            name (str): The name of the contact to search for.

        Returns:
            dict or None: The contact information if found, otherwise None.
        """
        headers = ["Name", "Phone Number", "Email", "Additional Information"]
        if name in self.contacts:
            phone_number = self.contacts[name]["Phone Number"]
            email = self.contacts[name]["Email"]
            add_info = self.contacts[name]["Additional Information"]
            table=[name, phone_number, email, add_info]
            print(tabulate(table, headers=headers, tablefmt="pretty"))
        else:
            print(colored(f'{name} not found!' , 'red', attrs=["reverse", "blink"]))
            return None

    def delete_contact(self, *, name: str) -> bool:
        """
        Deletes a contact from the contact list.

        Parameters:
            name (str): The name of the contact to delete.

        Returns:
            bool: True if the contact is found and deleted, otherwise False.
        """
        if name in self.contacts:
            del self.contacts[name]
            print(colored(f'{name} has been deleted successfully!', 'green', attrs=["reverse", "blink"]))
            return True
        else:
            print(colored(f'{name} not found!', 'red', attrs=["reverse", "blink"]))
            return False

    def update_contact(self, *, name: str, phone_number: Optional[str] = None, email: Optional[str] = None, **kwargs: str) -> bool:
        """
        Updates the contact information for a given contact name.

        Parameters:
            name (str): The name of the contact to update.
            phone_number (str, optional): The new phone number for the contact. Defaults to None.
            email (str, optional): The new email address for the contact. Defaults to None.
            **kwargs: Additional information to update for the contact.

        Returns:
            bool: True if the contact is found and updated, otherwise False.
        """
        if name in self.contacts.keys():
            if phone_number:
                self.contacts[name]['Phone Number'] = phone_number
            if email:
                self.contacts[name]['Email'] = email
            # Update additional information
            for key, value in kwargs.items():
                self.contacts[name][key] = value
            print(colored(f'{name} has been updated successfully!', 'green', attrs=["reverse", "blink"]))
            return True
        else:
            print(colored(f'{name} not found!', 'red', attrs=["reverse", "blink"]))
            return False
if __name__ == '__main__':
    print(colored('Welcome to ContactBook!', 'yellow', attrs=["reverse", "blink"]))
    book = ContactBook()

    while True:
        headers = ["Number", "Action"]
        table= [["1", "Add Contact"], ["2", "View Contacts"], ["3", "Search Contact"], ["4", "Delete Contact"], ["5", "Update Contact"], ["6", "Exit"]]
        print(tabulate(table, headers, tablefmt="github"))

        user_input = input('Enter your choice: ')

        if user_input not in ['1', '2', '3', '4', '5', '6']:
            print('Please enter a valid choice!')
            continue

        user_input = int(user_input)

        if user_input == 1:
            name = input('Enter name: ')
            phone_number = input('Enter phone number: ')
            email = input('Enter email: ')
            additional_information = input('Enter any additional information: ')
            book.add_contact(name=name, phone_number=phone_number, email=email, additional_information=additional_information)

        elif user_input == 2:
            book.view_contacts()

        elif user_input == 3:
            name = input('Enter name: ')
            contact_info = book.search_contact(name=name)
            if contact_info:
                print('Contact Information:', contact_info)

        elif user_input == 4:
            name = input('Enter name: ')
            deleted = book.delete_contact(name=name)
            if deleted:
                print(f'{name} has been deleted.')

        elif user_input == 5:
            name = input('Enter name: ')
            phone_number = input('Enter phone number: ')
            email = input('Enter email: ')
            additional_information = input('Enter any other information: ')
            updated = book.update_contact(name=name, phone_number=phone_number, email=email, additional_information=additional_information)
            if updated:
                print(f'{name} has been updated.')

        elif user_input == 6:
            print(colored('Thank you for using our ContactBook!', 'yellow', attrs=["reverse", "blink"]))
            break

