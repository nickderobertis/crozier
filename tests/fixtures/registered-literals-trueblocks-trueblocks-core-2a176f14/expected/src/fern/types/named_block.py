

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NamedBlock(UniversalBaseModel):
    """
    a block that has been given a particular name such as `first` or `latest`
    """

    block_number: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="blockNumber"),
        pydantic.Field(alias="blockNumber", description="the number of the block"),
    ] = None
    """
    the number of the block
    """

    timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    the Unix timestamp of the block
    """

    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    the timestamp as a date (calculated)
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    an optional name for the block
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    an optional description of the block
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
