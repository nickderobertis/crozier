

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .files_sharing_sharee import FilesSharingSharee
from .files_sharing_sharee_email import FilesSharingShareeEmail
from .files_sharing_sharee_remote import FilesSharingShareeRemote
from .files_sharing_sharee_remote_group import FilesSharingShareeRemoteGroup
from .files_sharing_sharee_user import FilesSharingShareeUser
from .files_sharing_sharees_recommended_result_exact import FilesSharingShareesRecommendedResultExact


class FilesSharingShareesRecommendedResult(UniversalBaseModel):
    exact: FilesSharingShareesRecommendedResultExact
    emails: typing.List[FilesSharingShareeEmail]
    groups: typing.List[FilesSharingSharee]
    remote_groups: typing.List[FilesSharingShareeRemoteGroup]
    remotes: typing.List[FilesSharingShareeRemote]
    users: typing.List[FilesSharingShareeUser]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
