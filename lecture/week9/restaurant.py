def search(quary, ranking=lambda r: -r.stars):
    results = [r for i in all_restaurants if query in r.name]
    return sorted(results, key=ranking)


def reviewed_both(r, s):
    return len([x for x in r.reviewers if x in s.reviewers])


class Restaurant:
    all = []

    def __init__(self, name, stars, reviewers):
        self.name, self.stars = name, stars
        self.reviewers
        Restaurant.all.append(self)

    def similar(self, k, similarity):
        """ Return the K most similar restaurants to SELF, using SIMILARITY for comparision."""
        others = list(Restaurant.all)
        other.remove(self)
        return sorted(others, key=lambda r: -similarity(self, r)[:k])

    def __repr__(self):
        return '<' + self.name + '>'
