# Backstage Takehome


## Project Decription


### Here's the challenge:

#### *Problem*: 

Please design and develop a service that I can query that will yield the difference between 

1. the sum of the squares of the first n natural numbers and 
2. the square of the sum of the same first n natural numbers, where n is guaranteed to be no greater than 100.

##### Example: 

The sum of the squares of the first ten natural numbers is:

`1^2 + 2^2 + ... + 10^2 = 385`

The square of the sum of the first ten natural numbers is:

`(1 + 2 + ... + 10)^2 = 552 = 3025`

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is `3025 − 385 = 2640`.

#### *Requirements*: 

You should use Python3.6+ and Django.

I should be able to install your service by doing: pip install -r requirements.txt. Please include a README with instructions for launching it.

I should be able to query your service at the following (or similar) endpoint:

`localhost:8000/difference?number=n` where `n` is any integer greater than 0 and less than or equal to 100.

Your service should emit a JSON object of the following structure:

```
{
    "datetime":current_datetime,
    "value":solution,
    "number":n,
    "occurrences":occurrences // the number of times n has been requested
    "last_datetime": datetime_of_last_request
}
```

For persistence you can use postgres, mysql, memcached,  sqlite3 or redis.

#### *Optional 1* 

Assume this is only the first of many such similar requests. For example, as a team we have decided that users really want to know the answer you may need to develop a service that also asks the following:

Please design and develop a service that I can query that will yield 1.) if a sequence of three natural numbers (a,b and c) are a Pythagorean triplet and 2.) the product of the sequence of these three numbers where abc = n, where c is guaranteed to be no greater than 1000.

Construct your application in such a way that you can easily scale to meet these additional product needs.

#### *Optional 2*  

Use Python3.6 style typehinting

#### *Optional 3*  

Unit tests are appreciated.

#### *Optional 4*  

Front end:

Create a react application (or any other front end framework or just jquery) based on the above backend service that should display a list of the above values in the four columns described above.

Your UI should have a form to enter the number that you wish to query.

#### *Delivery*:  

Please commit your code using either git or mercurial and use either bitbucket, gitlab, github, or a similar service. 

If you run into any issues, please contact Mo or Joe directly (cc'd).

Please deliver the result by November 27, 11 AM ET.



### How to use it




The admin interface has access to browse the data. This could use more refinement but it works out of the box.
http://localhost:8000/admin/


The API to calculate the difference
http://localhost:8000/difference?number=n  Where `n` is less than or equal to 100




## Tech Stack

This project was initialized off of [Docker Django Example](https://github.com/nickjj/docker-django-example). 

### Why this was chosen

First off, there's a lot of boiler plate to getting a django instance running locally on docker. I wanted to go straight to a dockerized instance so that my code has maximum portability. 

I wanted to give you an package that was easy to install and wouldn't interfere with anythign you've already install on your system. Containers ensure that correct versions of requirements are followed and don't collide with globally installed packages.


The initial bare bones are the following:

### Django Version
 - Django 5.1 
 - Python 3.12.5**

### Back-end

- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)
- [Celery](https://github.com/celery/celery)

### Front-end

- [esbuild](https://esbuild.github.io/)
- [TailwindCSS](https://tailwindcss.com/)
- [Heroicons](https://heroicons.com/)


## Set up for local dev


### Requirements

You will need to install [Docker Desktop](https://www.docker.com/products/docker-desktop/)


### Install Steps

```
git clone git@github.com:apt142/backstage.git
cd backstage
```

#### The .env file

The application requested doesn't need any special environmental variables since it doesn't have a need for secrets, API keys or environment specific configs.

But, it could! So, I built in an environment config file. 

The `.env.example` file has some standard dev environment values set by default. For a local dev environment, it should work without alteration. Production will definitely want a more robust version of this file.

Since we don't need it right now, I just committed the `.env.example` file as the `.env` so the set up process is more streamlined. Should this need to be altered, we would copy, make changes and restart the server. 

I would not do this in any development situation! This is not a terrible security decision.

For now, this is a no-op!


#### Run Docker
```
docker compose up --build
```

Once docker has initalized and is running you can visit the project at: <http://localhost:8000>


### Initialize your environment

The first thing you'll want to do is run your migrations

```
./run manage migrate
```

Next, you'll need to new super user.
```
./run manage createsuperuser
```


### Tools for ongoing development

#### Install Pre-commit

A pre-commit is highly recommended. To install it just run the following commands:

```
brew install pre-commit
pre-commit install
```

This will ensure that each commit that you do is in line with our coding standards.


#### Useful Commands

This project is built off of [Docker Django Example](https://github.com/nickjj/docker-django-example). See their documentation for a full list of useful commands. 

Here is a short list of helpful ones:


Update dependencies:
Back-end: `./run pip3:install` 
Front-end: `./run yarn:install`


Run Django commands:
```
./run manage <command>

# Run migrations
./run manage migrate

# Run all tests
./run manage test
```


## Next Steps

### Scalability

### Production Readiness

### Testing

### Additional endpoints
