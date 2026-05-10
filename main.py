import fifo, lru, optimal
import file_generator, parser

test_runs = 50
frame_sizes = [3, 4, 5, 6]

fifo_name = "First In, First Out"
lru_name = "Last Recently Used"
optimal_name = "Optimal"

test_file = "job_files/testingdata.txt"

def test_algorithm(algorithm, algorithm_name):
  print(f"\n---{algorithm_name}---")
  
  for frame in frame_sizes:
    page_faults = algorithm.run(test_file, frame)
    print(f"\nPage frame size: {frame}")
    print(f">> Page faults: {page_faults}")

def test_batch_algorithm(algorithm):
  averages = [0, 0, 0, 0]

  for run in range(test_runs):
    pointer = 0

    for frame in frame_sizes:
      averages[pointer] += algorithm.run(test_file, frame)

      pointer += 1

  for i in range(len(averages)):
    averages[i] = averages[i] / test_runs

  return averages

def _batch_test_helper(averages, algorithm_name):
  print(f"\n---{algorithm_name}---")

  for i, frame in enumerate(frame_sizes):
    print(f"\nPage frame size: {frame}")
    print(f">> Average page faults: {averages[i]}")

def batch_test():
  fifo_totals = [0] * len(frame_sizes)
  lru_totals = [0] * len(frame_sizes)
  optimal_totals = [0] * len(frame_sizes)

  for _ in range(test_runs):
    file_generator.generate()

    fifo_results = test_batch_algorithm(fifo)
    lru_results = test_batch_algorithm(lru)
    optimal_results = test_batch_algorithm(optimal)

    for i in range(len(frame_sizes)):
      fifo_totals[i] += fifo_results[i]
      lru_totals[i] += lru_results[i]
      optimal_totals[i] += optimal_results[i]

  for i in range(len(frame_sizes)):
    fifo_totals[i] = fifo_totals[i] / test_runs
    lru_totals[i] = lru_totals[i] / test_runs
    optimal_totals[i] = optimal_totals[i] / test_runs

  _batch_test_helper(fifo_totals, fifo_name)
  _batch_test_helper(lru_totals, lru_name)
  _batch_test_helper(optimal_totals, optimal_name)

# for the correctness test
# uncomment the section above batch_test
# comment the batch_test
def main(): 
  # test_algorithm(fifo, fifo_name)
  # test_algorithm(lru, lru_name)      
  # test_algorithm(optimal, optimal_name)      

  batch_test()

main()

