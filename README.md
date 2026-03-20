# Django Take-Home Assignment

Django take-home project: searching, filtering of products

---

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

---

## Setup

### Using uv (recommended)
```bash
git clone https://github.com/coffeemug17/django-take-home.git
cd django-take-home

uv sync
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py runserver
```

### Using pip
```bash
git clone https://github.com/coffeemug17/django-take-home.git
cd django-take-home

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install django

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## Populating the Database

The database isn't included in the repo, so you'll need to populate it before the app is useful.

Go to `http://localhost:8000/admin` and add data in this order, order matters since products depend on categories and tags existing first:

1. **Categories**: at least 5
2. **Tags**: at least 10
3. **Products**: at least 20, each with a name, description, a category, and some tags

---

## Using the App

Visit `http://localhost:8000`.

- Type in the search box to filter products by description
- Select a category from the dropdown
- Check one or more tags
- All three filters work together, results must match every applied condition
- Hit Clear to reset to go back to default display


---

## Running Tests
```bash
uv run python manage.py test
# or: python manage.py test
```

6 tests covering the main scenarios — default display, description search, category filter, tag filter, combined filters, and no results. Each test builds its own isolated data so they don't interfere with each other or depend on the database being pre-populated.

---

## A Few Notes

**Models**: `Product` has a `ForeignKey` to `Category` (one category per product) and a `ManyToManyField` to `Tag` (many tags per product). Used `SET_NULL` on the FK so deleting a category doesn't cascade delete all its products.

**Filtering logic**: filters are chained on the queryset so combining them applies AND logic. `.distinct()` is used when filtering by tags to avoid duplicate results from the ManyToMany join.

**Admin**: registered all three models with `list_display`, `search_fields`, and `filter_horizontal` on the tags field. `filter_horizontal` makes selecting multiple tags for a product much less painful than the default widget.

---

## AI Usage

Used Claude as a reference throughout, mainly for talking through structure and approach before writing code. All code written and understood by me. Hit a `TemplateDoesNotExist` error early on that turned out to be `APP_DIRS` not being enabled in settings. Also had to fix some test assertions that were checking for category and tag names that appear in the filter form on every page.