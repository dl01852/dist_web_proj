from DistWebProj import database
from sqlalchemy import ForeignKey
from sqlalchemy.sql import select


class UserAccount(database.Model):

    __tablename__ = 'useraccount'

    id = database.Column(database.INTEGER, primary_key=True)
    username = database.Column(database.String, nullable=False, unique=True)
    password = database.Column(database.String, nullable=False)

    def __init__(self,id, username, password):
        self.id = id
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
    price = database.Column(database.VARCHAR, nullable=True)

    def __init__(self,id,img, brand, model, maxpower, dimensions,price):
        self.id = id
        self.img=img
        self.brand = brand
        self.model = model
        self.maxpower = maxpower
        self.dimensions = dimensions
        self.price=price

    def __repr__(self):
        return "%s\t%s\t%s\t%s\t%s\t%s" % (self.img,self.brand, self.model, self.maxpower, self.dimensions,self.price)

    @staticmethod
    def columns():
        return ["Brand", "Model", "Max Power", "Dimensions", "Price"]

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
    price= database.Column(database.VARCHAR, nullable=True)


    def __init__(self,id,img, model,size,type,speed,voltage,notes, price):
        self.id = id
        self.model = model
        self.size=size
        self.type = type
        self.speed = speed
        self.voltage = voltage
        self.notes = notes
        self.img = img
        self.price=price

    def __repr__(self):
        return "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (self.img,self.size,self.model,self.type,self.speed,self.voltage,self.notes, self.price)

    @staticmethod
    def columns():
        return ["Size","Model","Type","Speed","Voltage","Notes","Price"]

class CPU(database.Model):

    __tablename__ = 'cpu'

    id = database.Column(database.INTEGER,primary_key=True)
    img = database.Column(database.VARCHAR, nullable=True)
    brand = database.Column(database.VARCHAR, nullable=True)
    type = database.Column(database.VARCHAR, nullable=True)
    model = database.Column(database.VARCHAR, nullable=True)
    socket = database.Column(database.VARCHAR, nullable=True)
    core=database.Column(database.VARCHAR, nullable=True)
    operatingfrequency = database.Column(database.VARCHAR, nullable=True)
    thermaldesignpower = database.Column(database.VARCHAR, nullable=True)
    price=database.Column(database.VARCHAR, nullable=True)


    def __init__(self,id,img,brand,type,model,socket,core,operatingfrequency,thermaldesignpower, price):
        self.id = id
        self.img=img
        self.brand = brand
        self.type = type
        self.model = model
        self.socket = socket
        self.core=core
        self.operatingfrequency = operatingfrequency
        self.thermaldesignpoower = thermaldesignpower
        self.price=price

    def __repr__(self):
        return "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" %(self.img,self.brand,self.type,self.model,self.socket,self.core,self.operatingfrequency,self.thermaldesignpower, self.price)

    @staticmethod
    def columns():
        return ["Brand","Type","Mode","Socket","Core","Operating Frequency","Thermal Design Power","Price"]
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
    price = database.Column(database.VARCHAR, nullable=True)

    def __init__(self,id,img,brand,model,interface,manufacturer,type,size,memorytype, price):
        self.id = id
        self.img=img
        self.brand = brand
        self.model = model
        self.interface = interface
        self.manufacturer = manufacturer
        self.type = type
        self.size = size
        self.memorytype = memorytype
        self.price=price

    def __repr__(self):
        return  "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (self.img,self.brand,self.model,self.interface,self.manufacturer,self.type,self.size,self.memorytype, self.price)

    @staticmethod
    def columns():
        return ["Brand","Model","Interface","Manufacturer","Type","Size","Memory Type","Price"]


class MotherBoard(database.Model):

    __tablename__ = 'motherboard'

    id = database.Column(database.INTEGER,primary_key=True)
    img = database.Column(database.VARCHAR, nullable=True)
    brand = database.Column(database.VARCHAR, nullable=True)
    model = database.Column(database.VARCHAR, nullable=True)
    memoryslots=database.Column(database.VARCHAR, nullable=True)
    supportedsocket = database.Column(database.VARCHAR, nullable=True)
    supportedcpu = database.Column(database.VARCHAR, nullable=True)
    expansionslots = database.Column(database.VARCHAR, nullable=True)
    price = database.Column(database.VARCHAR, nullable=True)


    def __init__(self, id,img,brand,model,memoryslots,supportedsocket,supportedcpu,expansionslots,price):
        self.id = id
        self.img=img
        self.brand = brand
        self.model = model
        self.memoryslots=memoryslots
        self.supportedsocket = supportedsocket
        self.supportedcpu = supportedcpu
        self.expansionslots = expansionslots
        self.price=price

    def __repr__(self):
        return "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (self.img,self.brand,self.model, self.memoryslots,self.supportedsocket,self.supportedcpu,self.expansionslots,self.price)

    @staticmethod
    def columns():
        return ["Brand","Model","Memory Slots","Supported Socket","Supported CPU", "Expansion Slots","Price"]


