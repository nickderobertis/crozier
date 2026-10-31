

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Fields(UniversalBaseModel):
    """
    String dictionary with the names of the fields and their respective values that must be inserted into the order.
    """

    marketplace_payment_method: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="marketplacePaymentMethod"),
        pydantic.Field(alias="marketplacePaymentMethod", description="String with field's key and value."),
    ]
    """
    String with field's key and value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
