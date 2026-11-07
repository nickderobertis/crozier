

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FilesSharingDeletedShare(UniversalBaseModel):
    id: str
    share_type: int
    uid_owner: str
    displayname_owner: str
    permissions: int
    stime: int
    uid_file_owner: str
    displayname_file_owner: str
    path: str
    item_type: str
    mimetype: str
    storage: int
    item_source: int
    file_source: int
    file_parent: int
    file_target: int
    expiration: typing.Optional[str] = None
    share_with: typing.Optional[str] = None
    share_with_displayname: typing.Optional[str] = None
    share_with_link: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
