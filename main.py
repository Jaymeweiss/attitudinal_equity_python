import time

from attitudinal_equity import CSVReader
from attitudinal_equity.AE_calculations import calculate_attitudinal_equity_for_responses
from attitudinal_equity.Table_Printer import print_attitudinal_equity_table, print_total_brand_level_ae

start = time.time()

responses = CSVReader.read_data()
calculate_attitudinal_equity_for_responses(responses)
print_attitudinal_equity_table(responses, 100)  # adds a full second to execution time

end = time.time()

print_total_brand_level_ae(responses)

print('Execution time', end - start)
