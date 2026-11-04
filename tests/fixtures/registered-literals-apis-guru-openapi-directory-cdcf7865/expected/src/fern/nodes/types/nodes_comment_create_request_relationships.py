

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NodesCommentCreateRequestRelationships(UniversalBaseModel):
    """
    URLs to other entities or entity collections that have a relationship to the comment entity.
    """

    node: typing.Optional[str] = pydantic.Field(default=None)
    """
    A relationship to the node the comment is on.
    """

    replies: typing.Optional[str] = pydantic.Field(default=None)
    """
    A relationship to the replies to the comment.
    """

    reports: typing.Optional[str] = pydantic.Field(default=None)
    """
    A relationship to the reports connected to the comment.
    """

    target: typing.Optional[str] = pydantic.Field(default=None)
    """
    A relationship to the target of the comment.
    """

    user: typing.Optional[str] = pydantic.Field(default=None)
    """
    A relationship to the user who created the comment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
