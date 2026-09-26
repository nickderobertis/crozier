

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.channel_folder import ChannelFolder


class GetChannelFoldersResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    channel_folders: typing.Optional[typing.List[ChannelFolder]] = pydantic.Field(default=None)
    """
    A list of channel folder objects.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
