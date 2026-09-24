

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .command_response import CommandResponse


class CommandsListResponse(UniversalBaseModel):
    total_items: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalItems"),
        pydantic.Field(alias="totalItems", description="The total number of commands"),
    ]
    """
    The total number of commands
    """

    items: typing.List[CommandResponse] = pydantic.Field()
    """
    The list of commands
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
