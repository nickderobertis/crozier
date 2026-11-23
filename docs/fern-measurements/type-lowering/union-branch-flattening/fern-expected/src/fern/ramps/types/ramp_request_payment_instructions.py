

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class RampRequestPaymentInstructions(UniversalBaseModel):
    iban: typing.Optional[str] = None
    bic: typing.Optional[str] = None
    holder: typing.Optional[int] = None
    account_number: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="accountNumber"), pydantic.Field(alias="accountNumber")
    ] = None
    routing_number: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="routingNumber"), pydantic.Field(alias="routingNumber")
    ] = None
    reference_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="referenceId"), pydantic.Field(alias="referenceId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
