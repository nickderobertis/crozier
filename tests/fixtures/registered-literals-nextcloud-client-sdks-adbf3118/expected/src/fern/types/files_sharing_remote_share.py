

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FilesSharingRemoteShare(UniversalBaseModel):
    accepted: bool
    file_id: typing.Optional[int] = None
    id: int
    mimetype: typing.Optional[str] = None
    mountpoint: str
    mtime: typing.Optional[int] = None
    name: str
    owner: str
    parent: typing.Optional[int] = None
    permissions: typing.Optional[int] = None
    remote: str
    remote_id: str
    share_token: str
    share_type: int
    type: typing.Optional[str] = None
    user: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
