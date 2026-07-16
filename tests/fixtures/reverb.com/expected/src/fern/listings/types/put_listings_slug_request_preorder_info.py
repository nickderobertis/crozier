

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .put_listings_slug_request_preorder_info_lead_time_unit import PutListingsSlugRequestPreorderInfoLeadTimeUnit


class PutListingsSlugRequestPreorderInfo(UniversalBaseModel):
    """
    Create or update a preorder listing. Requires opt-in. Please contact sales@reverb.com if you would like to activate this feature.
    """

    lead_time: typing.Optional[int] = pydantic.Field(default=None)
    """
    The amount of time before the item will be ready to ship. When lead_time is submitted it is converted into days and added to the current date to produce `estimated_ship_date` in the response body of the request.
    """

    lead_time_unit: PutListingsSlugRequestPreorderInfoLeadTimeUnit = pydantic.Field()
    """
    The unit of time which lead_time is measured in
    """

    ship_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date the item will be available to ship. In the response body of the request, `estimated_ship_date`, will be the same as ship_date. Date must be ISO8601 format - e.g: 2015-04-09T10:52:23-00:00.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
