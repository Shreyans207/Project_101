import os 
import dropbox

class TransferData : 
    def __init__(self,access_token,) : 
        self.access_token = access_token
         
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                    
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                   
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main() : 
    access_token = 'dRLZ440pW3MAAAAAAAAAAYpJGomEmG8dneeaVLyPLl-z1pvLH9U0LijkAY0iGl6u'
    db = TransferData(access_token)

    file_from = input('Path of the file you want to move to the dropbox : ')
    file_to = input('Path of the Destination of the file inside the dropbox : ')

    db.upload_file(file_from , file_to)

main()

