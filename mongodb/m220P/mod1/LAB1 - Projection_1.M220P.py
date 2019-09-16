def get_movies_by_country(countries):
    """
    Finds and returns movies by country.
    Returns a list of dictionaries, each dictionary contains a title and an _id.
    """
    try:

        """
        Ticket: Projection

        Write a query that matches movies with the countries in the "countries"
        list, but only returns the title and _id of each movie.

        Remember that in MongoDB, the $in operator can be used with a list to
        match one or more values of a specific field.
        """

        # TODO: Projection
        # Find movies matching the "countries" list, but only return the title
        # and _id. Do not include a limit in your own implementation, it is
        # included here to avoid sending 46000 documents down the wire.
        
        '''
        # original return
        return list(db.movies.find().limit(1))


        '''
        # My Return statement
        return list(db.movies.find( { "countries": {"$in": [countries]}}, { "title": 1. "_id" } ))


    except Exception as e:
        return e


