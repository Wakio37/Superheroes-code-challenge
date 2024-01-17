from app import app
from models import db,Hero,Power,hero_powers



with app.app_context():
        #Hero
        hero1 = Hero( name =  "Kamala Khan", super_name = "Ms. Marvel" )
        hero2 = Hero(name = "Doreen Green", super_name = "Squirrel Girl")
        hero3 = Hero(name = "Gwen Stacy", super_name = "Spider-Gwen")
        hero4 = Hero(name = "Janet Van Dyne", super_name = "The Wasp")
        hero5 = Hero(name = "Wanda Maximoff", super_name = "Scarlet Witch")
        hero6 = Hero(name = "Carol Danvers", super_name = "Captain Marvel")
        hero7 = Hero(name = "Jean Grey", super_name = "Dark Phoenix")
        hero8 = Hero(name = "Ororo Munroe", super_name = "Storm")
        hero9 = Hero(name = "Kitty Pryde", super_name = "Shadowcat")
        hero10 = Hero(name = "Elektra Natchios", super_name = "Elektra")

        hero_instances = [hero1,hero2,hero3,hero4,hero4,hero5,hero6,hero7,hero8,hero9,hero10]
        db.session.add_all(hero_instances)
        db.session.commit()

        #Power
        power1 = Power(name = 'super strength',description = 'gives the wielder super-human strengths')
        power2 = Power(name = 'flight',description = 'gives the wielder the ability to fly through the skies at supersonic speed')
        power3 = Power(name = 'super human senses',description = 'allows the wielder to use her senses at a super-human level')
        power4 = Power(name = 'elasticity',description = 'can stretch the human body to extreme lengths')

        power_instances = [power1,power2,power3,power4,power4]
        db.session.add_all(power_instances)
        db.session.commit()