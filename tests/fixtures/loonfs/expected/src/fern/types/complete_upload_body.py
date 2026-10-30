

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .completed_upload_part import CompletedUploadPart
from .upload_content_claim import UploadContentClaim


class CompleteUploadBody_DirectMultipart(UniversalBaseModel):
    """
    A request to complete an upload, in the mode that started it.
    """

    mode: typing.Literal["direct_multipart"] = "direct_multipart"
    content: UploadContentClaim
    parts: typing.List[CompletedUploadPart]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CompleteUploadBody_DirectPut(UniversalBaseModel):
    """
    A request to complete an upload, in the mode that started it.
    """

    mode: typing.Literal["direct_put"] = "direct_put"
    content: UploadContentClaim

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CompleteUploadBody_ServiceProxied(UniversalBaseModel):
    """
    A request to complete an upload, in the mode that started it.
    """

    mode: typing.Literal["service_proxied"] = "service_proxied"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


CompleteUploadBody = typing_extensions.Annotated[
    typing.Union[CompleteUploadBody_DirectMultipart, CompleteUploadBody_DirectPut, CompleteUploadBody_ServiceProxied],
    pydantic.Field(discriminator="mode"),
]
