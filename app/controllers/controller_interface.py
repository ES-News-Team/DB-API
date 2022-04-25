
class IController:
    """ Basic Controller interface """
    
    def list(self):
        """ Lists all content from a table."""
        pass


    def retrieve(self, id: str):
        """ Retrieves the content from a row where id == primary-key"""
        pass


    def create(self, *args, **kwargs):
        """ Creates a new row in a table."""
        pass


    def update(self, id: str, *args, **kwargs):
        """ Updates the content of a row, where id == primary-key."""
        pass


    def delete(self, id: str):
        """ Deletes a row from a table, where id == primary-key."""
        pass


class IUserController(IController):

    def retrieve(self, email: str):
        """ Retrieves the content from a row where email == User.email"""
        pass
