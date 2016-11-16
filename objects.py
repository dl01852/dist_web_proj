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


class Ram(database.Model):

    _tablename_ = 'ram'

    id = database.Column(database.INTEGER,primary_key=True)
    model = database.Column(database.String)
    type = database.Column(database.String)
    speed = database.Column(database.String)
    voltage = database.Column(database.String)
    notes = database.Column(database.String)

    def _init_(self, id, model,type,speed,voltage,notes):
        self.model = model
        self.type = type
        self.speed = speed
        self.voltage = voltage
        self.notes = notes

    def __repr__(self):
        return "%d\t%s\t%s\t%s\t%s\t%s"(self.id,self.model,self.type,self.speed,self.voltage,self.notes)

class CPU(database.Model):

    _tablename_ = 'cpu'

    id = database.Column(database.INTEGER,primary_key=True)
    brand = database.column(database.String)
    type = database.column(database.String)
    model = database.column(database.String)
    socket = database.column(database.String)
    operatingFrequency = database.column(database.String)
    thermalDesignPower = database.column(database.String)

    def __init__(self,id,brand,type,model,socket,operatingfrequency,thermaldesignpower):
        self.id = id
        self.brand = brand
        self.type = type
        self.model = model
        self.socket = socket
        self.operatingfrequency = operatingfrequency
        self.thermaldesignpoower =thermaldesignpower

    def __repr__(self):
        return "%d\t%s\t%s\t%s\t%s\t%s\t%s" (self.id,self.brand,self.type,self.model,self.socket,self.operatingfrequency,self.thermaldesignpower)

class GPU(database.Model):

    _tablename_ = 'gpu'

    id = database.Column(database.INTEGER,primary_key=True)

    brand = database.column(database.String)
    model = database.column(database.String)
    interface = database.column(database.String)
    manufacturer = database.column(database.String)
    type = database.column(database.String)
    size = database.column(database.String)
    memoryType = database.column(database.String)

    def _init_(self,id,brand,model,interface,manufacturer,type,size,memorytype):
        self.id = id
        self.brand = brand
        self.model = model
        self.interface = interface
        self.manufacturer = manufacturer
        self.type = type
        self.size = size
        self.memorytype = memorytype

    def _repr_(self):
        return  "%d\t%s\t%s\t%s\t%s\t%s\t%s\s" (self.id,self.brand,self.model,self,interface,self.manufacturer,self.type,self.size,self.memorytype)


class PowerSupply(database.Model):

    _tablename_ = 'powersupply'

    id = database.Column(database.INTEGER,primary_key=True)
    brand = database.column(database.String)
    model = database.column(database.String)
    maxPower = database.column(database.String)
    dimensions = database.column(database.String)

    def __init__(self,id,brand,model,maxpower,dimensions):
        self.id = id
        self.brand = brand
        self.model = model
        self.maxpower = maxpower
        self.dimensions = dimensions

    def __repr__(self):
        return "%d\t%s\t%s\t%s\t%s\t%s" (self.id,self.brand,self.model,self.maxpower,self.dimensions)

    def test(self):
        return "%d"(self.brand)




class MotherBoard:

    _tablename_ = 'motherboard'

    id = database.Column(database.INTEGER,primary_key=True)
    brand = database.column(database.String)
    model = database.column(database.String)
    supportedsocket = database.column(database.String)
    supportedcpu = database.column(database.String)
    expansionSlots = database.column(database.String)


    def __init__(self,id,brand,model,supportedsocket,supportedcpu,expansionslots):
        self.id = id
        self.brand = brand
        self.model = model
        self.supportedSocket = supportedsocket
        self.supportedCPU = supportedcpu
        self.expansionslots = expansionslots

    def __repr__(self):
        return "%d\t%s\t%s\t%s\t%s\t%s" (self.id,self.brand,self.model,self.supportedsocket,self.supportedcpu,self.expansionslots)