class HardDrive(database.Model):

    __tablename__='harddrive'

    id=database.Column(database.INTEGER,primary_key=True)
    img= database.Column(database.VARCHAR, nullable=True)
    brand= database.Column(database.VARCHAR, nullable=True)
    model= database.Column(database.VARCHAR, nullable=True)
    interface= database.Column(database.VARCHAR, nullable=True)
    capacity= database.Column(database.VARCHAR, nullable=True)
    rpm= database.Column(database.VARCHAR, nullable=True)
    features= database.Column(database.VARCHAR, nullable=True)
    price= database.Column(database.VARCHAR, nullable=True)

    def __init__(self, img, brand, model, interface, capacity, rpm, features, price):

        self.img=img
        self.brand=brand
        self.model=model
        self.interface=interface
        self.capacity=capacity
        self.rpm=rpm
        self.features=features
        self.price=price

    def __repr__(self):
        return "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (self.img,self.brand,self.model,self.interface,self.capacity,self.rpm,self.features,self.price)

    @staticmethod
    def columns():
        return ["Brand","Model","Interface","Capacity","RPM","Features","Price"]


class Cart(database.Model):
    __tablename__ = 'cart'

    id = database.Column(database.Integer, primary_key=True)
    userid = database.Column(database.Integer, ForeignKey(UserAccount.id), nullable=True)
    gpuid = database.Column(database.Integer, ForeignKey(GPU.id), nullable=True)
    cpuid = database.Column(database.Integer, ForeignKey(CPU.id), nullable=True)
    powersupplyid = database.Column(database.Integer, ForeignKey(Powersupply.id), nullable=True)
    ramid = database.Column(database.Integer, ForeignKey(Ram.id),nullable=True)
    motherboardid = database.Column(database.Integer, ForeignKey(MotherBoard.id), nullable=True)
    #harddriveid = database.Column(database.Integer, ForeignKey(HardDrive.id), nullable=True)

    def __init__(self, id, userid, gpuid, cpuid, powersupplyid, ramid, motherboardid, harddriveid):
        self.id = id
        self.userid = userid
        self.gpuid = gpuid
        self.cpuid = cpuid
        self.powersupplyid = powersupplyid
        self.ramid = ramid
        self.motherboardid = motherboardid
        #self.harddriveid = harddriveid


    # class Cart(database.Model):
    #     __tablename__ = 'cart'
    #
    #     id = database.Column(database.INTEGER, primary_key=True)
    #     userid = database.Column(database.INTEGER, ForeignKey(UserAccount.id), nullable=False)
    #     gpuid = database.Column(database.INTEGER, ForeignKey(GPU.id), nullable=True)
    #     cpuid = database.Column(database.INTEGER, ForeignKey(CPU.id), nullable=True)
    #     powersupplyid = database.Column(database.INTEGER, ForeignKey(Powersupply.id), nullable=True)
    #     ramid = database.Column(database.INTEGER, ForeignKey(Ram.id), nullable=True)
    #     motherboardid = database.Column(database.INTEGER, ForeignKey(MotherBoard.id), nullable=True)
    #     #harddriveid = database.Column(database.INTEGER, ForeignKey(HardDrive.id), nullable=True)
    #
    #     # cpu = database.relationship('cpu',foreign_keys='cpu.id')
    #     def __init__(self, userid, gpuid, cpuid, powersupplyid, ramid, motherboardid, harddriveid):
    #         self.userid = userid
    #         self.gpuid = gpuid
    #         self.cpuid = cpuid
    #         self.powersupplyid = powersupplyid
    #         self.ram_id = ramid
    #         self.motherboardid = motherboardid
    #         self.harddrive_id = harddriveid
    #
    #     def __repr__(self):
    #         return "%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % (
    #         self.userid, self.gpuid, self.cpuid, self.powersupplyid, self.ram_id, self.motherboardid, self.harddrive_id)
    #
    #     @staticmethod
    #     def columns():
    #         return ["GPU", "CPU", "PowerSupply", "RAM", "Motherboard", "Hard Drive"]
