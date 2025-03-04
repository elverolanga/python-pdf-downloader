import os
import requests

urls = [
]

output_dir = './dwnl'

for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        file_path = os.path.join(output_dir, os.path.basename(url))
        with open(file_path, 'wb') as f:
            f.write(response.content)
