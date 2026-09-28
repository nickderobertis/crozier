

import typing

from ...types.student import Student
from ...types.student_projection import StudentProjection

GetStudentsIdV3Response = typing.Union[Student, StudentProjection]
