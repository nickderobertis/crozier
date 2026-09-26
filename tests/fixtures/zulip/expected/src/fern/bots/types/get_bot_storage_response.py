

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetBotStorageResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    storage: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    A dictionary with string key-value pairs of
    data stored for the bot user.
    
    If the `keys` parameter was passed, then only
    the key-value pairs matching the list of keys
    will be returned.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
