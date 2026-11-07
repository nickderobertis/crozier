

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case import Case
from .case_update_pacer_options_response import CaseUpdatePacerOptionsResponse
from .last_tracked_details import LastTrackedDetails
from .schedule import Schedule


class CaseTrack(UniversalBaseModel):
    case: typing.Optional[Case] = None
    case_api: typing_extensions.Annotated[str, FieldMetadata(alias="caseAPI"), pydantic.Field(alias="caseAPI")]
    case_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="caseId"),
        pydantic.Field(alias="caseId", description="Unique Id for a Case in UniCourt."),
    ]
    """
    Unique Id for a Case in UniCourt.
    """

    last_fetch_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastFetchDate"),
        pydantic.Field(
            alias="lastFetchDate",
            description="The date and time when the case was last fetched from the Court. This date and time is in UTC. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz, Note: It is not necessary that every time the case is fetched from Court we find changes in the case information. It could be that we already have the latest information from the Court and no changes exist.",
        ),
    ] = None
    """
    The date and time when the case was last fetched from the Court. This date and time is in UTC. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz, Note: It is not necessary that every time the case is fetched from Court we find changes in the case information. It could be that we already have the latest information from the Court and no changes exist.
    """

    last_fetch_date_with_updates: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastFetchDateWithUpdates"),
        pydantic.Field(
            alias="lastFetchDateWithUpdates",
            description="The date and time when the case was last fetched from the Court where we found changes in the case information. This date and time is in UTC. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz,",
        ),
    ] = None
    """
    The date and time when the case was last fetched from the Court where we found changes in the case information. This date and time is in UTC. Formatted as YYYY-MM-DDTHH:MM:SS+ZZ:zz,
    """

    last_tracked_details: typing_extensions.Annotated[
        LastTrackedDetails, FieldMetadata(alias="lastTrackedDetails"), pydantic.Field(alias="lastTrackedDetails")
    ]
    object: str = pydantic.Field()
    """
    Name of the object.
    """

    pacer_options: typing_extensions.Annotated[
        typing.Optional[CaseUpdatePacerOptionsResponse],
        FieldMetadata(alias="pacerOptions"),
        pydantic.Field(alias="pacerOptions"),
    ] = None
    schedule: Schedule

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
