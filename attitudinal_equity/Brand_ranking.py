def rank_brands(brands_list):
    brand_rankings = {}
    ordered_brands = sorted(brands_list, key=lambda x: x.value, reverse=True)

    build_brand_hash(ordered_brands, 0, brand_rankings, 1)

    counter = 1
    for key in brand_rankings:
        if len(brand_rankings[key]) > 0:
            rank_value = get_rank_value(counter, len(brand_rankings[key]))
            for brand in brand_rankings[key]:
                brand.ranking = rank_value
            counter = counter + len(brand_rankings[key])

    return ordered_brands


def get_rank_value(current_rank, total_same_brands):
    total = current_rank
    for x in range(total_same_brands - 1):
        current_rank = current_rank + 1
        total = total + current_rank
    return total / total_same_brands


def build_brand_hash(brand_list, brand_no, brand_ranking_hash, rank):
    brand_object = brand_list[brand_no]
    if brand_no + 1 < len(brand_list):
        next_rating_total = brand_list[brand_no + 1]
        brand_ranking_hash.setdefault(rank, []).append(brand_object)
        if brand_object.value == next_rating_total.value:
            build_brand_hash(brand_list, brand_no + 1, brand_ranking_hash, rank)
        else:
            build_brand_hash(brand_list, brand_no + 1, brand_ranking_hash, rank + 1)
    else:
        brand_ranking_hash.setdefault(rank, []).append(brand_object)
