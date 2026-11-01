

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ShipmentPickUpResponse(UniversalBaseModel):
    """
    Shipment pick up response.
    """

    confirmation_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="confirmationNumber"),
        pydantic.Field(alias="confirmationNumber", description="Confirmation number for the pick up request."),
    ] = None
    """
    Confirmation number for the pick up request.
    """

    ready_by_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="readyByTime"),
        pydantic.Field(
            alias="readyByTime",
            description="Time by which shipment should be ready for pick up, this is in local time of pick up area.",
        ),
    ] = None
    """
    Time by which shipment should be ready for pick up, this is in local time of pick up area.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
