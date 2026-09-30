

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .endpoint_def_query_reference import EndpointDefQueryReference
from .endpoint_metadata_query_reference_methods_item import EndpointMetadataQueryReferenceMethodsItem


class EndpointMetadataQueryReference(UniversalBaseModel):
    comment: typing.Optional[str] = None
    definition: EndpointDefQueryReference
    methods: typing.List[EndpointMetadataQueryReferenceMethodsItem]
    name: str
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
