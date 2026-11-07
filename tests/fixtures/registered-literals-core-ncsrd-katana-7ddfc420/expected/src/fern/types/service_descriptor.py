

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .service_descriptor_ns_list_item import ServiceDescriptorNsListItem


class ServiceDescriptor(UniversalBaseModel):
    """
    This is the schema for the Service Descriptor part of slice IM
    """

    ns_list: typing.Optional[typing.List[ServiceDescriptorNsListItem]] = pydantic.Field(default=None)
    """
    List of the NSD to be instantiated alongside the slice
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
