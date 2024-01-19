# brightwheel-challenge

Install poetry and then to use the env:
```poetry install```

To set env:
```export $(cat .env | xargs)```

To run raw:
```python brightwheel_challenge/jobs/extract_raw.py --start-date 2023-01-01 --asset-name "07-07-2023 Oklahoma Human Services" --target-name "ok"```

to run clean:
```python brightwheel_challenge/jobs/clean.py --target-name "ok"```

to check the db:
```sqlite3 db/warehouse.db```