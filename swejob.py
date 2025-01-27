import json

import SWEScrape.swescrape
import SWESpreadsheet.swespreadsheet
import webbrowser

def main():
    swe_job = SWEScrape.swescrape.SWEJobs()
    json_file_name = input("Enter a json file name: ")
    swe_job.load_jobs(json_file_name)
    main_interface(json_file_name)
def main_interface(json_file_name: str):
    with open(f'{json_file_name}.json') as file:
        data = json.load(file)
    jobs_area = input("Enter locations for job in format (WA,CA,Seattle): ").lower().split(',')
    jobs_excel = input("Enter excel or enter: ").lower()
    jobs_found = find_jobs_in_area(jobs_area, data)
    if jobs_excel == 'excel':
        jobs_excel_name = input("Enter excel name: ")
        jobs_excel = input("Enter all or enter: ").lower()
        if jobs_excel == 'all':
            SWESpreadsheet.swespreadsheet.load_excel(json_file_name, jobs_excel_name, data)
        else:
            SWESpreadsheet.swespreadsheet.load_excel(json_file_name, jobs_excel_name, jobs_found)
        print(f"Created the file {jobs_excel_name}.xlsx!")

    else:
        for index, job in enumerate(jobs_found):
            print(f"{index+1}.({''.join(job['company']).title()}) - {''.join(job['role']).title()}")
        try:
            while(True):
                job_lookup_input = input("Enter a job number ( exit ): ")
                show_all_job_links(jobs_found, int(job_lookup_input))
        except Exception as e:
            print("Thank you for using the program.")
def show_all_job_links(jobs, job_index: int):
    try:
        for index,url in enumerate(jobs[job_index-1]['url']):
            print(f"{index+1} - {url}")
        user_in = int(input("Enter a number: "))
        webbrowser.open(jobs[job_index - 1]['url'][user_in - 1])
    except Exception as e:
        print("Thank you for using the program.")
def find_jobs_in_area(areas: [str], datas):
    jobs_found = []
    for data in datas:
        area_found = False
        if not area_found:
            for area in areas:
                if area in ''.join(data['location']):
                    jobs_found.append(data)
                    area_found = True
        area_found = False
    return jobs_found

if __name__ == '__main__':
    main()