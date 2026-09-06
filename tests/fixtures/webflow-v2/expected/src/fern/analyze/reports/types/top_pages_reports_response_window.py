

import datetime as dt
import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata


class TopPagesReportsResponseWindow(UniversalBaseModel):
    """
    A reporting time window. `endTime` must be greater than `startTime`.
    """

    start_time: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="startTime"),
        pydantic.Field(
            alias="startTime", description="Inclusive start of the reporting window, in ISO 8601 / RFC 3339 format."
        ),
    ]
    """
    Inclusive start of the reporting window, in ISO 8601 / RFC 3339 format.
    """

    end_time: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="endTime"),
        pydantic.Field(
            alias="endTime", description="Exclusive end of the reporting window, in ISO 8601 / RFC 3339 format."
        ),
    ]
    """
    Exclusive end of the reporting window, in ISO 8601 / RFC 3339 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
