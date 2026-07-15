

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .basic_dag_run import BasicDagRun


class DatasetEvent(UniversalBaseModel):
    """
    A dataset event.

    *New in version 2.4.0*
    """

    created_dagruns: typing.Optional[typing.List[BasicDagRun]] = None
    dataset_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The dataset id
    """

    dataset_uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URI of the dataset
    """

    extra: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    The dataset event extra
    """

    source_dag_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The DAG ID that updated the dataset.
    """

    source_map_index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The task map index that updated the dataset.
    """

    source_run_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The DAG run ID that updated the dataset.
    """

    source_task_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The task ID that updated the dataset.
    """

    timestamp: typing.Optional[str] = pydantic.Field(default=None)
    """
    The dataset event creation time
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
