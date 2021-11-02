class Assessments:
    def __init__(self, con_string):
        self.connection_string = con_string

    def get_assessment(self) -> (dict, int):
        a = self.connection_string
        # Establish connection to cellar
        # Execute query
        # Format results
        return {"msg": "success"}, 201
