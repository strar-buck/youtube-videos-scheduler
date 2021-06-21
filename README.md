# youtube-videos-scheduler

_fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response._
___
# Basic Requirements:

- [x] Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
> I used threading to spawn a background thread to fetch all the youtube videos data. However, threads are not really concurrent in python because of GIL or Global Interpreter Lock. A more scalable solution would be to use a background worker like Celery based on a queue like Redis Queue.
- [x] A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
> Used `flask` and `flask_restful` to create basic APIs for querying results from sqlite DB.
- [x] A basic search API to search the stored videos using their title and description.
> I used basic like wildcard queries to search for keywords in the table. A more robust solution would be to use an Inverted Index like ElasticSearch to make this a full-fledged search service.
- [x] Dockerize the project.
- [x] It should be scalable and optimised.

# Bonus Points:

- Add support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
> I have added support for multiple API keys if the quota is exhausted. I have exhausted my API keys, so please provide your own keys.
- Make a dashboard to view the stored videos with filters and sorting options (optional)
- Optimise search api, so that it's able to search videos containing partial match for the search query in either video title or description.
    - Ex 1: A video with title *`How to make tea?`* should match for the search query `tea how`
    > This was straight forward. I had to split the keywords and search for those keywords. However, mentioning again, A scalable solution would be to use and Inverted Index like ElasticSearch.
  
# Steps to run the application
- With Docker
   
