import logging
import random
from google.cloud import datastore

class UserBase():
    def __init__(self):
        """ Initialize user base. """
    
    def get_client(self):
        """ Gets the datastore client. """
        return datastore.Client()

    def user_to_entity(self, username, email, password):
        """ Converts a user to an entity. """
        client = self.get_client()

        user_entity = datastore.Entity(client.key('User'))
        user_entity.update(
            {
                "username" : username,
                "email" : email, 
                "password" : password,
                "time" : "",
            }
        )
        return user_entity

    def store_user(self, username, email, password):
        """ Store a user as an entity in datastore. """        
        client = self.get_client()
        client.put(self.user_to_entity(username, email, password))

    def update_time(self, username, time):
        client = self.get_client()
        key = client.key('User', username)
        user = client.get(key)
        user["time"] = time
        client.put(user)

    def get_user_time(self, username):
        client = self.get_client()
        key = client.key('User', username)
        user = client.get(key)
        return user["time"]

    def check_if_username_exists(self, username):
        client = self.get_client()
        query = client.query(kind='User')
        query.add_filter('username', '=', username)
        if len(list(query.fetch())) == 0:
            logging.error('Username, ' + username + ', does not exist in the datastore.')
            return False
        else:
            logging.error('Username, ' + username + ', exists in the datastore.')
            return True

    def check_if_email_exists(self, email):
        client = self.get_client()
        query = client.query(kind='User')
        query.add_filter('email', '=', email)
        if len(list(query.fetch())) == 0:
            logging.error('Email, ' + email + ', does not exist in the datastore.')
            return False
        else:
            logging.error('Email, ' + email + ', exists in the datastore.')
            return True

    def validate_login(self, userID, password):
        client = self.get_client()
        query = client.query(kind='User')
        query.add_filter('username', '=', userID)
        if len(list(query.fetch())) == 0:
            query = client.query(kind='User')
            query.add_filter('email', '=', userID)
            if len(list(query.fetch())) == 0:
                logging.error('User ID, ' + userID + ', does not exist in the datastore.')
                return False
            else:
                query.add_filter('password', '=', password)
                if len(list(query.fetch())) == 0:
                    logging.error('Password,' + passowrd + ', for ' + userID + ' does not exist in the datastore.')
                    return False
                else:
                    return True
        else:
            query.add_filter('password', '=', password)
            if len(list(query.fetch())) == 0:
                logging.error('Password,' + passowrd + ', for ' + userID + ' does not exist in the datastore.')
                return False
            else:
                return True