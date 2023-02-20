## WIP: Generate RSS feed for any website based on the given CSS selectors

## How to run
1. Pull the code from git
```commandline
git clone https://github.com/jovisai/rss-feed-generator.git
```

2. Build the docker container
```commandline
docker compose build
```
3. Run the container
```commandline
docker compose up
```
4. Test the rss feed generator

The below curl command generates rss feed for equitymaster.com
```commandline
curl --location 'http://<DOCKER_IP>:8011/feed/rss_xml' \
--header 'Content-Type: application/json' \
--data '{
    "website_title":"Equity Master",
    "website_link":"https://www.equitymaster.com/rss",
    "website_description":"Helping You Build Wealth With Honest Research. Since 1996",
    "url" : "https://www.equitymaster.com/archives.asp?von=1&ov=1&tm=1&cotd=1&5min=1&mnuserh=N",
    "title_css" : "#tdArticles .nns h3 > a:nth-child(2)",                           
    "link_css" : "#tdArticles .nns h3 > a:nth-child(2)",
    "description_css": "#tdArticles .nns > p",
    "image_css": "#tdArticles .nns > h3 > a:nth-child(1) > img",
    "author_css":"",
    "date_css":"#tdArticles .nns > small"
}'
```

5. Access the xml file directly after generating \
http://<DOCKER_IP>:8011/www.equitymaster.com.xml