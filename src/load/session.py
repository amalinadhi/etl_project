"""Method for session in database"""

from sqlalchemy.orm import sessionmaker


class BaseSesssion:
    def __init__(self):
        pass

    def create_from(self, engine):
        """Create session from an engine"""
        Session = sessionmaker(bind = engine)
        self.session = Session()

    def add(self, objs):
        """Add an object to a session"""
        self.session.bulk_save_objects(objs)

    def commit(self):
        """Commit a session"""
        self.session.commit()

