import dropbox

p = open('text.txt')

def upload_file(file):
    access_token = "R6TLfnzs-P8AAAAAAAAAASFtTu_mFk1CZJJQRT447sAUQfGiF-G15-qEa7I_Okeo"
    file = file
    file_from = file
    file_to = "/test_dropbox/"+file
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,
        mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        upload_file(p)


main()
