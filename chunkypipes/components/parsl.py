from chunkypipes.components import BasePipeline


class ParslPipeline(BasePipeline):
    pass


class Software(object):
    _id = 0
    _apps = list()

    def __init__(self, name, path):
        pass

    def prep(self, *args, **kwargs):
        pass


class Data(object):
    _id = 0
    _data = dict()

    def __new__(cls, path, tmp=False):
        if path in cls._data:
            return cls._data[path]
        return super(Data, cls).__new__(cls, path)

    def __init__(self, path, tmp=None):
        Data._data[path] = self
        self.path = path
        # TODO Implement tmp

    def as_input(self):
        return self

    def as_output(self):
        return self

    def __str__(self):
        return self.path

    def __unicode__(self):
        return self.__str__()


class Parameter(object):
    def __init__(self, *args, **kwargs):
        pass