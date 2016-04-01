import dataset
from user import User

class UserDao:
    def __init__(self):
        self.connectString = 'mysql://root:@127.0.0.1/users'
        self.db = dataset.connect(self.connectString)
        self.table = self.db['webapp_users']

    def rowToUser(self,row):
        user = User(row['key'],row['userid'],row['password'],row['admin'])
        return user

    def userToRow(self,user):
        row = dict(key=user.key, userid=user.userid, password=user.password, admin =user.admin)
        return row

    def selectByUserid(self,userid):
        rows   = self.table.find(userid=userid)
        result = None
        if (rows is None):
            print('UserDao:selectByUserid failed to find user with ' + userid)
        else:
            count = 0
            for row in rows:
                if (count > 0):
                    print('UserDao:selectByUserid more than one user selected with ' + userid)
                    return None
                else:
                    result = self.rowToUser(row)
                    count = count + 1
        return result

    def selectAll(self):
        table = self.db['webapp_users']
        rows   = table.all()

        result = []
        for row in rows:
            result.append(self.rowToUser(row))

        return result
        
    def insert(self,user):
        self.table.insert(self.userToRow(user))
        self.db.commit()

    def update(self,user):
        self.table.delete(userid=user.userid)
        self.table.insert(self.userToRow(user))
        self.db.commit()

    def delete(self,user):
        self.table.delete(userid=user.userid)
        self.db.commit()

    def populate(self):
        self.table.delete()
        self.table.insert(self.userToRow(User('wjsunve8xpoo7', 'dmisiaszek', 'admin','true')))
        self.table.insert(self.userToRow(User('wjsunve7xpoo7', 'bdimattia', 'admin','true')))
        self.table.insert(self.userToRow(User('wjsunve6xpoo7', 'bpowers','admin','true')))
        self.table.insert(self.userToRow(User('wjsunve4xpoo7', 'mmessier','admin','true')))
        
