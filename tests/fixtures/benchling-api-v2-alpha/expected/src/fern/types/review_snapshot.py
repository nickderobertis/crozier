

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .review_snapshot_status import ReviewSnapshotStatus


class ReviewSnapshot(UniversalBaseModel):
    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="DateTime the Review Snapshot was created at"),
    ] = None
    """
    DateTime the Review Snapshot was created at
    """

    download_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="downloadURL"),
        pydantic.Field(
            alias="downloadURL", description="A short-lived URL that can be used to download the original file."
        ),
    ] = None
    """
    A short-lived URL that can be used to download the original file.
    """

    expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(alias="expiresAt", description="DateTime the downloadURL expires."),
    ] = None
    """
    DateTime the downloadURL expires.
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Size, in bytes, of the snapshot file
    """

    status: typing.Optional[ReviewSnapshotStatus] = pydantic.Field(default=None)
    """
    the current status of the Snapshot process
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
