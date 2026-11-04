

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resources_vi_ms_item_available_resources import ResourcesViMsItemAvailableResources
from .resources_vi_ms_item_max_resources import ResourcesViMsItemMaxResources
from .resources_vi_ms_item_tenants import ResourcesViMsItemTenants


class ResourcesViMsItem(UniversalBaseModel):
    """
    A VIM
    """

    name: typing.Optional[str] = None
    id: typing.Optional[str] = None
    type: typing.Optional[str] = None
    location: typing.Optional[str] = None
    tenants: typing.Optional[ResourcesViMsItemTenants] = pydantic.Field(default=None)
    """
    Tenants created on the VIM
    """

    max_resources: typing.Optional[ResourcesViMsItemMaxResources] = None
    available_resources: typing.Optional[ResourcesViMsItemAvailableResources] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
