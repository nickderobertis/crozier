

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PaymentInteractionPaymentItemsItem(UniversalBaseModel):
    id: str
    label: str
    quantity: int
    amount_minor: typing_extensions.Annotated[
        int, FieldMetadata(alias="amountMinor"), pydantic.Field(alias="amountMinor")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
