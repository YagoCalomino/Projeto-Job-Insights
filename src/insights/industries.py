from src.insights.jobs import ProcessJobs
from typing import List

class ProcessIndustries(ProcessJobs):
    def __init__(self):  # Inicialização da classe
        super().__init__()

    # Método para obter indústrias únicas
    def get_unique_industries(self) -> List[str]:
        industries = set()
        for job in self.jobs_list:  # Para cada trabalho na lista de trabalhos
            if job["industry"] != "":
                industries.add(job["industry"])  # Adicionar a indústria à lista de indústrias
        return list(industries)
