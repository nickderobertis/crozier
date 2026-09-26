

import typing

from ...types.project_data_index_non_view import ProjectDataIndexNonView
from ...types.project_data_index_view import ProjectDataIndexView

UpdateProjectDataIndexRequestBody = typing.Union[ProjectDataIndexView, ProjectDataIndexNonView]
