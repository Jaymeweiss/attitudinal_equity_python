import csv

from attitudinal_equity.AE_calculations import get_rank_sum
from attitudinal_equity.Brand import Brand
from attitudinal_equity.Brand_ranking import rank_brands
from attitudinal_equity.Response import Response
from attitudinal_equity.S import s_value


def read_data(column_names):
    with open('./attitudinal_equity/survey_data_original.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        responses = []
        for row in csv_reader:
            ratings = []
            index = 0
            for column_name in column_names:
                if row[f'{column_name}:performance_rating'] != '':
                    ratings.append(Brand(column_name, int(row[f'{column_name}:performance_rating']), index))
                    index += 1

            if len(ratings) > 0:
                value_for_s = s_value(len(ratings))
                ranked_ratings = rank_brands(ratings)
                rank_sum = get_rank_sum(ranked_ratings, value_for_s)
                responses.append(Response(row["Response ID"], ranked_ratings, value_for_s, rank_sum))

            line_count += 1
        print(f'Processed {line_count} lines.')
        return responses
