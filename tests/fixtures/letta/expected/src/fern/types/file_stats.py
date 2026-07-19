

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FileStats(UniversalBaseModel):
    """
    File statistics for metadata endpoint
    """

    file_id: str = pydantic.Field()
    """
    Unique identifier of the file
    """

    file_name: str = pydantic.Field()
    """
    Name of the file
    """

    file_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Size of the file in bytes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
