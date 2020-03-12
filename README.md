# All Your Bots Are Belong To Us

![All Your Base Are Belong To Us](https://upload.wikimedia.org/wikipedia/en/0/03/Aybabtu.png)

## Roadmap

1. List bot accounts.
1. Build a tweet dataset (with metadata) from multiple bot accounts.
1. Explore tweets from a bot account.
1. Explore retweets from a bot account.
1. Explore hashtags from a bot account.
1. Explore replies from a bot account.
1. Explore mentions in tweets a bot account.
1. Explore location of multiple bot accounts.
1. Explore accounts multiple bot accounts follow.
1. Explore duplicated tweets (excluding retweets) in multiple bot accounts.
1. Explore timestamps of tweets from multiple bot accounts.
1. Explore timestamps of replies from multiple bot accounts.
1. Explore timestamps of replies from multiple bot accounts.
1. Explore Twitter threads context and correlation with bot replies.
1. Train a model to classify between bots and people.
1. Make an index of bots.
1. Flag Twitter bot accounts.
1. Warn Twitter users in a thread regarding bots.

## Requirements

A simple `requirements.txt` file is available for ease of configuration. Just run:

```
pip install -r requiremets.txt
```

## Usage

### Fetch

Fetch tweets from a given account and write it to a local CSV file.


```
python3 src/fetch.py [account]
```

## How to contribute

You don't need to be a developer to contribute to this project. There are many ways one can contirbute:

* Sharing this project in social media.
* Listing known bot accounts (use the Github issues or send it directly to me @vinicius0x42).
* Fetching tweets from bot accounts and opening PRs with new datasets.
* Opening PRs with your analysis (please, use Jupyter notebooks).
* Improving the crawler scripts.
* Improving the documentation.
* Translating the documenation.

Please, be polite.

## Disclaimer

This is a personal project.

**"All your ~~bases~~ bots are belong to us."**
