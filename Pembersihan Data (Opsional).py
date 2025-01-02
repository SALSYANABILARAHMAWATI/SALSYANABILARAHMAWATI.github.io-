import re

with open("data_group.txt", "r") as file:
    data = file.read()

# Pembersihan data
cleaned_data = re.sub(r'[^a-zA-Z0-9.,!? ]', '', data)

with open("cleaned_data_group.txt", "w") as file:
    file.write(cleaned_data)
