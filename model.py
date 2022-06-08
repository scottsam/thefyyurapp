from datetime import datetime
from email.policy import default

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# TODO: connect to a local postgresql database



def setup(app):
    app.config.from_object('config.Config')
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    return db






#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#




class Venue(db.Model):
    __tablename__ = 'venue_place'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_description = db.Column(db.String(500))
    seeking_talent = db.Column(db.Boolean, default=False)
    website = db.Column(db.String(120))
    genres = db.Column(db.String())
    artists = db.relationship("Show", back_populates='venue')


    def __init__(self, name,city,state,address,phone,image_link,facebook_link,seeking_description,seeking_talent,website,genres,):
        self.name = name
        self.city = city
        self.state = state
        self.address=address
        self.phone=phone
        self.image_link=image_link
        self.facebook_link = facebook_link
        self.seeking_description=seeking_description
        self.seeking_talent=seeking_talent
        self.website=website
        self.genres=genres
        
        


    def __repr__(self):
        return f'<Venue id: {self.id}, name: {self.name}>'




    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'artist_place'
    

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(120))
    website = db.Column(db.String(120))
    venues = db.relationship("Show", back_populates='artist')

    def __init__(self, name,city,state,phone,genres,image_link,facebook_link,seeking_venue,seeking_description,website):
        self.name = name
        self.city = city
        self.state = state
        self.phone=phone
        self.genres=genres
        self.image_link=image_link
        self.facebook_link = facebook_link
        self.seeking_venue=seeking_venue 
        self.seeking_description=seeking_description
        self.website=website
        
        


    def __repr__(self):

        return f'<Artist id:{self.id} , name:{self.name}>'

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

   
       
    

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.


#show model
class Show(db.Model):

    __tablename__ = 'shows'
    id = db.Column(db.Integer,primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue_place.id'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist_place.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False,default=datetime.utcnow())
    venue = db.relationship(Venue, back_populates="artists")
    artist = db.relationship(Artist, back_populates="venues")

    def __repr__(self):
        return f'<Show id:{self.id} , time: {self.start_time}>'
    



   


    
