#!/usr/lib/python3.8
# -*-coding:utf-8 -*
"""
Alexander DELAPORTE - CRLAO
https://tekipaki.hypotheses.org/
https://github.com/alxdrdelaporte/
https://gitlab.com/alxdrdelaporte

Parsing RSS feeds with feedparser
INPUT
RSS feed (feed URL)
OUTPUT
Console outputs + .tsv files
"""

import feedparser
import csv


def print_feed_data(feed):
    """Print title, URL, description and date of the last update of an RSS feed
    Parameter: feedparser parsed feed
    """
    print(feed.channel.title)
    print(feed.channel.link)
    print(feed.channel.description)
    print(f"Dernière mise à jour : {feed.channel.updated}")


def print_entries(feed):
    """Print title, URL, publication date, author, (description), tags for each of a feed's latest entries
    Parameter: feedparser parsed feed
    """
    for entry in feed.entries:
        print(entry.title)
        print(entry.link)
        print(entry.published)
        print(entry.author)
        # print(entry.description)
        try:
            for tag in entry.tags:
                print(tag['term'])
        except AttributeError:
            continue


def entries_table(output_file, feed):
    """Writes title, URL, publication date, author and tags of a feed's latests entries in a .tsv file
    Parameters: output file path (.tsv or .csv), feedparser parsed feed
    """
    with open(output_file, 'w', encoding='utf-8', newline='') as output_file:
        tags = ['Titre', 'URL', 'Date de publication', 'Auteur', 'Étiquettes']
        writer = csv.DictWriter(output_file, fieldnames=tags, delimiter='\t')
        writer.writeheader()
        for entry in feed.entries:
            entry_tags = ""
            tag_count = 0
            try:
                for tag in entry.tags:
                    tag_count += 1
                    if tag_count == len(entry.tags):
                        entry_tags += tag['term']
                    else:
                        entry_tags += f"{tag['term']};"
            except AttributeError:
                continue
            try:
                entry_title, entry_link, entry_published, entry_author = entry.title, entry.link,\
                                                                         entry.published, entry.author
            except AttributeError:
                continue
            entry_data = {
                'Titre': entry_title,
                'URL': entry_link,
                'Date de publication': entry_published,
                'Auteur': entry_author,
                'Étiquettes': entry_tags
            }
            writer.writerow(entry_data)


"""
USAGE EXAMPLES
"""
# Tekipaki
tekipaki = feedparser.parse('https://tekipaki.hypotheses.org/feed')
print_feed_data(tekipaki)
print_entries(tekipaki)
# Uncomment following line to write a .tsv file
# entries_table('tekipaki_entries_table.tsv', tekipaki)

# La Croisée de la Bulac
veille_bulac = feedparser.parse('https://veillebulac.hypotheses.org/feed')
print_feed_data(veille_bulac)
print_entries(veille_bulac)
# Uncomment following line to write a .tsv file
# entries_table('veille_bulac_entries_table.tsv', veille_bulac)
