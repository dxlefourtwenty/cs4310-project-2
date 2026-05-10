import parser

def _run_reference_string(reference_string, frame_count):
  frames = [None] * frame_count 
  last_used = [-1] * frame_count

  time = 0
  page_faults = 0

  for page in reference_string:
    time += 1

    found = False
    
    for i in range(0, frame_count):
      if frames[i] == page:
        found = True
        last_used[i] = time
        break

    if found == False:
      page_faults += 1 
      empty_index = -1

      for i in range(0, frame_count):
        if frames[i] == None:
          empty_index = i
          break
      
      if empty_index != -1:
        frames[empty_index] = page
        last_used[empty_index] = time

      else:
        victim_index = 0

        for i in range(1, frame_count):
          if last_used[i] < last_used[victim_index]:
            victim_index = i

        frames[victim_index] = page
        last_used[victim_index] = time

  return page_faults

def _run_algorithm(strings, frame_count):
  page_faults = 0

  for reference_string in strings:
    page_faults += _run_reference_string(reference_string, frame_count)
  
  return page_faults

def run(file_path, frame_count):
  return _run_algorithm(parser.parse_file(file_path), frame_count)
