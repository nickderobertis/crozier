

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sku import Sku


class Resource(UniversalBaseModel):
    """
    Model of the Resource.
    """

    tags: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups).
    """

    location: str = pydantic.Field()
    """
    The location of the resource. This will be one of the supported and registered Azure Regions (e.g. West US, East US, Southeast Asia, etc.). The region of a resource cannot be changed once it is created, but if an identical region is specified on update the request will succeed.
    """

    sku: Sku = pydantic.Field()
    """
    The sku type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
