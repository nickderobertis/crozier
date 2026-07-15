

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TaskInstanceReference(UniversalBaseModel):
    dag_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The DAG ID.
    """

    dag_run_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The DAG run ID.
    """

    execution_date: typing.Optional[str] = None
    task_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The task ID.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
