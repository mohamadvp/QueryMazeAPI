# QueryMaze API

An API version of the original [QueryMaze](https://github.com/mohamadvp/QueryMaze) project, built to improve backend development skills with Django and Django REST Framework.
The project is Dockerized with two containers: one for the database and one for the application, so users can run it without importing data manually.

##  Project Purpose

- Implement different API development methods: ViewSets, Generic Views, and APIView
- Use of Django ORM and Serializers for clean and structured data handling
- Make setup easy with Docker
- Remove the need for manual data import
- Explore high-performance API design approaches
- Designed for understand and compare different DRF methodologies



##  Installation & Usage

### Option 1 – Run with Docker (Recommended)

### 1. Pull the Images
```bash
docker pull mohammadvp/querymaze-api:latest
docker pull mohammadvp/querymaze-api-db:latest
```
### 2. Create .env file
in the project root 
```bash
DATABASE_URL=postgres://postgres:1234@db:5432/querymaze
```
### 3. Start containers
```bash
docker-compose up -d
```
### 4. View the api :
http://localhost:8000/api/customer/

### Option 2 - Run manual

### 1. Install dependencies

Make sure Python and pip are installed, then run:

```bash
pip install django djangorestframework python-dotenv psycopg2-binary
```

### 2. Apply migrations
``` bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Set up PostgreSQL and .env
Make sure PostgreSQL is running and create a database for the project.

Then create a `.env` file in the root directory and define the following:

```env
DATABASE_URL=postgres://USER:PASSWORD@localhost:5432/your_db_name

PRODUCT_CSV=/full/path/to/products.csv
CUSTOMER_CSV=/full/path/to/customers.csv
ORDER_CSV=/full/path/to/orders.csv
ORDERITEM_CSV=/full/path/to/order_items.csv
```

> You can download the CSV files from the official [Hanukkah of Data Dataset](https://hanukkah.bluebird.sh/5784-speedrun/data/)


##  Importing the Data

Once the environment variables and database are ready, run the data import script:
mysterious
```bash
python manage.py shell
```
Inside the shell:

```python
from querymaze.scripts.import_script import import_data
import_data()
```

This will populate the database with all the necessary data from the CSV files.


### 4. Run the Development Server
```bash
python manage.py runserver
```

### 5. View the api :
http://localhost:8000/api/customer/


## License
This project is open-source and free to use for learning and personal development.