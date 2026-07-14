

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CompleteExternalUploadResponse(UniversalBaseModel):
    dominant_color: typing.Optional[str] = None
    extension: str
    filesize: int
    height: int
    human_filesize: str
    id: int
    original_filename: str
    retain_hours: typing.Optional[str] = None
    short_path: str
    short_url: str
    thumbnail_height: int
    thumbnail_width: int
    url: str
    width: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
