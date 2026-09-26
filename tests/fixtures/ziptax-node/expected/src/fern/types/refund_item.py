

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RefundItem(UniversalBaseModel):
    item_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="itemId"),
        pydantic.Field(
            alias="itemId",
            description="The itemId of the line item to refund. Must match an itemId from the original order.",
        ),
    ]
    """
    The itemId of the line item to refund. Must match an itemId from the original order.
    """

    quantity: float = pydantic.Field()
    """
    The quantity of the item to refund. May be fractional and must not exceed the quantity on the original order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
