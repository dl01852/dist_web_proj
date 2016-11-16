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
    Model = database.Column(database.String)
    Type = database.Column(database.String)
    Speed = database.Column(database.String)
    Voltage = database.Column(database.String)
    Notes = database.Column(database.String)

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
    Brand = database.column(database.String)
    Type = database.column(database.String)
    Model = database.column(database.String)
    Socket = database.column(database.String)
    OperatingFrequency = database.column(database.String)
    ThermalDesignPower = database.column(database.String)

    def __init__(self,id,Brand,Type,Model,Socket,OperatingFrequency,ThermalDesignPower):
        self.id = id
        self.Brand = Brand
        self.Type = Type
        self.Model = Model
        self.Socket = Socket
        self.OperatingFrequency = OperatingFrequency
        self.ThermalDesignPower =ThermalDesignPower

    def __repr__(self):
        return "%d\t%s\t%s\t%s\t%s\t%s\t%s" (self.id,self.Brand,self.Type,self.Model,self.Socket,self.OperatingFrequency,self.ThermalDesignPower)

class GPU(database.Model):

    _tablename_ = 'GPU'

    id = database.Column(database.INTEGER,primary_key=True)

    Brand = database.column(database.String)
    Model = database.column(database.String)
    Interface = database.column(database.String)
    Manufacturer = database.column(database.String)
    Type = database.column(database.String)
    Size = database.column(database.String)
    MemoryType = database.column(database.String)

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
    Brand = database.column(database.String)
    Model = database.column(database.String)
    MaxPower = database.column(database.String)
    Dimensions = database.column(database.String)

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
    Brand = database.column(database.String)
    Model = database.column(database.String)
    SupportedSocket = database.column(database.String)
    SupportedCPU = database.column(database.String)
    ExpansionSlots = database.column(database.String)


    def __init__(self,id,Brand,Model,SupportedSocket,SupportedCPU,ExpansionSlots):
        self.id = id
        self.Brand = Brand
        self.Model = Model
        self.SupportedSocket = SupportedSocket
        self.SupportedCPU = SupportedCPU
        self.ExpansionSlots = ExpansionSlots

    def __repr__(self):
        return "%d\t%s\t%s\t%s\t%s\t%s" (self.id,self.Brand,self.Model,self.SupportedSocket,self.SupportedCPU,self.ExpansionSlots)





