

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dag_schedule_dataset_reference import DagScheduleDatasetReference
from .task_outlet_dataset_reference import TaskOutletDatasetReference


class Dataset(UniversalBaseModel):
    """
    A dataset item.

    *New in version 2.4.0*
    """

    consuming_dags: typing.Optional[typing.List[DagScheduleDatasetReference]] = None
    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The dataset creation time
    """

    extra: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The dataset extra
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The dataset id
    """

    producing_tasks: typing.Optional[typing.List[TaskOutletDatasetReference]] = None
    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The dataset update time
    """

    uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    The dataset uri
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
