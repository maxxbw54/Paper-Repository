# Created by Bowen Xu at 8/6/22

from path_config import DATA_DIR
import os
import json
from utils.paper_list_analyzer import stats_for_paper_list


def search(keywords, attribute, yrs_range):
    res = []
    for venue_type in os.listdir(DATA_DIR):
        venue_type_dir = os.path.join(DATA_DIR, venue_type)
        if not os.path.isdir(venue_type_dir):
            continue
        for venue_name in os.listdir(venue_type_dir):
            venue_dir = os.path.join(venue_type_dir, venue_name)
            if not os.path.isdir(venue_dir):
                continue
            for year in os.listdir(venue_dir):
                if year not in yrs_range:
                    continue
                json_fname = os.listdir(os.path.join(
                    DATA_DIR, venue_type, venue_name, year))[0]
                json_fpath = os.path.join(
                    DATA_DIR, venue_type, venue_name, year, json_fname)
                data = json.load(open(json_fpath))
                for paper in data:
                    for keyword in keywords:
                        if keyword+' ' in paper[attribute].lower() or ' '+keyword in paper[attribute].lower():
                            res.append(paper)
                            break

    return res


def main():
    # conditions
    keywords = {'how far are we'}
    attribute = 'title'
    display_attributes = ['title', 'url', 'venue_name', 'venue_type', 'year']
    yrs_range = [str(i) for i in range(2017, 2023)]

    res = search(keywords, attribute, yrs_range)

    for idx, paper in enumerate(res):
        paper = {k: v for k, v in paper.items() if v is not None and k in display_attributes}
        print("Paper #{0}\n{1}\n".format(
            idx, json.dumps(paper, sort_keys=True, indent=4)))

    # print stats
    print("counts: {0}".format(len(res)))
    venue_stats, year_stats, venue_type_stats = stats_for_paper_list(res)
    print("venue_stats:\n{0}\n\n".format(json.dumps(venue_stats, indent=4)))
    print("year_stats:\n{0}\n\n".format(json.dumps(year_stats, indent=4)))
    print("venue_type_stats:\n{0}\n".format(
        json.dumps(venue_type_stats, indent=4)))


if __name__ == '__main__':
    main()
