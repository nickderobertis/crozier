

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateChannelFolderResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    channel_folder_id: int = pydantic.Field()
    """
    The unique ID of the created channel folder.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
