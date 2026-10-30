

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdateTrackingStatusRequestEventsItem(UniversalBaseModel):
    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    City where the event ocurred.
    """

    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date when event ocurred.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the event.
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    State where the event ocurred.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
