

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .files_sharing_sharee import FilesSharingSharee
from .files_sharing_sharee_circle import FilesSharingShareeCircle
from .files_sharing_sharee_email import FilesSharingShareeEmail
from .files_sharing_sharee_lookup import FilesSharingShareeLookup
from .files_sharing_sharee_remote import FilesSharingShareeRemote
from .files_sharing_sharee_remote_group import FilesSharingShareeRemoteGroup
from .files_sharing_sharee_user import FilesSharingShareeUser
from .files_sharing_sharees_search_result_exact import FilesSharingShareesSearchResultExact


class FilesSharingShareesSearchResult(UniversalBaseModel):
    exact: FilesSharingShareesSearchResultExact
    circles: typing.List[FilesSharingShareeCircle]
    emails: typing.List[FilesSharingShareeEmail]
    groups: typing.List[FilesSharingSharee]
    lookup: typing.List[FilesSharingShareeLookup]
    remote_groups: typing.List[FilesSharingShareeRemoteGroup]
    remotes: typing.List[FilesSharingShareeRemote]
    rooms: typing.List[FilesSharingSharee]
    users: typing.List[FilesSharingShareeUser]
    lookup_enabled: typing_extensions.Annotated[
        bool, FieldMetadata(alias="lookupEnabled"), pydantic.Field(alias="lookupEnabled")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
