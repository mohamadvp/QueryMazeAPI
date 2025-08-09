# QueryMaze API

An API version of the original [QueryMaze](https://github.com/mohamadvp/QueryMaze) project, built to improve backend development skills with Django and Django REST Framework.

##  Project Purpose

- Implementation of multiple API development approaches: ViewSets, Generic Views, and APIView
- Use of Django ORM and Serializers for efficient, structured data handling
- Modular and scalable architecture with a focus on clean, maintainable code 
- Use a different way for high-performance API design
- Designed for understand and compare different DRF methodologies



##  Installation & Usage

### 1. Install Dependencies

Make sure Python and pip are installed, then run:

```bash
pip install django djangorestframework python-dotenv psycopg2-binary
```

### 2. Apply Migrations
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

### 5. Usage
```bash
GET http://127.0.0.1:8000/api/top-customer/
```


## License
This project is open-source and free to use for learning and personal development.