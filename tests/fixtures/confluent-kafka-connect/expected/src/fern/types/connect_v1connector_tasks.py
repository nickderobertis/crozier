

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConnectV1ConnectorTasks(UniversalBaseModel):
    connector: str = pydantic.Field()
    """
    The name of the connector the task belongs to
    """

    task: int = pydantic.Field()
    """
    Task ID within the connector
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
