## Generate RSS feed for any website based on the given CSS selectors

Example:
```commandline
curl --location 'http://192.168.1.24:8011/feed/rss_xml' \
--header 'Content-Type: application/json' \
--data '{
    "url" : "https://www.equitymaster.com/archives.asp?von=1&ov=1&tm=1&cotd=1&5min=1&mnuserh=N",
    "title_css" : "#tdArticles .nns h3 > a:nth-child(2)",                           
    "link_css" : "#tdArticles .nns h3 > a:nth-child(2)",
    "description_css": "#tdArticles .nns > p",
    "image_css": "#tdArticles .nns > h3 > a:nth-child(1) > img",
    "author_css":"",
    "date_css":"#tdArticles .nns > small"
}'
```

Will generate an XML output for website https://www.equitymaster.com