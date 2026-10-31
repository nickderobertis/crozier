

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class FulfillmentSimulationResponseLogisticsInfoItemSlasItemAvailableDeliveryWindowsItem(UniversalBaseModel):
    """
    Object with delivery windows information.
    """

    end_date_utc: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="endDateUtc"),
        pydantic.Field(alias="endDateUtc", description="End date of the delivery window."),
    ]
    """
    End date of the delivery window.
    """

    price: int = pydantic.Field()
    """
    Extra price for scheduled delivery. The last two digits are the cents.
    """

    start_date_utc: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="startDateUtc"),
        pydantic.Field(alias="startDateUtc", description="Start date of the delivery window."),
    ]
    """
    Start date of the delivery window.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
