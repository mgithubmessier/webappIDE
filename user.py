class User:
    def __init__(self, key, userid, password, admin):
	self.key = key
        self.userid = userid
        self.password = password
	self.admin = admin

    def toString(self):
        return self.key + " " + self.userid + " " + self.admin
