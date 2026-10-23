

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetStatusResponseJobsItemMetadataBacklog(UniversalBaseModel):
    """
    Metadata queue measured after this job's last successful batch. Null means no batch has reported coverage yet; a fresh batch does not imply complete token coverage.
    """

    total: int
    due: int
    visible_due: typing_extensions.Annotated[int, FieldMetadata(alias="visibleDue"), pydantic.Field(alias="visibleDue")]
    never_read: typing_extensions.Annotated[int, FieldMetadata(alias="neverRead"), pydantic.Field(alias="neverRead")]
    errors: int
    oldest_checked_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="oldestCheckedAt"), pydantic.Field(alias="oldestCheckedAt")
    ] = None
    measured_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="measuredAt"), pydantic.Field(alias="measuredAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
