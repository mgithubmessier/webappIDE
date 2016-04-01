import dataset
from file import File

class FileDao:
    def __init__(self):
        self.connectString = 'mysql://root:@127.0.0.1/users'
        self.db = dataset.connect(self.connectString)
        self.table = self.db['webapp_files']

    def rowToFile(self,row):
        file = File(row['key'],row['filename'],row['lang'],row['username'],row['text'])
        return file

    def fileToRow(self,file):
        row = dict(key=file.key, filename=file.filename, username=file.username, text =file.text)
        return row

    def selectByFileName(self,filename):
        rows   = self.table.find(filename=filename)
        result = None
        if (rows is None):
            print('FileDao:selectByFileName failed to find file with ' + filename)
        else:
            count = 0
            for row in rows:
                if (count > 0):
                    print('FileDao:selectByFileName more than one file selected with ' + filename)
                    return None
                else:
                    result = self.rowToFile(row)
                    count = count + 1
        return result

    def selectAll(self):
        table = self.db['webapp_files']
        rows   = table.all()

        result = []
        for row in rows:
            result.append(self.rowToFile(row))

        return result
        
    def insert(self,file):
        self.table.insert(self.fileToRow(file))
        self.db.commit()

    def update(self,file):
        self.table.delete(filename=filename)
        self.table.insert(self.fileToRow(file))
        self.db.commit()

    def delete(self,file):
        self.table.delete(filename=file.filename)
        self.db.commit()

    def populate(self):
        self.table.delete()
        
