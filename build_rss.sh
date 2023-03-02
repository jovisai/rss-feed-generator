# for equity master
curl --location 'http://127.0.0.1:8011/feed/rss_xml' \
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


