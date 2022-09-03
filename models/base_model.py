#!/usr/bin/python3
import datetime, uuid

class BaseModel():
    """ Defines all common attributes/methods for other classes """

    

    def __str__(self):
        return "<" + str(BaseModel.__class__.name__) + ">" + "<" + str(self.id) + ">" + self.__dict__

    def save(self):
        
    def to_dict(self):

