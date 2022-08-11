#   2021.04.02
#   andrew.krause

import argparse
import win32com.client as win32
import sys

def main():
    parser = argparse.ArgumentParser(description = "Sends an email via Outlook", epilog="Returns 0 on success or 1 on failure")

    parser.add_argument('--to', required=True, help='recipients (semicolon delimited)')
    parser.add_argument('--subject', required=True, help='email subject')
    parser.add_argument('--body', required=True, help='email body')

    parser.add_argument('--cc', help='CC recipients (semicolon delimited)')
    parser.add_argument('--attachments', help='attachment paths (semicolon delimited)')
    parser.add_argument('--edit', action="store_true", help='open draft instead of immediately sending')

    args = parser.parse_args()

    try:    
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = args.to
        mail.Subject = args.subject
        mail.Body = args.body

        if (args.cc):
            mail.CC = args.cc

        if (args.attachments):
            attachments = args.attachments.split(';')
            for attachment in attachments:
                mail.Attachments.Add(attachment)

        if (args.edit):
            mail.Display(True)
        else:
            mail.send
    except:
        print("Error")
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()

