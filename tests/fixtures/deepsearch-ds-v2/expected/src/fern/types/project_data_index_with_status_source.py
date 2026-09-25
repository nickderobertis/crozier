

import typing

from .elastic_index_source import ElasticIndexSource
from .project_data_index_source import ProjectDataIndexSource

ProjectDataIndexWithStatusSource = typing.Union[ElasticIndexSource, ProjectDataIndexSource]
