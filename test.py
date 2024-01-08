class ModelBase:
    id: int
    name: str

    def get_id(self):
        return self.id


class User(ModelBase):
    pass



my_user = User()



