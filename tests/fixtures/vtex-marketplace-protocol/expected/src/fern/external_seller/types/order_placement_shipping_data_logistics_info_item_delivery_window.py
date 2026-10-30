

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class OrderPlacementShippingDataLogisticsInfoItemDeliveryWindow(UniversalBaseModel):
    """
    Scheduled delivery window information, in case it applies to the item.
    """

    end_date_utc: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="endDateUtc"),
        pydantic.Field(alias="endDateUtc", description="Scheduled delivery window end date in UTC."),
    ] = None
    """
    Scheduled delivery window end date in UTC.
    """

    list_price: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="listPrice"),
        pydantic.Field(alias="listPrice", description="Scheduled delivery window list price."),
    ] = None
    """
    Scheduled delivery window list price.
    """

    start_date_utc: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="startDateUtc"),
        pydantic.Field(alias="startDateUtc", description="Scheduled delivery window start date in UTC."),
    ] = None
    """
    Scheduled delivery window start date in UTC.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
