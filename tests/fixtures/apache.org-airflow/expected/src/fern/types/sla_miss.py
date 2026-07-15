

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SlaMiss(UniversalBaseModel):
    dag_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The DAG ID.
    """

    description: typing.Optional[str] = None
    email_sent: typing.Optional[bool] = None
    execution_date: typing.Optional[str] = None
    notification_sent: typing.Optional[bool] = None
    task_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The task ID.
    """

    timestamp: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
