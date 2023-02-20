import os
from datetime import timezone
from urllib.parse import urlparse

import dateutil
import requests
from bs4 import BeautifulSoup
from flask import Blueprint, request, Response
from flask_expects_json import expects_json
from feedgen.feed import FeedGenerator
from urllib.parse import urljoin

feed_blueprint = Blueprint('feed_blueprint', __name__)

rss_feed_descriptor_schema = {
    "type": "object",
    "properties": {
        "url": {"type": "string"},
        "title_css": {"type": "string"},
        "link_css": {"type": "string"},
        "description_css": {"type": "string"},
        "author_css": {"type": "string"},
        "image_css": {"type": "string"},
        "date_css": {"type": "string"},
        "website_link": {"type": "string"},
        "website_title": {"type": "string"},
        "website_description": {"type": "string"}
    },
    "required": ["url", "title_css", "link_css", "description_css", "date_css", "website_link", "website_title",
                 "website_description"]
}


@feed_blueprint.route('/rss_xml', methods=['POST'])
@expects_json(rss_feed_descriptor_schema)
def refresh_feeds():
    url = request.get_json()["url"]
    title_css = request.get_json()["title_css"]
    link_css = request.get_json()["link_css"]
    description_css = request.get_json()["description_css"]
    author_css = request.get_json()["author_css"]
    image_css = request.get_json()["image_css"]
    website_title = request.get_json()["website_title"]
    website_link = request.get_json()["website_link"]
    website_description = request.get_json()["website_description"]
    date_css = request.get_json()["date_css"]

    r = requests.get(url)
    html_document = r.text
    soup = BeautifulSoup(html_document, "lxml")
    title_elements = soup.select(title_css)
    link_elements = soup.select(link_css)
    description_elements = soup.select(description_css)
    images_elements = soup.select(image_css)
    date_elements = soup.select(date_css)

    fg = FeedGenerator()
    fg.title(website_title)
    fg.link(href=website_link, rel='self')
    fg.description(website_description)
    for index, title_element in enumerate(title_elements):
        fe = fg.add_entry()
        fe.id(link_elements[index].get('href'))
        fe.title(title_element.get_text())
        fg.image(images_elements[index].get('src'))
        fe.description(description_elements[index].get_text())

        anchor_href = link_elements[index].get('href')
        fe.link(href=urljoin(url, anchor_href))

        dt = dateutil.parser.parse(date_elements[index].get_text())
        dt = dt.replace(tzinfo=timezone.utc)

        fe.published(dt.isoformat())
        domain = urlparse(website_link).netloc
        filename = os.path.join(os.environ.get('STATIC_FILES_ROOT'), "{0}.xml".format(domain))
        fg.rss_file(filename)
    return Response(fg.rss_str(), mimetype='text/xml')
