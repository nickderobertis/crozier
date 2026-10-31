

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ObjectTransferAccess_PresignedUrl(UniversalBaseModel):
    """
    A capability that lets a client transfer bytes directly to or from object storage.
    """

    kind: typing.Literal["presigned_url"] = "presigned_url"
    expires_at_ms: int
    headers: typing.Dict[str, str]
    method: str
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ObjectTransferAccess = ObjectTransferAccess_PresignedUrl
