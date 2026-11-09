

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DescriptionRecord(UniversalBaseModel):
    """
    Metadata for a stored description record. The content itself is returned by GET on the record.
    """

    content_type: str = pydantic.Field()
    """
    The stored content type, either "application/json" or "text/plain; charset=utf-8".
    """

    created_at: int = pydantic.Field()
    """
    When the record was first created (Unix seconds).
    """

    created_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    The actor who created the record.
    """

    length: int = pydantic.Field()
    """
    The content length in bytes.
    """

    md5: str = pydantic.Field()
    """
    The hex-encoded MD5 of the content.
    """

    modified_at: int = pydantic.Field()
    """
    When the record was last updated (Unix seconds).
    """

    modified_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    The actor who last updated the record.
    """

    name: str = pydantic.Field()
    """
    The record name (letters, digits, '.', '_' or '-').
    """

    owner_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The owning project (app) UID for project-scoped records; empty for global.
    """

    scope: str = pydantic.Field()
    """
    The ownership scope of the record ("global" or "project").
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
