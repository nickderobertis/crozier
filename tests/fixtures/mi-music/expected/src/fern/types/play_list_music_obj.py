

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PlayListMusicObj(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    歌单名称
    """

    music_list: typing.List[str] = pydantic.Field()
    """
    歌曲名称列表
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
