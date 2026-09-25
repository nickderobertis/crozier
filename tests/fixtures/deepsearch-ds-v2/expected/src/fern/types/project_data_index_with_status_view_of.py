

import typing

from .elastic_instance_data_index import ElasticInstanceDataIndex
from .project_source_data_index import ProjectSourceDataIndex

ProjectDataIndexWithStatusViewOf = typing.Union[ProjectSourceDataIndex, ElasticInstanceDataIndex]
