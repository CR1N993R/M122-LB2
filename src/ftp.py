import pysftp


def upload(filename, local_path, ftp_address, ftp_username, ftp_password, port, ftp_path):
    if len(ftp_address) > 0 and len(ftp_username) > 0 and len(ftp_password) > 0:
        print("Uploading file to FTP...")
        try:
            with pysftp.Connection(host=ftp_address, username=ftp_username, password=ftp_password, port=port) as sftp:
                ftp_file = filename
                if len(ftp_path) > 0:
                    if not sftp.exists(ftp_path):
                        sftp.mkdir(ftp_path)
                    ftp_file = ftp_path + "/" + filename
                sftp.put(local_path, ftp_file)
            print("Done")
        except Exception as e:
            print(e)
            print("Failed to connect to Server")
        return
    print("FTP Skipped")
