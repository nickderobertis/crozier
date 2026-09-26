

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .get_quote_by_id_quote_response_data_deposit_option_type import GetQuoteByIdQuoteResponseDataDepositOptionType


class GetQuoteByIdQuoteResponseDataDeposit(UniversalBaseModel):
    option_type: typing_extensions.Annotated[
        typing.Optional[GetQuoteByIdQuoteResponseDataDepositOptionType],
        FieldMetadata(alias="optionType"),
        pydantic.Field(alias="optionType"),
    ] = None
    option_value: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="optionValue"), pydantic.Field(alias="optionValue")
    ] = None
    is_paid: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isPaid"), pydantic.Field(alias="isPaid")
    ] = None
    invoice_guid: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="invoiceGuid"), pydantic.Field(alias="invoiceGuid")
    ] = None
    invoice_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="invoiceUrl"), pydantic.Field(alias="invoiceUrl")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
