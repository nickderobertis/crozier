

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .upload_meta_form_content_type import UploadMetaFormContentType


class UploadMetaForm(UniversalBaseModel):
    bucket: str
    object_key: str
    checksum: typing.Optional[str] = None
    content_type: UploadMetaFormContentType
    size_bytes: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
