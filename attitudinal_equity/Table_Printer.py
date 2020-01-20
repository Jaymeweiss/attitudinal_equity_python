from tabulate import tabulate

from attitudinal_equity.AE_calculations import calculate_total_ae_for_brand


def print_attitudinal_equity_table(responses, number_of_responses, brand_names):
    print('Attitudinal Equity')
    table = []
    headers = ['Response'] + brand_names + ['Total']

    for x in range(number_of_responses):
        response = responses[x]
        row_values = [response.response_id]
        ordered_ratings = sorted(response.ratings, key=lambda y: y.table_index)
        current_index = 0
        total_attitudinal_equity = 0
        for brand in ordered_ratings:
            current_index = fill_blank_values(current_index, row_values, brand.table_index)

            row_values.append("{:10.3f}".format(brand.attitudinal_equity))
            total_attitudinal_equity = total_attitudinal_equity + brand.attitudinal_equity
            current_index += 1

        fill_blank_values(current_index, row_values, 6)

        row_values.append("{:10.3f}".format(total_attitudinal_equity))
        table.append(row_values)

    print(tabulate(table, headers))


def fill_blank_values(current_index, row_values, upper_bound):
    while current_index < upper_bound:
        row_values.append('-')
        current_index += 1
    return current_index


def print_total_brand_level_ae(responses, brand_names):
    total_brand_level_ae = 0
    for brand_name in brand_names:
        brand_ae = calculate_total_ae_for_brand(brand_name, responses, 10000)
        print(f'{brand_name} total AE: {brand_ae}')
        total_brand_level_ae += brand_ae
    print(f'Total brand level ae: {total_brand_level_ae}')
