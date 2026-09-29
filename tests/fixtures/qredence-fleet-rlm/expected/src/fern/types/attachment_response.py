

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AttachmentResponse(UniversalBaseModel):
    """
    Public attachment metadata — no host or Volume paths.
    """

    id: str
    filename: str
    content_type: typing.Optional[str] = None
    byte_size: int
    checksum_sha256: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
