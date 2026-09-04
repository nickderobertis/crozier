

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SettlementDelayConfiguration(UniversalBaseModel):
    payment_method: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="paymentMethod"),
        pydantic.Field(alias="paymentMethod", description="The payment method to which the settlement delay applies."),
    ]
    """
    The payment method to which the settlement delay applies.
    """

    settlement_delay: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="settlementDelay"),
        pydantic.Field(
            alias="settlementDelay",
            description="The updated settlement delay applied to your user's transactions. It indicates the number of days after which your user's funds become available in their balance account.",
        ),
    ]
    """
    The updated settlement delay applied to your user's transactions. It indicates the number of days after which your user's funds become available in their balance account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
