

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .collection_links import CollectionLinks
from .collection_metadata import CollectionMetadata
from .service_credential_type import ServiceCredentialType


class ServiceCredentialTypesCollection(UniversalBaseModel):
    data: typing.Optional[typing.List[ServiceCredentialType]] = None
    links: typing.Optional[CollectionLinks] = None
    meta: typing.Optional[CollectionMetadata] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
