import ftplib
import zipfile
import io
import pandas as pd

class Extractor:
	def __init__ (self):
		# FTP login credentials
		self.host = "ftp.dlptest.com"
		self.user = "dlpuser"
		self.password = "rNrKYTX9g7z3RgJRmxWuGHbeu"
		self.ftp_filepath = "peoples.zip"
		self.upload_filepath = "upload_to_ftp/peoples.zip"

	def connect(self):
		# Connect to the FTP server
		self.ftp_server = ftplib.FTP(self.host, self.user, self.password)

	def show_dir_contents(self):
		# print contents of ftp directory
		self.ftp_server.dir()
	
	def upload_sample_file(self, upload_name="peoples.zip"):
		# optionally upload a sample file
		with open(self.upload_filepath, 'rb') as f:
			self.ftp_server.storbinary(f"STOR {upload_name}", f)

	def retrive_file(self):
		# Retrieve the .zip file from the FTP server
		zip_file = io.BytesIO()
		self.ftp_server.retrbinary("RETR " + self.ftp_filepath, zip_file.write)

		# Extract the files from the .zip file
		with zipfile.ZipFile(zip_file) as self.zf:
			self.zf.extractall('downloads/')
	
	def make_csv(self):
		# Concatenate the extracted files into a single .csv
		df = pd.concat([pd.read_csv(f'downloads/{f}') for f in self.zf.namelist()])
		self.data_warehouse_name = "data.csv"
		df.to_csv(f"./downloads/merged_data/{self.data_warehouse_name}", index=False)

	def upload_to_warehouse(self):
		# TODO TBD
		print(f"{self.data_warehouse_name} is uploading")

	def close_conn(self):
		# Close the FTP connection
		self.ftp_server.quit()
