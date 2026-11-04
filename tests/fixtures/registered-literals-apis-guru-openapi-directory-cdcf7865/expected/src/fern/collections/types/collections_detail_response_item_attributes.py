

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CollectionsDetailResponseItemAttributes(UniversalBaseModel):
    """
    The properties of the collection.
    """

    bookmarks: typing.Optional[bool] = pydantic.Field(default=None)
    """
    This attribute indicates if a collection is being used as part of the bookmarking feature that allows each user to create a personal collection.
    """

    collected_type_choices: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of the acceptable entity `collected_type` metadata options acceptable for entities in the a collection. This indicates the collected types of entities within a collection.
    """

    date_created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the collection was created, as an iso8601 formatted timestamp.
    """

    date_modified: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the collection was last modified, as an iso8601 formatted timestamp.
    """

    is_promoted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    ???
    """

    is_public: typing.Optional[bool] = pydantic.Field(default=None)
    """
    This attribute indicates if a collection is viewable to a user with no special permissions.
    """

    issue_choices: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of the acceptable entity `issue` metadata options acceptable for entities in the a collection.  This indicates what issues exist of a multi-issue collection.
    """

    program_area_choices: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of the acceptable entity `program_area` metadata options acceptable for entities in the a collection.  This indicates what program areas a collection is composed of .
    """

    status_choices: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of the acceptable entity `status` metadata options acceptable for entities in the a collection. This indicates the status of a entity within a collection.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the collection.
    """

    volume_choices: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of the acceptable entity `volume` metadata options acceptable for entities in the a collection.  This indicates what volumes exist of a multi-volume collection.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
