

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PlaceFulfillmentOrderRequestItemsItemPriceTagsItem(UniversalBaseModel):
    identifier: typing.Optional[str] = pydantic.Field(default=None)
    """
    Price tag identifier.
    """

    is_percentual: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isPercentual"),
        pydantic.Field(alias="isPercentual", description="`true` if price tag value is applied through a percentage."),
    ] = None
    """
    `true` if price tag value is applied through a percentage.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Price tag name.
    """

    raw_value: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="rawValue"),
        pydantic.Field(alias="rawValue", description="Price tag value."),
    ] = None
    """
    Price tag value.
    """

    value: typing.Optional[int] = pydantic.Field(default=None)
    """
    Price tag raw value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
