# import logging

import click
import twitter
from dynaconf import settings

from utils import write_tweets_to_csv

api = twitter.Api(
    consumer_key=settings.CONSUMER_KEY,
    consumer_secret=settings.CONSUMER_SECRET,
    access_token_key=settings.ACCESS_TOKEN_KEY,
    access_token_secret=settings.ACCESS_TOKEN_SECRET,
    tweet_mode='extended',
    sleep_on_rate_limit=True)

USER_TIMELINE_COUNT = 200


def get_tweets(screen_name, count=USER_TIMELINE_COUNT):
    tweets = []

    if count:
        _count = count % (USER_TIMELINE_COUNT + 1)
    else:
        _count = USER_TIMELINE_COUNT

    _query = api.GetUserTimeline(
        screen_name=screen_name,
        count=_count,
        include_rts=True,
        exclude_replies=False)
    tweets.extend(_query)

    if count:
        count = count - len(_query)

    while count or (count is None):
        _id = _query[-1].id - 1

        if count:
            _count = count % (USER_TIMELINE_COUNT + 1)

        _query = api.GetUserTimeline(
            screen_name=screen_name,
            max_id=_id,
            count=_count,
            include_rts=True,
            exclude_replies=False)

        tweets.extend(_query)

        if not _query:
            break

    return tweets


@click.command()
@click.option(
    '--limit',
    default=200,
    show_default=True,
    help='Number of tweets to fetch.')
@click.argument('account')
def fetch(limit, account):
    print(account)
    tweets = get_tweets(account, count=limit)
    write_tweets_to_csv(account, tweets)


if __name__ == '__main__':
    fetch()
