class uType:

    department = 'Engineering'
    subjects = ['Calc','Programming','BES','CPE-414','ECE-412']

    def init(obj, fname, mname, lname, address):

        obj.Fname = fname
        obj.Mname = mname
        obj.Lname = lname
        obj.Aaddress = address
        obj.email = f'{obj.Aaddress.lower()}ijaytanza@gmail.com'
        obj.courses = ['Proj']

    def getFname(obj):
        return obj.Fname

    def getMname(obj):
        return obj.Mname

    def getLname(obj):
        return obj.Lname

    def getAaddress(obj):
        return obj.Aaddress

    def welcome(obj):
        return f'Welcome {obj.Fname} {obj.Mname} {obj.Lname} {obj.email}'

    def registerSubject(obj,*sub):
        for s in sub:
            if s not in uType.subjects:
                print(f'{s} is not offered!')
            if s in uType.subjects and s not in obj.courses:
                print(f'{s} is on the subject offered!')
                obj.courses.append(s)

user1 = uType()
user2 = uType()

user1.init('Jay Michael','Molde', 'Tanza', 'Mactan')
user2.init('Frenah Marie','Silawan', 'Tanza', 'Soong')

#print(user2.welcome())

user1.registerSubject('BES','PE','CALC','ME')
print(user1.courses)