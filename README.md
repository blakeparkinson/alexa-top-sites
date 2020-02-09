## Requirements
- Python 2 or Python 3
- Needed libraries can be installed by the following command

```$python
pip install -r requirements.txt
```

## Usage
```$shell
python alexa.py -country US -count 1000 -secret xxx -key xxx [-start 10]
```

Where:
- `country`: should be the 2 character [ISO_3166-1 style](http://en.wikipedia.org/wiki/ISO_3166-1)
- `count`: the number of top sites to fetch
- `secret`: secret access key from your AWS account
- `key`: access key id from your AWS account
- `start` (optional): the website ranking you want to get started, the default is 1

Results will be:
- printed to the screen with format: `Ranking Domain`
- saved to a json file (top_alexa.json) with format `{"1": "google.com", ...}`
