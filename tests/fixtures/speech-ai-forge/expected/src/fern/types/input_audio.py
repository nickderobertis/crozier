

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .from_url import FromUrl


class InputAudio(UniversalBaseModel):
    from_url: typing.Optional[FromUrl] = pydantic.Field(default=None)
    """
    从 URL 加载音频
    """

    from_base64: typing.Optional[str] = pydantic.Field(default=None)
    """
    base64 编码的音频数据
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
