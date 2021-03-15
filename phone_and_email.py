import re
import pyperclip

#sablon numar telefon 0745987654 (\d\d\d\d\d\d\d\d\d\d)
# 021 314 34 00  (\s|-)

phoneRegex = re.compile(r'''

\d[-/\s]?
\d[-/\s]?
\d[-/\s]?
\d[-/\s]?
\d[-/\s]?
\d[-/\s]?
\d[-/\s]?
\d[-/\s]?
\d[-/\s]?
\d


    ''', re.VERBOSE)

text = pyperclip.paste()

emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+
@
[a-zA-Z0-9_.+]+

    ''', re.VERBOSE)

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

result = '\n'.join(extractedPhone) + '\n' + '\n' + '\n'.join(extractedEmail)

pyperclip.copy(result)

