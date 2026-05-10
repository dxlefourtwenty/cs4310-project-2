import random

file_path = "job_files/testingdata.txt"

data_lines = 30

def generate():
  with open(file_path, "w") as f:
    for i in range(1, data_lines + 1):
      string = ''.join(random.choices('01234567', k=30))
      f.write(f"{string}\n")

if __name__ == "__main__":
  generate()


