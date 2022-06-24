# Created by Bowen Xu at 8/6/22

from path_config import DATA_DIR
import os
import json
import paper


def search(keywords, attribute, yrs_range):
    res = []
    for venue_type in os.listdir(DATA_DIR):
        for venue in os.listdir(os.path.join(DATA_DIR, venue_type)):
            for year in os.listdir(os.path.join(DATA_DIR, venue_type, venue)):
                if year not in yrs_range:
                    continue
                json_fname = os.listdir(os.path.join(
                    DATA_DIR, venue_type, venue, year))[0]
                json_fpath = os.path.join(
                    DATA_DIR, venue_type, venue, year, json_fname)
                data = json.load(open(json_fpath))
                for paper in data:
                    for keyword in keywords:
                        if keyword+' ' in paper[attribute].lower() or ' '+keyword in paper[attribute].lower():
                            res.append(paper)
                            break

    return res


def main():
    # conditions
    keywords = {'plugin'}
    attribute = 'title'
    yrs_range = [str(i) for i in range(2017, 2023)]

    res = search(keywords, attribute, yrs_range)

    print(json.dumps(res, indent=4))
    print("counts: {0}".format(len(res)))


if __name__ == '__main__':
    main()
