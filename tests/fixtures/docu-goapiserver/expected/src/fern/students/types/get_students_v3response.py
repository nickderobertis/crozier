

import typing

from ...types.student import Student
from ...types.student_projection import StudentProjection

GetStudentsV3Response = typing.Union[typing.List[Student], typing.List[StudentProjection]]
