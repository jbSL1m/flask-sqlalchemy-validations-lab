# Flask-SQLAlchemy Validations Lab

## Scenario

You’ve been brought in as a junior developer to help maintain a blog platform 
for a publishing company. The editorial team recently complained that the system 
is accepting poorly formatted data: posts with missing content, authors with 
duplicate entries, and even spammy or incomplete titles. Your job is to 
strengthen the backend validation layer so only clean, accurate, and editorial-
ready data is stored in the database.

To accomplish this, you’ll add attribute-level validations directly to your 
SQLAlchemy models using Python property decorators and `@validates()` methods. 
You’ll enforce field constraints such as uniqueness, length, and conditional logic,
all of which align with typical business rules you'd encounter in production.

## Tools & Resources

- [GitHub Repo](https://github.com/learn-co-curriculum/flask-sqlalchemy-validations-lab)
- [Changing Attribute Behavior - SQLAlchemy](https://docs.sqlalchemy.org/en/14/orm/mapped_attributes.html#simple-validators)

## Set Up

This is a **test-driven lab**.

Run `pipenv install` to create your virtual environment and `pipenv shell` to
enter the virtual environment.

```console
pipenv install && pipenv shell
```

This project has starter code for a couple of models, `Author` and `Post`. To
get create the database from the initial migration, run:

```console
$ cd server
$ flask db upgrade
$ python seed.py
```

## Instructions

## Validation behavior

The `Author` and `Post` models validate values as they are assigned. Authors
must have a unique, non-empty name and a phone number made up of exactly ten
digits. Posts need at least 250 characters of content, may have a summary of
up to 250 characters, must use the `Fiction` or `Non-Fiction` category, and
must include one of the supported clickbait phrases in the title.

Run the tests from the `server/` directory with:

```console
pytest -x
```

### Task 1: Define the Problem

Currently, the application lacks basic validation. The following issues exist:

* `Authors` can be created with no name or duplicate names.
* `Posts` may have:
  * Empty or short content,
  * Overly long or missing summaries,
  * Incorrect categories,
  * Non-descriptive or generic titles.

Because these rules are not enforced at the model level, invalid data can be inserted 
either manually or via a broken front-end form.

Without these constraints, the database risks filling up with junk or misleading data, 
and the application loses credibility with users and internal teams. Your task is to 
ensure all `Author` and `Post` records comply with strict rules before being persisted.

### Task 2: Determine the Design

You'll work on adding validators to both the Author and Post models.

* Author
  * name: required and no duplicates
  * phone numbers: exactly ten digits

* Post 
  * content: 250 character minimum
  * summary: 250 characters maximum
  * category: `Fiction` or `Non-Fiction` only
  * title: must contain "Won't Believe", "Secret", "Top", and/or "Guess"

### Task 3: Develop, Test, and Refine the Code

#### Step 1: Implement Validations

Add validators to the `Author` and `Post` models such that:

1. All authors have a name.
2. No two authors have the same name.
3. Author phone numbers are exactly ten digits.
4. Post content is at least 250 characters long.
5. Post summary is a maximum of 250 characters.
6. Post category is either `Fiction` or `Non-Fiction`.
7. Post title is sufficiently clickbait-y and must contain one of the following:
   - "Won't Believe"
   - "Secret"
   - "Top"
   - "Guess"

You should not need to run another migration, unless you altered model
constraints.

#### Step 2: Test and Refine your Code

Run `pytest -x` to run your tests. Use these instructions and `pytest`'s error
messages to complete your work in the `server/` folder.

#### Step 3: Commit and Push Git History

* Commit and push your code:

```bash
git add .
git commit -m "final solution"
git push
```

* If you created a separate feature branch, remember to open a PR on main and merge.

### Task 4: Document and Maintain

Best Practice documentation steps:
* Add comments to the code to explain purpose and logic, clarifying intent and functionality of your code to other developers.
* Update README text to reflect the functionality of the application following https://makeareadme.com. 
  * Add screenshot of completed work included in Markdown in README.
* Delete any stale branches on GitHub
* Remove unnecessary/commented out code
* If needed, update git ignore to remove sensitive data

---

## Important Submission Note

Before you submit your solution, you need to save your progress with git.

1. Add your changes to the staging area by executing `git add .`.
2. Create a commit by executing `git commit -m "Your commit message"`.
3. Push your commits to GitHub by executing `git push origin main`.

CodeGrade will grade your lab using the same tests as are provided in the `testing/` directory.