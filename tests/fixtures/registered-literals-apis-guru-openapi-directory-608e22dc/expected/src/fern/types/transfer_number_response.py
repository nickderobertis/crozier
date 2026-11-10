

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TransferNumberResponse(UniversalBaseModel):
    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The two character country code in ISO 3166-1 alpha-2 format
    """

    from_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="from"),
        pydantic.Field(alias="from", description="Account the number is transferred from"),
    ] = None
    """
    Account the number is transferred from
    """

    number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Number transfered
    """

    to: typing.Optional[str] = pydantic.Field(default=None)
    """
    Account the number is transferred to
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
