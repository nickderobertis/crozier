

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resources_get_response_data_resources_item import ResourcesGetResponseDataResourcesItem


class ResourcesGetResponseData(UniversalBaseModel):
    resources: typing.List[ResourcesGetResponseDataResourcesItem] = pydantic.Field()
    """
    List of resources
    """

    total: float = pydantic.Field()
    """
    Total number of resources
    """

    limit: typing.Optional[float] = pydantic.Field(default=None)
    """
    Applied limit
    """

    offset: typing.Optional[float] = pydantic.Field(default=None)
    """
    Applied offset
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
