import parser

def _run_reference_string(reference_string, frame_count):
  frames = [None] * frame_count
  pointer = 0
  page_faults = 0

  for page in reference_string:
    found = False

    for i in range(0, frame_count):
      if frames[i] == page:
        found = True
        break

    if found == False:
      page_faults += 1
      frames[pointer] = page
      
      pointer = (pointer + 1) % frame_count

  return page_faults

def _run_algorithm(strings, frame_count):
  page_faults = 0

  for reference_string in strings:
    page_faults += _run_reference_string(reference_string, frame_count)

  return page_faults

def run(file_path, frame_count):
  return _run_algorithm(parser.parse_file(file_path), frame_count)
