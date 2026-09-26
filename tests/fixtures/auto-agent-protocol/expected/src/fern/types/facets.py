

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Facets(UniversalBaseModel):
    """
    Aggregated facet counts and ranges over a dealer's inventory. Returned by the `inventory.facets` AAP skill (wrapped in `inventory.facets.response`) and OPTIONALLY embedded in `inventory.search` responses. Both responses travel inside an A2A `Message.parts[].data` DataPart via the A2A `SendMessage` operation.
    """

    makes: typing.Optional[typing.Any] = None
    models: typing.Optional[typing.Any] = None
    trims: typing.Optional[typing.Any] = None
    years: typing.Optional[typing.Any] = None
    conditions: typing.Optional[typing.Any] = None
    transmissions: typing.Optional[typing.Any] = None
    fuels: typing.Optional[typing.Any] = None
    drivelines: typing.Optional[typing.Any] = None
    bodies: typing.Optional[typing.Any] = None
    exterior_colors: typing.Optional[typing.Any] = None
    interior_colors: typing.Optional[typing.Any] = None
    rooftops: typing.Optional[typing.Any] = None
    statuses: typing.Optional[typing.Any] = None
    price_range: typing.Optional[typing.Any] = None
    mileage_range: typing.Optional[typing.Any] = None
    year_range: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
