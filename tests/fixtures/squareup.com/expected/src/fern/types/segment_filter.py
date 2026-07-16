

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .filter_value import FilterValue


class SegmentFilter(UniversalBaseModel):
    """
    A query filter to search for appointment segments by.
    """

    service_variation_id: str = pydantic.Field()
    """
    The ID of the [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation) representing the service booked in this segment.
    """

    team_member_id_filter: typing.Optional[FilterValue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
