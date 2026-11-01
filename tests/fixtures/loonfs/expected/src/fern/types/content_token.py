

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .content_ref import ContentRef


class ContentToken(UniversalBaseModel):
    """
    A signed token that shows a `content_ref` was verified in a completed upload, so a later
    commit can use that reference.
    """

    content_ref: ContentRef = pydantic.Field()
    """
    The content that this token authorizes.
    """

    token: str = pydantic.Field()
    """
    The opaque token that the server signed. Clients must not parse it.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
