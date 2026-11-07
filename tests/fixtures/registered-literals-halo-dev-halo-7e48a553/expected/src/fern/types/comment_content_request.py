

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CommentContentRequest(UniversalBaseModel):
    """
    Body-only update for an existing comment or reply.
    """

    content: str
    raw: str
    version: int = pydantic.Field()
    """
    Resource version when the editor was opened.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
