

import typing

from .project_author_type_one import ProjectAuthorTypeOne
from .project_author_type_zero import ProjectAuthorTypeZero

ProjectAuthorType = typing.Union[ProjectAuthorTypeZero, ProjectAuthorTypeOne]
