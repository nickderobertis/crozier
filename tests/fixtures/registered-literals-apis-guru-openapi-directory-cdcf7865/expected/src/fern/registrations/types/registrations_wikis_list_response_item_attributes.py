

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegistrationsWikisListResponseItemAttributes(UniversalBaseModel):
    """
    The properties of the wiki.
    """

    content_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Content type of the wiki (`text/markdown`).
    """

    current_user_can_comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    Whether the current user is allowed to post comments on this wiki.
    """

    date_modified: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time at which the wiki was last modified, as an iso8601 formatted timestamp.
    """

    extra: typing.Optional[str] = pydantic.Field(default=None)
    """
    A dictionary containing additional metadata about this wiki, including version information.
    """

    kind: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of object.
    """

    materialized_path: typing.Optional[str] = pydantic.Field(default=None)
    """
    Materialized path to the wiki object.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name/title of the wiki page.
    """

    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    Path to the wiki object.
    """

    size: typing.Optional[str] = pydantic.Field(default=None)
    """
    Size of the wiki.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
