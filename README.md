# youtube-videos-scheduler

_fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response._
___
# Basic Requirements:

- [x] Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
- [x] A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- [x] A basic search API to search the stored videos using their title and description.
- [x] Dockerize the project.
- [x] It should be scalable and optimised.

  
# Steps to run the application
Build the Image
```
docker-compose buid
```
Run the docker container
```
docker-compose up
```


   
