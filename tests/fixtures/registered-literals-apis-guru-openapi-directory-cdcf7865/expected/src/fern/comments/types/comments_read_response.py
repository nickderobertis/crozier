

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .comments_read_response_attributes import CommentsReadResponseAttributes
from .comments_read_response_links import CommentsReadResponseLinks
from .comments_read_response_relationships import CommentsReadResponseRelationships


class CommentsReadResponse(UniversalBaseModel):
    attributes: typing.Optional[CommentsReadResponseAttributes] = pydantic.Field(default=None)
    """
    The properties of the comment entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the comment entity.
    """

    links: typing.Optional[CommentsReadResponseLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the comment entity.
    """

    relationships: typing.Optional[CommentsReadResponseRelationships] = pydantic.Field(default=None)
    """
    URLs to other entities or entity collections that have a relationship to the comment entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the comment entity (`comments`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
