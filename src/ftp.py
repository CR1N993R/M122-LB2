import pysftp


def upload(filename, ftp_address, ftp_username, ftp_password, port):
    if len(ftp_address) > 0 and len(ftp_username) > 0 and len(ftp_password) > 0:
        print("Uploading file to FTP...")
        try:
            with pysftp.Connection(ftp_address, username=ftp_username, password=ftp_password, port=port) as sftp:
                sftp.put(filename, filename)
            print("Done")
        except:
            print("Failed to connect to Server")
        return
    print("FTP Skipped")
