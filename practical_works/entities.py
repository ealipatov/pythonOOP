from dataclasses import dataclass, field

ADMIN_ACCESS = "ADMIN_ACCESS"
STUDENT_ACCESS = "STUDENT_ACCESS"


@dataclass(frozen=True)
class Student:
    name: str
    password: str
    access_level: str = STUDENT_ACCESS
    marks: list = field(default_factory=list)
