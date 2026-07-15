

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_at import CreatedAt
from .expires_at import ExpiresAt
from .shared_link_scope import SharedLinkScope
from .shared_link_target import SharedLinkTarget
from .updated_at import UpdatedAt


class SharedLink(UniversalBaseModel):
    created_at: typing.Optional[CreatedAt] = None
    download_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL that can be used to download the file.
    """

    expires_at: typing.Optional[ExpiresAt] = None
    password: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional password for the shared link.
    """

    password_protected: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicated if the shared link is password protected.
    """

    scope: typing.Optional[SharedLinkScope] = pydantic.Field(default=None)
    """
    The scope of the shared link.
    """

    target: typing.Optional[SharedLinkTarget] = None
    target_id: str = pydantic.Field()
    """
    The ID of the file or folder to link.
    """

    updated_at: typing.Optional[UpdatedAt] = None
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL that can be used to view the file.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
