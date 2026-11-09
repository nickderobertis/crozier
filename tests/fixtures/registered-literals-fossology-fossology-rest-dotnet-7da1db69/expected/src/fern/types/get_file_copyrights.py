

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetFileCopyrights(UniversalBaseModel):
    """
    CX details of a file
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    CX content
    """

    hash: typing.Optional[str] = pydantic.Field(default=None)
    """
    CX hash
    """

    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Count of the CXs
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
