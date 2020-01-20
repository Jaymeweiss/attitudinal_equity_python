import csv

from attitudinal_equity.AE_calculations import get_rank_sum
from attitudinal_equity.Brand import Brand
from attitudinal_equity.Brand_ranking import rank_brands
from attitudinal_equity.Response import Response
from attitudinal_equity.S import s_value


def read_data():
    with open('./attitudinal_equity/survey_data_original.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        responses = []
        for row in csv_reader:
            ratings = []
            if row["Facebook:performance_rating"] != '':
                ratings.append(Brand('Facebook', int(row["Facebook:performance_rating"]), 0))
            if row["Twitter:performance_rating"] != '':
                ratings.append(Brand('Twitter', int(row["Twitter:performance_rating"]), 1))
            if row["Google+:performance_rating"] != '':
                ratings.append(Brand('Google Plus', int(row["Google+:performance_rating"]), 2))
            if row["LinkedIn:performance_rating"] != '':
                ratings.append(Brand('Linked In', int(row["LinkedIn:performance_rating"]), 3))
            if row["Tumblr:performance_rating"] != '':
                ratings.append(Brand('Tumblr', int(row["Tumblr:performance_rating"]), 4))
            if row["Instagram:performance_rating"] != '':
                ratings.append(Brand('Instagram', int(row["Instagram:performance_rating"]), 5))

            if len(ratings) > 0:
                value_for_s = s_value(len(ratings))
                ranked_ratings = rank_brands(ratings)
                rank_sum = get_rank_sum(ranked_ratings, value_for_s)
                responses.append(Response(row["Response ID"], ranked_ratings, value_for_s, rank_sum))

            line_count += 1
        print(f'Processed {line_count} lines.')
        return responses
