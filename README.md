It is an simple but highly effective hotel search web app which fetches the hotel info from booking.com and agoda based on user input and shows the best matches.
Tech stacks - Django, FastApi, Requests, Scrapy.


### ER diagram public link - https://dbdiagram.io/d/hotel_search_erd-687128b4f413ba3508757786

* sudo docker-compose up db --build -d [only for database]
* sudo docker-compose exec db psql -U hotel_user -d hotel_db
* sudo docker-compose down -v


[dev commands]
## If we face database migration issues then run - 
bash clean_pycache.sh

1.  sudo docker-compose up db --build -d
    sudo docker-compose exec db psql -U hotel_user -d hotel_db
    sudo docker-compose down -v

2.  cd django-project
    uv run python manage.py makemigrations hotel_search
    uv run python manage.py migrate

## To run the project
1. sudo docker-compose up db --build -d
2. uv run python manage.py migrate
3. go to the 'http://127.0.0.1:8000/search/' link.