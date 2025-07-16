# QueryMaze

**QueryMaze** is a Django data exploration game inspired by the [Hanukkah of Data 5784 Challenge](https://hanukkah.bluebird.sh/5784/). The objective is to explore a dataset using Django ORM and solve a series of puzzles.

---

##  What is this project?

This project is a Django/PostgreSQL playground where the goal is to search a maze of data and extract hidden information, like finding a customer! It’s built to help improve your Django ORM skills.

Data is provided by [Bluebird's Hanukkah of Data](https://hanukkah.bluebird.sh/5784-speedrun/data/).

---

##  Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/querymaze.git
cd querymaze
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```


### 3. Set up PostgreSQL and `.env`

Make sure PostgreSQL is running and create a database for the project.

Then create a `.env` file in the root directory and define the following:

```env
DATABASE_URL=postgres://USER:PASSWORD@localhost:5432/your_db_name

PRODUCT_CSV=/full/path/to/products.csv
CUSTOMER-CSV=/full/path/to/customers.csv
ORDER_CSV=/full/path/to/orders.csv
ORDERITEM_CSV=/full/path/to/order_items.csv
```

> You can download the CSV files from the official [Hanukkah of Data Dataset](https://hanukkah.bluebird.sh/5784-speedrun/data/)

---

##  Importing the Data

Once the environment variables and database are ready, run the data import script:
mysterious
```bash
python manage.py shell
```

Inside the shell:

```python
from import_script import import_data
import_data()
```

This will populate the database with all the necessary data from the CSV files.

---

##  Solving the Chapters

Each puzzle or chapter has its own script located in the `scripts/` folder. To solve a chapter:

```bash
python manage.py shell
```

Then run the desired function, for example:

```python
from querymaze.scripts.contractor_phone import find_contractor
find_contractor()
```

Repeat this for each chapter to proceed in the game!

---

## ✅ Goals

- Practice using Django ORM for complex data queries.
- Understand patterns in large-scale datasets.
- Build better confidence with data-driven applications.

---

##  License

This project is for educational purposes, inspired by the public [Hanukkah of Data](https://hanukkah.bluebird.sh/5784/) challenge.
