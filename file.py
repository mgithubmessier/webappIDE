class File:
    def __init__(self, key, filename, lang, username, text):
	self.key = key
        self.filename = filename
        self.lang = lang
	self.username = username
	self.text = text

    def toString(self):
        return self.key + " " + self.filename + " " + self.lang + " " + self.username + self.text

