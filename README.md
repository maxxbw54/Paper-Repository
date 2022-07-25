# Top-tier-SE-Paper-Repository

## Living Coverage/Scope (from 2012-2022)

### Conferences

- ICSE
- ASE
- FSE
- ISSTA

### Journals

- TSE
- TOSEM
- ESE (a.k.a. EMSE)

## Instruction on running the Script [keyword.py](scripts/search/keywords.py) for search purpose (key word mapping on target attribute)

- Modify the [conditions](scripts/search/keywords.py#L37) based on your need
- Run the script

Example Query:
```python
# conditions
keywords = {'how far are we'}
attribute = 'title'
display_attributes = ['title', 'url', 'venue_name', 'venue_type', 'year']
yrs_range = [str(i) for i in range(2017, 2023)]

```

Example Output:

```json
Paper #0
{
    "title": "Detecting False Alarms from Automatic Static Analysis Tools: How Far are We?",
    "url": "https://ieeexplore.ieee.org/document/9793908",
    "venue_name": "International Conference on Software Engineering",
    "venue_type": "conf",
    "year": 2022
}

Paper #1
{
    "title": "Log-based Anomaly Detection with Deep Learning: How Far Are We?",
    "url": "https://doi.org/10.1145/3510003.3510155",
    "venue_name": "International Conference on Software Engineering",
    "venue_type": "conf",
    "year": 2022
}

Paper #2
{
    "title": "Automatic Unit Test Generation for Machine Learning Libraries: How Far Are We?",
    "url": "https://doi.org/10.1109/ICSE43902.2021.00138",
    "venue_name": "International Conference on Software Engineering",
    "venue_type": "conf",
    "year": 2021
}

Paper #3
{
    "title": "Automatically assessing code understandability: how far are we?",
    "url": "https://doi.org/10.1109/ASE.2017.8115654",
    "venue_name": "IEEE/ACM International Conference on Automated Software Engineering",
    "venue_type": "conf",
    "year": 2017
}

Paper #4
{
    "title": "Machine Learning Based Recommendation of Method Names: How Far are We.",
    "url": "https://doi.org/10.1109/ASE.2019.00062",
    "venue_name": "IEEE/ACM International Conference on Automated Software Engineering",
    "venue_type": "conf",
    "year": 2019
}

Paper #5
{
    "title": "Automated Patch Correctness Assessment: How Far are We?",
    "url": "https://doi.org/10.1145/3324884.3416590",
    "venue_name": "IEEE/ACM International Conference on Automated Software Engineering",
    "venue_type": "conf",
    "year": 2020
}

Paper #6
{
    "title": "Code-Based Vulnerability Detection in Node.js Applications: How far are we?",
    "url": "https://doi.org/10.1145/3324884.3421838",
    "venue_name": "IEEE/ACM International Conference on Automated Software Engineering",
    "venue_type": "conf",
    "year": 2020
}

Paper #7
{
    "title": "Neural-machine-translation-based commit message generation: how far are we?",
    "url": "https://doi.org/10.1145/3238147.3238190",
    "venue_name": "IEEE/ACM International Conference on Automated Software Engineering",
    "venue_type": "conf",
    "year": 2018
}

Paper #8
{
    "title": "History-driven build failure fixing: how far are we?",
    "url": "https://doi.org/10.1145/3293882.3330578",
    "venue_name": "International Symposium on Software Testing and Analysis",
    "venue_type": "conf",
    "year": 2019
}

Paper #9
{
    "title": "Deep just-in-time defect prediction: how far are we?",
    "url": "https://doi.org/10.1145/3460319.3464819",
    "venue_name": "International Symposium on Software Testing and Analysis",
    "venue_type": "conf",
    "year": 2021
}

counts: 10
venue_stats:
{
    "International Conference on Software Engineering": 3,
    "IEEE/ACM International Conference on Automated Software Engineering": 5,
    "International Symposium on Software Testing and Analysis": 2
}


year_stats:
{
    "2022": 2,
    "2021": 2,
    "2017": 1,
    "2019": 2,
    "2020": 2,
    "2018": 1
}


venue_type_stats:
{
    "conf": 10
}
```

