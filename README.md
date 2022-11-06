

## Description
A script to handle scraping images from bike listings on craigslist. Running this script make a search request to craigslist for listings in the past 30 days that have images, and downloads the images into the `bike_scraper/images/full/` directory. The image files are named `{sha1_hash_of_the_image_url}.jpg`. Duplicate images are not downloaded.

Currently the script fetches listings for bicicyles in the Worcester area. The `pycraigslist` library used to make the initial search request to Craigslist has an issue constructing the url for listings in the Boston area. The `Scrapy` library used to download images has functionality that could also be used to make the search request, and I'm planning to integrate this in the next update.


## Executing program
To start the scraper run the following command from the `bike_scraper` directory 
```
scrapy crawl bikeSpider
```

If you would like to output a file for the results of the web scraper you can append `-O FILE` to the above command, where `FILE` is one of the following formats: `.json`, `.jsonl`, `.csv` or `.xml`. The [Scrapy documentation](https://docs.scrapy.org/en/latest/topics/commands.html#crawl) has more infomation on  this.

## Run  Info
On my local machine, it took ~30 minutes to scrape 1309 images (59MB in total) from 234 listings.
