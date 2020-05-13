#! /usr/bin/env python3

import settings
import email_tools

def main():
    matched = False
    choice = input("Choose the email type {}: ".format(list(settings.email_types.keys())))

    for (email_type, keywords) in settings.email_types.items():
        if choice in keywords:
            email_tools.send(email_type)
            matched = True
    
    if not matched:
        print("Invalid Choice.")

if __name__ == '__main__':
    main()