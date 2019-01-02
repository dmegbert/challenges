from collections import Counter
import difflib
import xml.etree.ElementTree as ET

RSS_FEED = 'rss.xml'
PYBITES_XML = ET.parse(RSS_FEED)
ROOT = PYBITES_XML.getroot()
SIMILAR = 0.87
TOP_NUMBER = 10


def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    all_tags = []
    for item in ROOT[0].findall('item'):
        for category in item.findall('category'):
            blog_tag = category.text
            blog_tag = _clean_tag(blog_tag)
            all_tags.append(blog_tag)
    return all_tags


def _clean_tag(blog_tag):
    blog_tag = blog_tag.lower()
    blog_tag = blog_tag.replace('-', ' ')
    return blog_tag.strip()


def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    all_tags = get_tags()
    tag_counts = Counter(all_tags)
    return tag_counts.most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    all_tags = set(get_tags())
    all_matches = set()
    counter = 0
    dup_list = []
    for blog_tag in all_tags:
        matches = difflib.get_close_matches(blog_tag, all_tags, n=2, cutoff=SIMILAR)
        if len(matches) == 2 and matches[0] not in dup_list:
            match_tup = (matches[0], matches[1])
            all_matches.add(match_tup)
            counter += 1
            dup_list.append(matches[1])
    print(all_matches)
    return all_matches


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
