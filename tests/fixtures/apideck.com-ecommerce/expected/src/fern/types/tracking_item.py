

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .updated_at import UpdatedAt


class TrackingItem(UniversalBaseModel):
    """
    Represents the tracking information associated with an ecommerce order.
    """

    number: typing.Optional[str] = pydantic.Field(default=None)
    """
     The tracking number associated with the shipment, which can be used to track the progress of the delivery.
    """

    provider: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name or code of the carrier or shipping company that is handling the shipment.
    """

    updated_at: typing.Optional[UpdatedAt] = None
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the carrier's tracking page, which can be used to view detailed information about the shipment's progress.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
