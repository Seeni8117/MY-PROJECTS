right="recorse/msg.txt"
wrong="recorse/msg1.txt"

try:
    with open(right,"r") as file:
        lines=file.read()
        print(lines)
except(FileNotFoundError):
        print("file not found")
