

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .key_value import KeyValue


class RenameConfig(KeyValue):
    update_modtime: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Update modification time. This setting is not recursive and only applies to storage providers that support changing modification times
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
