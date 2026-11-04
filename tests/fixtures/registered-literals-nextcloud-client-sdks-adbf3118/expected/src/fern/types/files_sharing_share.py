

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .files_sharing_share_status import FilesSharingShareStatus


class FilesSharingShare(UniversalBaseModel):
    attributes: typing.Optional[str] = None
    can_delete: bool
    can_edit: bool
    displayname_file_owner: str
    displayname_owner: str
    expiration: typing.Optional[str] = None
    file_parent: int
    file_source: int
    file_target: str
    has_preview: bool
    id: str
    item_source: int
    item_type: str
    label: str
    mail_send: int
    mimetype: str
    note: str
    password: typing.Optional[str] = None
    password_expiration_time: typing.Optional[str] = None
    path: str
    permissions: int
    send_password_by_talk: typing.Optional[bool] = None
    share_type: int
    share_with: typing.Optional[str] = None
    share_with_avatar: typing.Optional[str] = None
    share_with_displayname: typing.Optional[str] = None
    share_with_link: typing.Optional[str] = None
    status: typing.Optional[FilesSharingShareStatus] = None
    stime: int
    storage: int
    storage_id: str
    token: typing.Optional[str] = None
    uid_file_owner: str
    uid_owner: str
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
