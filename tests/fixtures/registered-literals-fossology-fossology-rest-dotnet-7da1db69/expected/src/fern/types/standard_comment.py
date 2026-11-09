

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StandardComment(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The primary key of the comment.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the comment.
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text content of the comment.
    """

    is_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the comment is enabled or not.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
