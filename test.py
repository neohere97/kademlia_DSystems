txt = "Key '00048a5c76.jpg' has value 'http://localhost:9000/file/00048a5c76.jpg'"

import re
# find the url from the txt
url = re.findall(r'(\'http?://\S+)', txt)[0]
print(url)