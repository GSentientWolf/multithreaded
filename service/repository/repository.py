
""" Create and initialize a relational Repository """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Union
from service.model.message import Message


class Repository:
    """
        Repository with a simple relational DB
    """
    def __init__(self, db: str = 'sqlite:///sensors.sqlite'):
        self.engine = create_engine(db)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        Message.metadata.create_all(self.engine)

    def add_message(self, message:Message) -> None:
        self.session.add(message)

    def save(self, messages: Union[List[Message] | Message]) -> None:

        if isinstance(messages, list):
            try:
                for msg in messages:
                    self.add_message(msg)
            except SQLAlchemyError as err:
                self.session.rollback()
            else:
                self.session.commit()
        else:
            self.add_message(messages)
            self.session.commit()
