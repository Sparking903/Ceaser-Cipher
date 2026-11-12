import subprocess

#TestedText = input("Enter the text to be decoded: ")

result = subprocess.run(
    ["ls"],
    capture_output=True,
    text=True,
    check=True
)

print(result.stdout)