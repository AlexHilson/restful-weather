#!/usr/bin/env python

import argparse

import yaml


class WCSMetadata(object):
    def __init__(self, url, **kwargs):
        pass


def scrape(services):
    metadata = {}
    for name, details in services.iteritems():
        url = details['url']
        kwargs = {key: details[key] for key in details if
                  key != 'url'}
        metadata[name] = WCSMetadata(url, **kwargs)
    return metadata


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config',
                        dest='config',
                        required=True,
                        help='location of configuration file')
    args = parser.parse_args()
    with open(args.config) as inf:
        services = yaml.load(inf.read())
    metadata = scrape(services)
