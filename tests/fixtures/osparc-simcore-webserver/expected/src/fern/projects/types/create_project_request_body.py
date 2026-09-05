

import typing

from ...types.project_copy_override import ProjectCopyOverride
from ...types.project_create_new import ProjectCreateNew

CreateProjectRequestBody = typing.Union[ProjectCreateNew, ProjectCopyOverride]
