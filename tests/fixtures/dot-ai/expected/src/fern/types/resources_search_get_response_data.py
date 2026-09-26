

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resources_search_get_response_data_resources_item import ResourcesSearchGetResponseDataResourcesItem


class ResourcesSearchGetResponseData(UniversalBaseModel):
    resources: typing.List[ResourcesSearchGetResponseDataResourcesItem] = pydantic.Field()
    """
    Matching resources
    """

    total: float = pydantic.Field()
    """
    Total number of matches
    """

    limit: float = pydantic.Field()
    """
    Requested limit
    """

    offset: float = pydantic.Field()
    """
    Requested offset
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
