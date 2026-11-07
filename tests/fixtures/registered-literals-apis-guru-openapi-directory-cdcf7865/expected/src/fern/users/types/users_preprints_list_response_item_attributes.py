

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UsersPreprintsListResponseItemAttributes(UniversalBaseModel):
    """
    The properties of the preprint entity.
    """

    date_created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the preprint was created, as an iso8601 formatted timestamp.
    """

    date_modified: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the preprint was last modified, as an iso8601 formatted timestamp.
    """

    date_published: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time at which the preprint was published, as an iso8601 formatted timestamp.
    """

    doi: typing.Optional[str] = pydantic.Field(default=None)
    """
    The DOI of the associated journal article, as entered by the user, if the preprint is published.
    """

    is_preprint_orphan: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the preprint is orphaned. A preprint can be orphaned if it's primary file was removed from the preprint node. This field may be deprecated in future versions.
    """

    license_record: typing.Optional[str] = pydantic.Field(default=None)
    """
    The metadata (copyright year and holder) associated with a license, required for certain licenses.
    """

    subjects: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A nested array structure that describe subjects related to the preprint, in the BePress taxonomy. Each dictionary contains the text and ID of a subject.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
