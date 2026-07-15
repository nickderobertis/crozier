

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TaskOutletDatasetReference(UniversalBaseModel):
    """
    A datasets reference to an upstream task.

    *New in version 2.4.0*
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The dataset creation time
    """

    dag_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The DAG ID that updates the dataset.
    """

    task_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The task ID that updates the dataset.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The dataset update time
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
