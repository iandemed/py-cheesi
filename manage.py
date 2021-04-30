import os
from flask_script import Manager, Command
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from db.scrape_seed_data import scrape_seed_data


app = create_app()
app.config.from_object(os.getenv('APP_SETTINGS'))

db.init_app(app)

migrate = Migrate(app, db)
manager = Manager(app)

class ScrapeSeedData(Command):
    "Scrapes cheese.com for data to populate the cheese API."

    def run(self):
        scrape_seed_data()

manager.add_command('db', MigrateCommand)
manager.add_command('seeddata', ScrapeSeedData())


if __name__ == '__main__':
    manager.run()