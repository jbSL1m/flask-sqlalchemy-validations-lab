from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validate_name(self, key, name):
        # Strip extra spaces so a name containing only spaces is treated as empty.
        if not isinstance(name, str) or not name.strip():
            raise ValueError('An author name is required.')

        name = name.strip()
        # Check the database before accepting a name that another author uses.
        existing_author = Author.query.filter_by(name=name).first()
        if existing_author is not None and existing_author is not self:
            raise ValueError('Author names must be unique.')

        return name

    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        # Phone numbers are stored as text so leading zeroes are preserved.
        if (
            not isinstance(phone_number, str)
            or len(phone_number) != 10
            or not phone_number.isascii()
            or not phone_number.isdigit()
        ):
            raise ValueError('Phone numbers must contain exactly ten digits.')

        return phone_number

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title')
    def validate_title(self, key, title):
        # A useful title must include at least one of the lab's clickbait phrases.
        clickbait_phrases = ("won't believe", 'secret', 'top', 'guess')
        if not isinstance(title, str) or not any(
            phrase in title.lower() for phrase in clickbait_phrases
        ):
            raise ValueError(
                'Post titles must include "Won\'t Believe", "Secret", "Top", or "Guess".'
            )

        return title

    @validates('content')
    def validate_content(self, key, content):
        # The full post needs at least 250 characters to meet the minimum length.
        if not isinstance(content, str) or len(content) < 250:
            raise ValueError('Post content must be at least 250 characters long.')

        return content

    @validates('summary')
    def validate_summary(self, key, summary):
        # A missing summary is allowed, but a supplied one cannot exceed 250 characters.
        if summary is not None and (
            not isinstance(summary, str) or len(summary) > 250
        ):
            raise ValueError('Post summaries cannot exceed 250 characters.')

        return summary

    @validates('category')
    def validate_category(self, key, category):
        # Keep categories consistent so posts can be grouped reliably.
        if category not in ('Fiction', 'Non-Fiction'):
            raise ValueError('Post category must be Fiction or Non-Fiction.')

        return category


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
