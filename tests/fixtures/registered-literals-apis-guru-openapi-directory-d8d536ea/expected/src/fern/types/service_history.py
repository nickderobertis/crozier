

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ServiceHistory(UniversalBaseModel):
    """
    A timeline of courts where the judge has been employed.
    """

    appointed_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="appointedBy"),
        pydantic.Field(alias="appointedBy", description="The President-in-charge of the Judges appointment."),
    ] = None
    """
    The President-in-charge of the Judges appointment.
    """

    from_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="fromDate"),
        pydantic.Field(
            alias="fromDate", description="The year in which the Judge began practicing in his current service."
        ),
    ] = None
    """
    The year in which the Judge began practicing in his current service.
    """

    from_year: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="fromYear"),
        pydantic.Field(
            alias="fromYear", description="The year in which the Judge began practicing in his current service."
        ),
    ] = None
    """
    The year in which the Judge began practicing in his current service.
    """

    is_visible: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isVisible"),
        pydantic.Field(alias="isVisible", description="Boolean indicating if the service history  is visible or not."),
    ]
    """
    Boolean indicating if the service history  is visible or not.
    """

    object: str
    reason_for_termination: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="reasonForTermination"),
        pydantic.Field(
            alias="reasonForTermination", description="The reason for the Judges termination for the current position."
        ),
    ] = None
    """
    The reason for the Judges termination for the current position.
    """

    source_court: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sourceCourt"),
        pydantic.Field(
            alias="sourceCourt", description="The court served by the Judge. The court is taken from source."
        ),
    ] = None
    """
    The court served by the Judge. The court is taken from source.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Title held by the Judge.
    """

    to_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="toDate"),
        pydantic.Field(
            alias="toDate", description="The year in which the Judge stoped practicing in his current service."
        ),
    ] = None
    """
    The year in which the Judge stoped practicing in his current service.
    """

    to_year: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="toYear"),
        pydantic.Field(
            alias="toYear", description="The year in which the Judge stoped practicing in his current service."
        ),
    ] = None
    """
    The year in which the Judge stoped practicing in his current service.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
