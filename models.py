
class Recipe():

    def __init__(self, id, title, description, time, servings, img, category, author, url_video):

        self.id = id
        self.title = title
        self.description = description
        self.preparation_time = time
        self.preparation_time_unit =  'Minutos'
        self.servings = servings
        self.servings_unit = 'Pessoas'
        self.img = img
        self.category = category
        self.author_name = author
        self.video = url_video
                                

class Categoty():

    def __init__(self, id, category_name):

        self.id = id
        self.category = category_name