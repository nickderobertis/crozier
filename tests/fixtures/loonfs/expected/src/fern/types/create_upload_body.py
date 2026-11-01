

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateUploadBody_DirectMultipart(UniversalBaseModel):
    """
    The transport for a new upload session.
    """

    mode: typing.Literal["direct_multipart"] = "direct_multipart"
    part_size_bytes: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateUploadBody_DirectPut(UniversalBaseModel):
    """
    The transport for a new upload session.
    """

    mode: typing.Literal["direct_put"] = "direct_put"
    size_bytes: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateUploadBody_ServiceProxied(UniversalBaseModel):
    """
    The transport for a new upload session.
    """

    mode: typing.Literal["service_proxied"] = "service_proxied"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


CreateUploadBody = typing_extensions.Annotated[
    typing.Union[CreateUploadBody_DirectMultipart, CreateUploadBody_DirectPut, CreateUploadBody_ServiceProxied],
    pydantic.Field(discriminator="mode"),
]
