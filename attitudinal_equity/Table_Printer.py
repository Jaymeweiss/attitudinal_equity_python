from tabulate import tabulate

from attitudinal_equity.AE_calculations import calculate_total_ae_for_brand

brand_names = ['Facebook', 'Twitter', 'Google Plus', 'Linked In', 'Tumblr', 'Instagram']


def print_attitudinal_equity_table(responses, number_of_responses):
    table = []
    print('Attitudinal Equity')
    headers = ['Response'] + brand_names

    for x in range(number_of_responses):
        response = responses[x]
        row_values = [response.response_id]
        current_index = 0
        ordered_ratings = sorted(response.ratings, key=lambda y: y.table_index)
        total_attitudinal_equity = 0
        for brand in ordered_ratings:
            while current_index < brand.table_index:
                row_values.append('-')
                current_index += 1

            row_values.append("{:10.3f}".format(brand.attitudinal_equity))
            total_attitudinal_equity = total_attitudinal_equity + brand.attitudinal_equity
            current_index += 1

        while current_index < 6:
            row_values.append('-')
            current_index += 1

        row_values.append("{:10.3f}".format(total_attitudinal_equity))
        table.append(row_values)

    print(tabulate(table, headers))


def print_total_brand_level_ae(responses):
    total_brand_level_ae = 0
    for brand_name in brand_names:
        brand_ae = calculate_total_ae_for_brand(brand_name, responses, 10000)
        print(f'{brand_name} total AE: {brand_ae}')
        total_brand_level_ae += brand_ae
    print(f'Total brand level ae: {total_brand_level_ae}')
