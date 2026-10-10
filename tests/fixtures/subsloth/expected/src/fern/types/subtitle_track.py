

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .language_code import LanguageCode
from .subtitle_track_format import SubtitleTrackFormat


class SubtitleTrack(UniversalBaseModel):
    """
    A single subtitle track with language, code, URL, and format.
    """

    lang: typing.Optional[LanguageCode] = None
    language: typing.Optional[LanguageCode] = None
    code: typing.Optional[LanguageCode] = None
    label: typing.Optional[str] = None
    url: typing.Optional[str] = None
    download_url: typing.Optional[str] = None
    format: typing.Optional[SubtitleTrackFormat] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
