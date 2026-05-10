import parser

def _run_reference_string(reference_string, frame_count):
  frames = [None] * frame_count
  page_faults = 0

  for current_index in range(0, len(reference_string)):
    current_page = reference_string[current_index]

    found = False

    for i in range(0, frame_count):
      if frames[i] == current_page:
        found = True
        break

    if found == False:
      page_faults = page_faults + 1
      empty_index = -1

      for i in range(0, frame_count):
        if frames[i] == None:
          empty_index = i
          break

      if empty_index != -1:
        frames[empty_index] = current_page

      else:
        victim_index = -1
        farthest_use = -1

        for i in range(0, frame_count):
          next_use = float('inf')

          for j in range(current_index + 1, len(reference_string)):
            if reference_string[j] == frames[i]:
              next_use = j
              break

          if next_use == float('inf'):
            victim_index = i
            break

          if next_use > farthest_use:
            farthest_use = next_use
            victim_index = i

        frames[victim_index] = current_page

  return page_faults

def _run_algorithm(strings, frame_count):
  page_faults = 0

  for reference_string in strings:
    page_faults += _run_reference_string(reference_string, frame_count)

  return page_faults

def run(file_path, frame_count):
  return _run_algorithm(parser.parse_file(file_path), frame_count)
