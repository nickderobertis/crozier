

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DealerInformation(UniversalBaseModel):
    """
    Public dealership profile. v1.0 reduces this to the minimum: a dealer group `name`, an optional `welcome_message`, and one or more `rooftops` (physical locations). Per-location identity, address, geo, contacts, hours, and service capabilities live on each rooftop. Vehicles reference the rooftop that holds them via `Vehicle.rooftop` = the rooftop's `name`. Returned by the `dealer.information` AAP skill, wrapped in `dealer.information.response` and carried inside an A2A `Message.parts[].data` DataPart via the A2A `SendMessage` operation.
    """

    name: str = pydantic.Field()
    """
    Dealer group / business name shown to buyers (e.g. 'Demo Auto Group').
    """

    welcome_message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional greeting a buyer agent MAY surface to the user (e.g. 'Welcome to Demo Auto Group — happy to help by phone, video, or in person.').
    """

    rooftops: typing.List[typing.Any] = pydantic.Field()
    """
    One or more dealership locations (rooftops). A single-location dealer has one entry; a multi-rooftop group lists each store.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
