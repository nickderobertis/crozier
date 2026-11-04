

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Result(UniversalBaseModel):
    """
    the result (articulated if possible, as bytes otherwise) of a call to a smart contract
    """

    block_number: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="blockNumber"),
        pydantic.Field(alias="blockNumber", description="the block number at which this call was made"),
    ] = None
    """
    the block number at which this call was made
    """

    timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    the timestamp of the block for this call
    """

    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    the timestamp as a date (calculated)
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    the address of contract being called
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    the name of the function call
    """

    encoding: typing.Optional[str] = pydantic.Field(default=None)
    """
    the encoding for the function call
    """

    signature: typing.Optional[str] = pydantic.Field(default=None)
    """
    the canonical signature of the interface
    """

    encoded_arguments: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="encodedArguments"),
        pydantic.Field(alias="encodedArguments", description="the bytes data following the encoding of the call"),
    ] = None
    """
    the bytes data following the encoding of the call
    """

    articulated_out: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="articulatedOut"),
        pydantic.Field(alias="articulatedOut", description="the result of the call articulated as other models"),
    ] = None
    """
    the result of the call articulated as other models
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
