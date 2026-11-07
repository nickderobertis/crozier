

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Contract(UniversalBaseModel):
    """
    smart contract state and interaction data including read function results, write function forms, and event history
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    the address of this smart contract
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    the name of this contract (if available)
    """

    abi: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    the ABI for this contract
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="lastUpdated"),
        pydantic.Field(alias="lastUpdated", description="timestamp when this contract state was last updated"),
    ] = None
    """
    timestamp when this contract state was last updated
    """

    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    date when this contract state was last updated (calculated)
    """

    error_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="errorCount"),
        pydantic.Field(alias="errorCount", description="number of errors encountered when calling read functions"),
    ] = None
    """
    number of errors encountered when calling read functions
    """

    last_error: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastError"),
        pydantic.Field(alias="lastError", description="the most recent error message when calling functions"),
    ] = None
    """
    the most recent error message when calling functions
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
