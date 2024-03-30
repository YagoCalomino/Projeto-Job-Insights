from typing import Dict, List, Union

from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):  # Inicialização da classe
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:  # Obter o maior salário
        biggest_salary = 0

        for job in self.jobs_list:
            try:
                int(job["max_salary"])
            except ValueError:
                continue

            if int(job["max_salary"]) > biggest_salary:
                biggest_salary = int(job["max_salary"])

        return biggest_salary

    def get_min_salary(self) -> int:  # Obter o menor salário
        smallest_salary = self.get_max_salary()

        for job in self.jobs_list:
            try:
                int(job["min_salary"])
            except ValueError:
                continue

            if int(job["min_salary"]) < smallest_salary:
                smallest_salary = int(job["min_salary"])

        return smallest_salary

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        try:
            min_salary = int(job["min_salary"])
            max_salary = int(job["max_salary"])
            salary = int(salary)

            if min_salary > max_salary:
                raise ValueError

            if min_salary > salary or max_salary < salary:
                return False
            else:
                return True

        except Exception:
            raise ValueError

    def filter_by_salary_range(  # Filtrar trabalhos por intervalo de salário
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
