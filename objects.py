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

    _tablename_ = 'RAM'

    id = database.Column(database.INTEGER,primary_key=True)
    model = database.Column(database.String)
    type = database.Column(database.String)
    speed = database.Column(database.String)
    voltage = database.Column(database.String)
    notes = database.Column(database.String)

    def _init_(self, id, Model,Type,Speed,Voltage,Notes):
        self.Model = Model
        self.Type = Type
        self.Speed = Speed
        self.Voltage = Voltage
        self.Notes = Notes

    def __repr__(self):
        return "%d\t%s\t%s\t%s\t%s\t%s"(self.id,self.Model,self.Type,self.Speed,self.Voltage,self.Notes)

class CPU(database.Model):

    _tablename_ = 'CPU'

    id = database.Column(database.INTEGER,primary_key=True)
    brand = database.column(database.String)
    type = database.column(database.String)
    model = database.column(database.String)
    socket = database.column(database.String)
    operatingFrequency = database.column(database.String)
    thermalDesignPower = database.column(database.String)

    def __init__(self,id,Brand,Type,Model,Socket,OperatingFrequency,ThermalDesignPower):
        self.id = id
        self.brand = Brand
        self.type = Type
        self.model = Model
        self.socket = Socket
        self.operatingFrequency = OperatingFrequency
        self.thermalDesignPower =ThermalDesignPower

    def __repr__(self):
        return "%d\t%s\t%s\t%s\t%s\t%s\t%s" (self.id,self.Brand,self.Type,self.Model,self.Socket,self.OperatingFrequency,self.ThermalDesignPower)

class GPU(database.Model):

    _tablename_ = 'GPU'

    id = database.Column(database.INTEGER,primary_key=True)

    brand = database.column(database.String)
    model = database.column(database.String)
    interface = database.column(database.String)
    manufacturer = database.column(database.String)
    type = database.column(database.String)
    size = database.column(database.String)
    memoryType = database.column(database.String)

    def _init_(self,id,Brand,Model,Interface,Manufacturer,Type,Size,MemoryType):
        self.id = id
        self.Brand = Brand
        self.Model = Model
        self.Interface = Interface
        self.Manufacturer = Manufacturer
        self.Type = Type
        self.Size = Size
        self.MemoryType = MemoryType

    def _repr_(self):
        return  "%d\t%s\t%s\t%s\t%s\t%s\t%s\s" (self.id,self.Brand,self.Model,self.Interface,self.Manufacturer,self.Type,self.Size,self.MemoryType)


class PowerSupply(database.Model):

    _tablename_ = 'PowerSupply'

    id = database.Column(database.INTEGER,primary_key=True)
    brand = database.column(database.String)
    model = database.column(database.String)
    maxPower = database.column(database.String)
    dimensions = database.column(database.String)

    def __init__(self,id,Brand,Model,MaxPower,Dimensions):
        self.id = id
        self.Brand = Brand
        self.Model = Model
        self.MaxPower = MaxPower
        self.Dimensions = Dimensions

    def __repr__(self):
        return "%d\t%s\t%s\t%s\t%s\t%s" (self.id,self.Brand,self.Model,self.MaxPower,self.Dimensions)

    def test(self):
        return "%d"(self.Brand)




class MotherBoard:
    id = database.Column(database.INTEGER,primary_key=True)
    brand = database.column(database.String)
    model = database.column(database.String)
    supportedsocket = database.column(database.String)
    supportedcpu = database.column(database.String)
    expansionSlots = database.column(database.String)


    def __init__(self,id,Brand,Model,SupportedSocket,SupportedCPU,ExpansionSlots):
        self.id = id
        self.Brand = Brand
        self.Model = Model
        self.SupportedSocket = SupportedSocket
        self.SupportedCPU = SupportedCPU
        self.ExpansionSlots = ExpansionSlots

    def __repr__(self):
        return "%d\t%s\t%s\t%s\t%s\t%s" (self.id,self.Brand,self.Model,self.SupportedSocket,self.SupportedCPU,self.ExpansionSlots)





