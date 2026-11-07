

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .files_sharing_lookup import FilesSharingLookup


class FilesSharingShareeLookupAllOfExtra(UniversalBaseModel):
    federation_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="federationId"), pydantic.Field(alias="federationId")
    ]
    name: FilesSharingLookup
    email: FilesSharingLookup
    address: FilesSharingLookup
    website: FilesSharingLookup
    twitter: FilesSharingLookup
    phone: FilesSharingLookup
    twitter_signature: FilesSharingLookup
    website_signature: FilesSharingLookup
    userid: FilesSharingLookup

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
