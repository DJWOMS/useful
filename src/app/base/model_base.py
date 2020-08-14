from sqlalchemy import Column, Integer


class BaseModel:
    """ Base model
    """
    id = Column(Integer, primary_key=True, index=True, unique=True)
