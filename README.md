# sendMail

A utility to send email from the Windows command line. (Not to be confused with [Sendmail](https://en.wikipedia.org/wiki/Sendmail))

Builds with [pyinstaller](https://github.com/pyinstaller/pyinstaller).

## Installation:
Fork or clone the repo and execute `build.cmd` to build the executable.
## Usage:
Sends an email via Outlook

`sendMail [-h] [--cc CC] [--attachments ATTACHMENTS] [--edit] --to TO --subject SUBJECT --body BODY`

Parameter | Usage
----|-----
-h, --help | Shows help message and exits
--to | Recipients (semicolon delimited)
--cc | CC recipients (semicolon delimited)
--subject | Email subject line
--body | Email body
--attachments | Attachment paths (semicolon delimited)
--edit | Open draft instead of immediately sending

To, subject, and body are required.

Returns 0 on success or 1 on failure

## License:
Distributed under the MIT License. See [`LICENSE.txt`](https://github.com/scgrn/sendMail/blob/main/LICENSE) for more information.

## Contact:
Andrew Krause - ajkrause@gmail.com

Project Link: [https://github.com/scgrn/sendMail](https://github.com/scgrn/sendMail)
