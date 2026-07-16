

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .collection_info import CollectionInfo
from .task_instance import TaskInstance


class TaskInstanceCollection(CollectionInfo):
    """
    Collection of task instances.

    *Changed in version 2.1.0*&#58; 'total_entries' field is added.
    """

    task_instances: typing.Optional[typing.List[TaskInstance]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
