from extractor import Extractor

def run():
    e = Extractor()
    e.connect()
    e.upload_sample_file()
    e.show_dir_contents()
    e.retrive_file()
    e.make_csv()
    e.upload_to_warehouse()
    e.close_conn()

if __name__ == "__main__":
    run()