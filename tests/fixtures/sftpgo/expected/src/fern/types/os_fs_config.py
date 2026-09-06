

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OsFsConfig(UniversalBaseModel):
    read_buffer_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    The read buffer size, as MB, to use for downloads. 0 means no buffering, that's fine in most use cases.
    """

    write_buffer_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    The write buffer size, as MB, to use for uploads. 0 means no buffering, that's fine in most use cases.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
