import os

def create_files():
    for i in range(5):
        file_name = f"virus.inject"
        with open(file_name, "wb") as f:
            f.write(b'\x00' * (size_in_mb * 1024 * 1024))

size_in_mb = 200
create_files()
print("Your device killed by virus")
 