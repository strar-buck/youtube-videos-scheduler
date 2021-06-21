# youtube-videos-scheduler

_fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response._
___
# Basic Requirements:

- [x] Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
- [x] A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- [x] A basic search API to search the stored videos using their title and description.
- [x] Dockerize the project.
- [x] It should be scalable and optimised.

# Bonus Points:

- [x] Add support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
- [] Make a dashboard to view the stored videos with filters and sorting options (optional)
- [x] Optimise search api, so that it's able to search videos containing partial match for the search query in either video title or description.

  
# Steps to run the application
Build the Image
```
docker-compose buid
```
Run the containers (Running multiple container - application server: Gunicorn, db container)
```
docker-compose up
```
Application server: Gunicorn and Background Jobs are running thrugh supervisor
# supervisor.conf

```

[program:fampay_main]
directory=/code
command=gunicorn fampay.wsgi:application --bind 0.0.0.0:8000
autostart=true
autorestart=true
stopwaitsecs=1
stdout_logfile=/code/logs/django_out.log
stderr_logfile=/code/logs/django_err.log

[program:fampay_scheduler]
directory=/code
command=celery -A fampay worker --loglevel=info
autostart=true
autorestart=true
stopwaitsecs=1
stdout_logfile=/code/logs/worker_out.log
stderr_logfile=/code/logs/worker_err.log

[program:fampay_beat_scheduler]
directory=/code
command=celery -A fampay beat --loglevel=info
autostart=true
autorestart=true
stopwaitsecs=1
stdout_logfile=/code/logs/worker_out.log
stderr_logfile=/code/logs/worker_err.log
```
Api endpoints
```
$ curl GET \
  --url 'http://localhost:8000/api/v1/youtube-video/list

$ curl GET \
  --url 'http://localhost:8000/api/v1/youtube-video/list?title=<some_title>&description=<some_desc>

```
Api Response
```
[{
	"videoId": "FcIxDz7sbGI",
	"createdOn": "2021-06-21T13:31:03.793520Z",
	"updatedOn": "2021-06-21T13:31:03.793543Z",
	"videoTitle": "LIVE CRICKET DISCUSSION &amp; FAN CHAT OF ISLAMABAD VS MULTAN  -  LIVE ANALYSIS OF IU VS MS TODAY PSL",
	"description": "psl live today match LIVE CRICKET DISCUSSION & FAN CHAT OF MULTAN vs LAHORE - LIVE ANALYSIS OF ms vs lq TODAY psl live today match LIVE ...",
	"publishedAt": "2021-06-21T11:49:07Z",
	"thumbnails": {
		"high": {
			"url": "https://i.ytimg.com/vi/FcIxDz7sbGI/hqdefault_live.jpg",
			"width": 480,
			"height": 360
		},
		"medium": {
			"url": "https://i.ytimg.com/vi/FcIxDz7sbGI/mqdefault_live.jpg",
			"width": 320,
			"height": 180
		},
		"default": {
			"url": "https://i.ytimg.com/vi/FcIxDz7sbGI/default_live.jpg",
			"width": 120,
			"height": 90
		}
	},
	"channelId": "UCnHzxEsUqjDdZ8cPjH4NBEQ",
	"channelTitle": "Techno Records"
}, {
	"videoId": "CsIyXOVKhhU",
	"createdOn": "2021-06-21T13:31:03.885944Z",
	"updatedOn": "2021-06-21T13:31:03.885969Z",
	"videoTitle": "LIVE CRICKET DISCUSSION &amp; FAN CHAT OF KARACHI VS QUETTA  - LIVE ANALYSIS OF KK vs QG TODAY PSL",
	"description": "psl live today match LIVE CRICKET DISCUSSION & FAN CHAT OF KARACHI VS QUETTA - LIVE ANALYSIS OF ms vs lq TODAY psl live today match LIVE ...",
	"publishedAt": "2021-06-19T17:12:36Z",
	"thumbnails": {
		"high": {
			"url": "https://i.ytimg.com/vi/CsIyXOVKhhU/hqdefault.jpg",
			"width": 480,
			"height": 360
		},
		"medium": {
			"url": "https://i.ytimg.com/vi/CsIyXOVKhhU/mqdefault.jpg",
			"width": 320,
			"height": 180
		},
		"default": {
			"url": "https://i.ytimg.com/vi/CsIyXOVKhhU/default.jpg",
			"width": 120,
			"height": 90
		}
	},
	"channelId": "UCnHzxEsUqjDdZ8cPjH4NBEQ",
	"channelTitle": "Techno Records"
}]
```

   
