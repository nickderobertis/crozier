

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FilesVersionsResponseItemAttributes(UniversalBaseModel):
    """
    The properties of the file versions entity.
    """

    content_type: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    MIME content-type for the file (null if unavailable).
    """

    date_created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date of the file version creation, as an iso8601 formatted timestamp.
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Size of the file in bytes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
