# file reader for main()
def parse_file(file_path):

  strings = []

  try:
    with open(file_path, 'r') as file: 
      lines = [line.strip() for line in file]

    for i in range(0, len(lines)):
      string = lines[i]
      strings.append(string)

  except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
  except Exception as e:
    print(f"An error occured: {e}")

  return strings
