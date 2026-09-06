

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PublishedFileDetailsPreview(UniversalBaseModel):
    external_reference: typing.Optional[str] = None
    filename: typing.Optional[str] = None
    preview_type: typing.Optional[int] = None
    previewid: typing.Optional[int] = None
    size: typing.Optional[int] = None
    sortorder: typing.Optional[int] = None
    url: typing.Optional[str] = None
    youtubevideoid: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
