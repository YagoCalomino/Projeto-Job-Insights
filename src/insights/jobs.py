import csv
from typing import Dict, List

class ProcessJobs:
    def __init__(self) -> None:  # Inicialização da classe
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]: # Ler arquivo CSV
        with open(path) as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                self.jobs_list.append(row)

        return self.jobs_list

    def get_unique_job_types(self) -> List[str]: # Obter tipos de trabalho únicos
        job_types = list()
        for job in self.jobs_list:
            job_types.append(job["job_type"])

        return list(set(job_types))

    def filter_by_multiple_criteria(
        self, jobs: List[Dict], filter_criteria: Dict
    ) -> List[dict]:
        filtered_jobs = list()

        for job in jobs:
            if (
                job["industry"] == filter_criteria["industry"]
                and job["job_type"] == filter_criteria["job_type"]
            ):
                filtered_jobs.append(job)

        return filtered_jobs
