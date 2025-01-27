import SWEScrape.swescrape
import SWESpreadsheet.swespreadsheet
import os

def main():
    swe_job = SWEScrape.swescrape.SWEJobs()
    #SWESpreadsheet.swespreadsheet.load_excel()
    json_file_name = input("Enter a json file name: ")
    if (os.path.isfile(f"{json_file_name}.json")):
        print("Has file")
    else:
        swe_job.load_jobs(json_file_name)
def
if __name__ == '__main__':
    main()