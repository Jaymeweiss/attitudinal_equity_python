def get_rank_sum(ratings, s):
    rank_sum = 0.0
    for rating in ratings:
        rank_sum += (1 / (pow(rating.ranking, s)))
    return rank_sum


def calculate_attitudinal_equity(ranking, s, rank_sum):
    return 1 / (pow(ranking, s) * rank_sum)


def calculate_attitudinal_equity_for_responses(response_list):
    for response in response_list:
        if len(response.ratings) < 2:
            response.ratings[0].attitudinal_equity = 1
        else:
            for brand in response.ratings:
                brand.attitudinal_equity = calculate_attitudinal_equity(brand.ranking, response.s_value,
                                                                        response.rank_sum)


def calculate_total_ae_for_brand(brand_name, response_list, total_responses):
    total_ae = 0.0
    for response in response_list:
        for brand in response.ratings:
            if brand.brand == brand_name:
                total_ae += brand.attitudinal_equity
    return total_ae / total_responses
