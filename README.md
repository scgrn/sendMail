#sendMail

A utility to send email from the Windows command line.
Builds with [pyinstaller](https://github.com/pyinstaller/pyinstaller).

(Not to be confused with [Sendmail](https://en.wikipedia.org/wiki/Sendmail))

##Installation:
Fork or clone the repo and execute `build.cmd` to build the executable.
##Usage:
`sendMail [-h] [--cc CC] [--attachments ATTACHMENTS] [--edit] --to TO --subject SUBJECT --body BODY`

Sends an email via Outlook

optional arguments:
  -h, --help            shows help message and exits
  --cc CC               CC recipients (semicolon delimited)
  --attachments ATTACHMENTS
                        attachment paths (semicolon delimited)
  --edit                open draft instead of immediately sending
  --to TO               recipients (semicolon delimited)
  --subject SUBJECT     email subject
  --body BODY           email body

Returns 0 on success or 1 on failure

##License:
Distributed under the MIT License. See [`LICENSE.txt`](LICENSE.txt) for more information.

##Contact:
Andrew Krause - ajkrause@gmail.com

Project Link: [https://github.com/scgrn/sendMail](https://github.com/scgrn/sendMail)
