

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NodesCommentCreateRequestAttributes(UniversalBaseModel):
    """
    The properties of the comment entity.
    """

    can_edit: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the current user has permission to edit this comment
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    The content of the comment.
    """

    date_created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the comment was created, as an iso8601 formatted timestamp.
    """

    date_modified: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the comment was last modified, as an iso8601 formatted timestamp.
    """

    deleted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the comment is deleted.
    """

    has_children: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the comment has replies.
    """

    has_report: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the comment the current user reported this as spam.
    """

    is_abuse: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the comment is flagged or confirmed spam.
    """

    is_ham: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not an admin checked the legitimacy of this comment.
    """

    modified: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the comment has been edited.
    """

    page: typing.Optional[str] = pydantic.Field(default=None)
    """
    The page type the comment is on, e.g. `node`, `registration`, `wiki`, `files`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
