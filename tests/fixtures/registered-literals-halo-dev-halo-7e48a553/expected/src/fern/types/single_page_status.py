

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .condition import Condition


class SinglePageStatus(UniversalBaseModel):
    """
    Observed single page state derived by content reconcilers.
    """

    comments_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="commentsCount"),
        pydantic.Field(alias="commentsCount", description="Total number of comments associated with the content item."),
    ] = None
    """
    Total number of comments associated with the content item.
    """

    conditions: typing.Optional[typing.List[Condition]] = pydantic.Field(default=None)
    """
    Reconciliation conditions reported by controllers for this content item.
    """

    contributors: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    User metadata.name values that contributed to the content snapshots.
    """

    excerpt: typing.Optional[str] = pydantic.Field(default=None)
    """
    Excerpt text resolved from the content excerpt configuration.
    """

    hide_from_list: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hideFromList"),
        pydantic.Field(
            alias="hideFromList",
            description="Whether any associated category hides this content item from theme-side lists.",
        ),
    ] = None
    """
    Whether any associated category hides this content item from theme-side lists.
    """

    in_progress: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="inProgress"),
        pydantic.Field(
            alias="inProgress", description="Whether the latest draft snapshot differs from the released snapshot."
        ),
    ] = None
    """
    Whether the latest draft snapshot differs from the released snapshot.
    """

    last_modify_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastModifyTime"),
        pydantic.Field(alias="lastModifyTime", description="Last modification time of the released snapshot."),
    ] = None
    """
    Last modification time of the released snapshot.
    """

    observed_version: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="observedVersion"),
        pydantic.Field(
            alias="observedVersion", description="Metadata version observed by the last successful reconciliation."
        ),
    ] = None
    """
    Metadata version observed by the last successful reconciliation.
    """

    permalink: typing.Optional[str] = pydantic.Field(default=None)
    """
    Absolute permalink calculated from the content permalink policy.
    """

    phase: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current publishing phase, such as DRAFT, PENDING_APPROVAL, PUBLISHED, or FAILED.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
