# Django Product Search: Take-Home Assignment

A Django application for searching and filtering products by description, category, and tags.

---

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

---

## Setup

### Using uv (recommended)

**1. Clone the repository**
```bash
git clone https://github.com/coffeemug17/django-take-home.git
cd django-take-home
```

**2. Install dependencies**
```bash
uv sync
```

**3. Run migrations**
```bash
uv run python manage.py migrate
```

**4. Create a superuser**
```bash
uv run python manage.py createsuperuser
```

**5. Start the development server**
```bash
uv run python manage.py runserver
```

---

### Using pip (alternative)

**1. Clone the repository**
```bash
git clone https://github.com/coffeemug17/django-take-home.git
cd django-take-home
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install django
```

**4. Run migrations**
```bash
python manage.py migrate
```

**5. Create a superuser**
```bash
python manage.py createsuperuser
```

**6. Start the development server**
```bash
python manage.py runserver
```

---

## Populating the Database

The database is not included in the repository. You will need to populate it manually via the Django admin interface.

**1. Go to** `http://localhost:8000/admin` and log in with your superuser credentials

**2. Add data in this order** (order matters due to model dependencies):
- **Categories**: at least 5 (e.g. Electronics, Clothing, Books, Kitchen, Sports)
- **Tags**: at least 10 (e.g. Sale, New Arrival, Popular, Wireless, Eco-Friendly)
- **Products**: at least 20, each with a name, description, one category, and one or more tags

---

## Using the App

Visit `http://localhost:8000` to access the product search page.

- **Search**: type any word or phrase to search across product descriptions
- **Category filter**: select a category from the dropdown to filter by category
- **Tag filter**: check one or more tags to filter by tags
- **Combine**: all three filters work together simultaneously
- **Clear**: click the Clear link to reset all filters and show all products

---

## Running Tests
```bash
uv run python manage.py test
# or with pip: python manage.py test
```

6 tests covering default display, description search, category filter, tag filter, combined filters, and no results.

---

## Project Structure
```
django-take-home/
├── config/                 # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── products/               # Main application
│   ├── migrations/
│   ├── templates/
│   │   └── products/
│   │       └── product_list.html
│   ├── admin.py            # Admin registration with search and filter config
│   ├── models.py           # Category, Tag, Product models
│   ├── tests.py            # Search and filter tests
│   ├── urls.py
│   └── views.py            # Search and filter logic
├── manage.py
├── pyproject.toml
└── README.md
```

---

## Design Decisions

- **`ForeignKey` for category**: a product belongs to one category, so a ForeignKey with `SET_NULL` was the appropriate choice to avoid deleting products if a category is removed
- **`ManyToManyField` for tags**: a product can have multiple tags and a tag can belong to multiple products
- **Chained queryset filtering**: filters are applied sequentially using Django's ORM, so combining search and filters uses AND logic — results must match all applied conditions
- **`.distinct()`**: used when filtering by tags to prevent duplicate products appearing in results due to the M2M join
- **`filter_horizontal`** in admin: makes selecting multiple tags for a product significantly easier during data entry

---

## AI Usage

Claude (Anthropic) was used as an assistant during this assignment for guidance on project structure, phase planning, and code review. All code was written, understood, and validated by me. The AI was not used to generate code directly; it was used in a conversational capacity to talk through decisions and catch issues like false positive test assertions and the `TemplateDoesNotExist` error caused by `APP_DIRS` configuration.