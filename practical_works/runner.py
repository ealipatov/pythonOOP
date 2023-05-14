from utils import Utils
from test_service import TestService
from repository import StudentRepoXlsx


class TestProgramRunner:
    repository = StudentRepoXlsx()
    test_service = TestService(repository)

    def run(self):
        students = self.repository.load_all_students()

        menu = self.repository.load_menu()

        user = Utils.user_authentication(students)

        self.test_service.show_menu(students, menu, user)


runner = TestProgramRunner()
runner.run()
