from DistWebProj import database


class UserAccount(database.Model):

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
    price = database.Column(database.VARCHAR, nullable=True)

    def __init__(self,img, brand, model, maxpower, dimensions,price):
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
        return ["Brand", "Model", "Max Power", "Dimensions"]

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


    def __init__(self,img, model,size,type,speed,voltage,notes, price):
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


    def __init__(self,img,brand,type,model,socket,core,operatingfrequency,thermaldesignpower, price):
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

    def __init__(self,img,brand,model,interface,manufacturer,type,size,memorytype, price):
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


    def __init__(self,img,brand,model,memoryslots,supportedsocket,supportedcpu,expansionslots,price):
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

# class Tower(database.Model):
#
#     __tablename__ = 'tower'
#
#     id= database.Column(database.INTEGER,primary_key=True)
#     img = database.Column(database.VARCHAR, nullable=True)
#     brand = database.Column(database.VARCHAR, nullable=True)
#     model = database.Column(database.VARCHAR, nullable=True)
#     type = database.Column(database.VARCHAR, nullable=True)
#     compatibility = database.Column(database.VARCHAR, nullable=True)
#     expansionslots = database.Column(database.VARCHAR, nullable=True)
#     gpusupport = database.Column(database.VARCHAR, nullable=True)
#     dimensions = database.Column(database.VARCHAR, nullable=True)
#     weight = database.Column(database.VARCHAR, nullable=True)
#     price = database.Column(database.VARCHAR, nullable=True)
#
#     def __init__(self, img, brand, model, type, compatibility, expansionslots, gpusupport, dimensions, weight, price):
#         self.img=img
#         self.brand=brand
#         self.model=model
#         self.type=type
#         self.compatibility=compatibility
#         self.expansionslots=expansionslots
#         self.gpusupport=gpusupport
#         self.dimensions=dimensions
#         self.weight=weight
#         self.price=price
#
#     def __repr__(self):
#         return "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % (self.img, self.brand, self.model,self.type, self.compatibility, self.expansionslots, self.gpusupport, self.dimensions, self.weight, self.price)
#
#
#     @staticmethod
#     def columns():
#         return ["Brand", "Model", "Type", "Compatibility", "ExpansionSlots", "GpuSupport", "Dimensions", "Weight", "Price"]

class HardDrive(database.Model):

    __tablename__='harddrive'

    id=database.Column(database.INTEGER,primary_key=True)
    img= database.Column(database.VARCHAR, nullable=True)
    brand= database.Column(database.VARCHAR, nullable=True)
    series= database.Column(database.VARCHAR, nullable=True)
    model= database.Column(database.VARCHAR, nullable=True)
    interface= database.Column(database.VARCHAR, nullable=True)
    capacity= database.Column(database.VARCHAR, nullable=True)
    rpm= database.Column(database.VARCHAR, nullable=True)
    dimensions= database.Column(database.VARCHAR, nullable=True)
    features= database.Column(database.VARCHAR, nullable=True)
    price= database.Column(database.VARCHAR, nullable=True)

    def __init__(self, img, brand, series, model, interface, capacity, rpm, dimensions, features, price):
        self.img=img
        self.brand=brand
        self.series=series
        self.model=model
        self.interface=interface
        self.capacity=capacity
        self.rpm=rpm
        self.dimensions=dimensions
        self.features=features
        self.price=price

    def __repr__(self):
        return "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % (self.img,self.brand,self.series,self.model,self.interface,self.capacity,self.rpm,self.dimensions,self.features,self.price)

    @staticmethod
    def columns():
        return ["Brand","Series","Model","Interface","Capacity","RPM","Dimensions","Features","Price"]

# class SSD(database.Model):
#
#     __tablename__='ssd'
#
#     id=database.Column(database.INTEGER,primary_key=True)
#     img= database.Column(database.VARCHAR, nullable=True)
#     brand= database.Column(database.VARCHAR, nullable=True)
#     series= database.Column(database.VARCHAR, nullable=True)
#     model= database.Column(database.VARCHAR, nullable=True)
#     capacity= database.Column(database.VARCHAR, nullable=True)
#     interface= database.Column(database.VARCHAR, nullable=True)
#     controller= database.Column(database.VARCHAR, nullable=True)
#     speed= database.Column(database.VARCHAR, nullable=True)
#     features= database.Column(database.VARCHAR, nullable=True)
#     powerconsume= database.Column(database.VARCHAR, nullable=True)
#     dimensions= database.Column(database.VARCHAR, nullable=True)
#     price= database.Column(database.VARCHAR, nullable=True)
#
#     def __init__(self, img, brand, series, model, capacity, interface, controller, speed, features, powerconsume, dimensions, price):
#         self.img=img
#         self.brand=brand
#         self.series=series
#         self.model=model
#         self.capacity=capacity
#         self.interface=interface
#         self.controller=controller
#         self.speed=speed
#         self.features=features
#         self.powerconsume=powerconsume
#         self.dimensions=dimensions
#         self.price=price
#
#     def __repr__(self):
#         return "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % (self.img, self.brand, self.series, self.model, self.capacity, self.interface, self.controller, self.speed, self.features, self.powerconsume, self.dimensions, self.price)
#
#     @staticmethod
#     def columns():
#         return ["Brand","Series","Model","Capacity","Interface","Controller","Speed","Features","PowerConsumption","Dimensions","Price"]
#
# class Cooler(database.Model):
#
#     __tablename__='cooler'
#
#
#     id=database.Column(database.INTEGER,primary_key=True)
#     img= database.Column(database.VARCHAR, nullable=True)
#     brand= database.Column(database.VARCHAR, nullable=True)
#     series= database.Column(database.VARCHAR, nullable=True)
#     model= database.Column(database.VARCHAR, nullable=True)
#     type= database.Column(database.VARCHAR, nullable=True)
#     compatibility= database.Column(database.VARCHAR, nullable=True)
#     connector= database.Column(database.VARCHAR, nullable=True)
#     fandimensions=database.Column(database.VARCHAR, nullable=True)
#     sinkdimensions= database.Column(database.VARCHAR, nullable=True)
#     features= database.Column(database.VARCHAR, nullable=True)
#     price= database.Column(database.VARCHAR, nullable=True)
#
#     def __init__(self,img,brand,series,model,type,compatibility,connector, fandimensions,sinkdimensions,features,price):
#         self.img = img
#         self.brand = brand
#         self.series = series
#         self.model = model
#         self.type=type
#         self.compatibility=compatibility
#         self.connector=connector
#         self.fandimensions=fandimensions
#         self.sinkdimensdons=sinkdimensions
#         self.features=features
#         self.price=price
#
#     def __repr__(self):
#         return "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t" % (self.img, self.brand, self.series, self.model, self.type, self.compatibility, self.connector,self.fandimensions, self.sinkdimensions, self.features, self.price)
#
#     @staticmethod
#     def columns():
#         return ["Brand","Series","Model","Type","Compatibility","Connector","Fan Dimensions","Sink Dimensions","Features" ,"Price"]
#
#
#
