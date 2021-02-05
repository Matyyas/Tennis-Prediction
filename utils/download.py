import logging
import os.path as osp
import os
import pandas as pd 
import zipfile

from glob import glob
from urllib.request import urlopen 

logging.getLogger().setLevel('INFO')

BASE_URL = 'http://tennis-data.co.uk'
DATA_DIR = "tennis_data"
ATP_DIR = './{}/ATP'.format(DATA_DIR)
WTA_DIR = './{}/WTA'.format(DATA_DIR)

ATP_URLS = [BASE_URL + "/%i/%i.zip" % (i,i) for i in range(2000,2019)]
WTA_URLS = [BASE_URL + "/%iw/%i.zip" % (i,i) for i in range(2007,2019)]

def download_file(url_str, path):
        url = urlopen(url_str)
        output = open(path, 'wb')       
        output.write(url.read())
        output.close()  
    
def extract_file(archive_path, target_dir):
        zip_file = zipfile.ZipFile(archive_path, 'r')
        zip_file.extractall(target_dir)
        zip_file.close()

def build_dataframes():
        os.makedirs(osp.join(ATP_DIR, 'archives'), exist_ok=True)
        os.makedirs(osp.join(WTA_DIR, 'archives'), exist_ok=True)

        for files, directory in ((ATP_URLS, ATP_DIR), (WTA_URLS, WTA_DIR)):
                for dl_path in files:
                        logging.info("downloading & extracting file %s", dl_path)
                        archive_path = osp.join(directory, 'archives', osp.basename(dl_path))
                        download_file(dl_path, archive_path)
                        extract_file(archive_path, directory)
        
        ATP_FILES = sorted(glob("%s/*.xls*" % ATP_DIR))
        WTA_FILES = sorted(glob("%s/*.xls*" % WTA_DIR))

        # Issue when loading '.xlsx' file, must use 'openpyxl' in this case
        df_atp = pd.concat([pd.read_excel(f) if f[-1]=='s' else pd.read_excel(f, engine='openpyxl') for f in ATP_FILES], ignore_index=True)
        df_wta = pd.concat([pd.read_excel(f) if f[-1]=='s' else pd.read_excel(f, engine='openpyxl') for f in WTA_FILES], ignore_index=True)

        logging.info("%i matches ATP in df_atp", df_atp.shape[0])
        logging.info("%i matches WTA in df_wta", df_wta.shape[0])
        return df_atp, df_wta

