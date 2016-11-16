from DistWebProj import database


class User(database.Model):

    __tablename__ = 'useraccount'

    id = database.Column(database.INTEGER, primary_key=True)
    username = database.Column(database.String, nullable=False, unique=True)
    password = database.Column(database.String, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "%s:%s" % (self.username, self.password)


class Powersupply(database.Model):

    __tablename__ = 'powersupply'

    id = database.Column(database.INTEGER, primary_key=True)
    img = database.Column(database.VARCHAR, nullable=True)
    brand = database.Column(database.VARCHAR, nullable=True)
    model = database.Column(database.VARCHAR, nullable=True)
    maxpower= database.Column(database.VARCHAR, nullable=True)
    dimensions = database.Column(database.VARCHAR, nullable=True)

    def __init__(self,img, brand, model, maxpower, dimensions):
        self.img=img
        self.brand = brand
        self.model = model
        self.maxpower = maxpower
        self.dimensions = dimensions

    def __repr__(self):
        return "%s\t%s\t%s\t%s\t%s" % (self.img,self.brand, self.model, self.maxpower, self.dimensions)


class Ram(database.Model):

    __tablename__ = 'ram'

    id = database.Column(database.INTEGER,primary_key=True)
    img = database.Column(database.VARCHAR, nullable=True)
    model = database.Column(database.VARCHAR, nullable=True)
    size = database.Column(database.VARCHAR, nullable=True)
    type = database.Column(database.VARCHAR, nullable=True)
    speed = database.Column(database.VARCHAR, nullable=True)
    voltage = database.Column(database.VARCHAR, nullable=True)
    notes = database.Column(database.VARCHAR, nullable=True)


    def __init__(self,img, model,size,type,speed,voltage,notes):


        self.model = model
        self.size=size
        self.type = type
        self.speed = speed
        self.voltage = voltage
        self.notes = notes
        self.img = img

    def __repr__(self):
        return "%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % (self.img,self.size,self.model,self.type,self.speed,self.voltage,self.notes)

class CPU(database.Model):

    __tablename__ = 'cpu'

    id = database.Column(database.INTEGER,primary_key=True)
    img = database.Column(database.VARCHAR, nullable=True)
    brand = database.Column(database.VARCHAR, nullable=True)
    type = database.Column(database.VARCHAR, nullable=True)
    model = database.Column(database.VARCHAR, nullable=True)
    socket = database.Column(database.VARCHAR, nullable=True)
    operatingfrequency = database.Column(database.VARCHAR, nullable=True)
    thermaldesignpower = database.Column(database.VARCHAR, nullable=True)

    def __init__(self,img,brand,type,model,socket,operatingfrequency,thermaldesignpower):
        self.img=img
        self.brand = brand
        self.type = type
        self.model = model
        self.socket = socket
        self.operatingfrequency = operatingfrequency
        self.thermaldesignpoower = thermaldesignpower

    def __repr__(self):
        return "%s\t%s\t%s\t%s\t%s\t%s\t%s\t" %(self.img,self.brand,self.type,self.model,self.socket,self.operatingfrequency,self.thermaldesignpower)

class GPU(database.Model):

    __tablename__ = 'gpu'

    id = database.Column(database.INTEGER,primary_key=True)
    img=database.Column(database.VARCHAR, nullable=True)
    brand = database.Column(database.VARCHAR, nullable=True)
    model = database.Column(database.VARCHAR, nullable=True)
    interface = database.Column(database.VARCHAR, nullable=True)
    manufacturer = database.Column(database.VARCHAR, nullable=True)
    type = database.Column(database.VARCHAR, nullable=True)
    size = database.Column(database.VARCHAR, nullable=True)
    memorytype = database.Column(database.VARCHAR, nullable=True)

    def __init__(self,img,brand,model,interface,manufacturer,type,size,memorytype):
        self.img=img
        self.brand = brand
        self.model = model
        self.interface = interface
        self.manufacturer = manufacturer
        self.type = type
        self.size = size
        self.memorytype = memorytype

    def __repr__(self):
        return  "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % (self.img,self.brand,self.model,self.interface,self.manufacturer,self.type,self.size,self.memorytype)





class MotherBoard(database.Model):

    __tablename__ = 'motherboard'

    id = database.Column(database.INTEGER,primary_key=True)
    img = database.Column(database.VARCHAR, nullable=True)
    brand = database.Column(database.VARCHAR, nullable=True)
    model = database.Column(database.VARCHAR, nullable=True)
    supportedsocket = database.Column(database.VARCHAR, nullable=True)
    supportedcpu = database.Column(database.VARCHAR, nullable=True)
    expansionslots = database.Column(database.VARCHAR, nullable=True)


    def __init__(self,img,brand,model,supportedsocket,supportedcpu,expansionslots):
        self.img=img
        self.brand = brand
        self.model = model
        self.supportedsocket = supportedsocket
        self.supportedcpu = supportedcpu
        self.expansionslots = expansionslots

    def __repr__(self):
        return "%s\t%s\t%s\t%s\t%s\t%s\t" (self.img,self.brand,self.model,self.supportedsocket,self.supportedcpu,self.expansionslots)





