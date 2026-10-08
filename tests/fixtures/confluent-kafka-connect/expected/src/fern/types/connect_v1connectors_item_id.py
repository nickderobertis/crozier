

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConnectV1ConnectorsItemId(UniversalBaseModel):
    """
    The ID of task.
    """

    connector: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the connector the task belongs to.
    """

    task: typing.Optional[int] = pydantic.Field(default=None)
    """
    Task ID within the connector.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
