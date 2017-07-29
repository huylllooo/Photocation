from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db0 import Category, Base, MenuItem, User

engine = create_engine('sqlite:///cameradatabasewithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Items for 'DSLR Cameras'
category1 = Category(user_id=1, name="DSLR Cameras")

session.add(category1)
session.commit()

menuItem0 = MenuItem(user_id=1, name="Canon 5D Mark III", description="Greatest possible image quality",
                     price="$4,000", maker="Canon", category=category1)

session.add(menuItem0)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Nikon D810", description="Dramatically improved autofocus system",
                     price="$4,000", maker="Nikon", category=category1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Sony a99", description="Articulating display, continuous autofocus",
                     price="$2,800", maker="Sony", category=category1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Nikon D7100", description="The ultimate amateur sports and wildlife camera",
                     price="$1,500", maker="Nikon", category=category1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Canon T3 kit", description="As inexpensive as possible",
                     price="$400", maker="Canon", category=category1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Nikon D610", description="Ideal for landscapes and portraits",
                     price="$3,000", maker="Nikon", category=category1)

session.add(menuItem5)
session.commit()

# Items for Mirrorless Cameras
category2 = Category(user_id=1, name="Mirrorless Cameras")

session.add(category2)
session.commit()


menuItem0 = MenuItem(user_id=1, name="Sony a5100", description="Compact size",
                     price="$700", maker="Sony", category=category2)

session.add(menuItem0)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Sony a7R Mark II", description="Best image quality",
                     price="$4,000", maker="Sony", category=category2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Sony a6300", description="The best all-around camera",
                     price="$1000", maker="Sony", category=category2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Panasonic GH4", description="Best video, most DSLR-like",
                     price="$1,700", maker="Panasonic", category=category2)

session.add(menuItem3)
session.commit()


# Items for Lenses
category3 = Category(user_id=1, name="Lenses")

session.add(category3)
session.commit()


menuItem0 = MenuItem(user_id=1, name="EF5018STM", description="Single Focus Lens EF50mm F1.8 STM",
                     price="$150", maker="Canon", category=category3)

session.add(menuItem0)
session.commit()


menuItem1 = MenuItem(user_id=1, name="EF24-105USM", description="Standard Zoom Lens EF24-105mm F4L IS USM",
                     price="$900", maker="Canon", category=category3)

session.add(menuItem1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="SEL1670Z", description="Standard Zoom Lens 16-170mm F4L IS USM",
                     price="$900", maker="Sony", category=category3)

session.add(menuItem1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="SELP18105G", description="SONY E PZ 18-105mm F4 G OSS",
                     price="$600", maker="Sony", category=category3)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="SEL16F28 ", description="Sony SEL16F28 SLR Wide lens",
                     price="$200", maker="Sony", category=category3)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="NIKKOR 80-400mm", description="Nikon AF-S NIKKOR 80-400mm f/4.5-5.6G ED VR Lens",
                     price="$35,700", maker="Nikon", category=category3)

session.add(menuItem3)
session.commit()


print "added menu items 2!"