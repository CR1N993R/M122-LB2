import pysftp


def upload(filename, ftp_address, ftp_username, ftp_password):
    if len(ftp_address) > 0 and len(ftp_username) > 0 and len(ftp_password) > 0:
        with pysftp.Connection(ftp_address, username=ftp_username, password=ftp_password) as sftp:
            sftp.put(filename, filename)
