

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_data_source_connection_command_type import ListDataSourceConnectionCommandType


class ListDataSourceConnectionCommand(UniversalBaseModel):
    """
    List data source schemas.

        Retrieves available schemas for a data source engine.

        Attributes:
            engine: Data source engine identifier.
    """

    engine: str
    type: ListDataSourceConnectionCommandType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
