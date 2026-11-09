

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .case_update_pacer_options_response import CaseUpdatePacerOptionsResponse
from .exception import Exception


class LastTrackedDetails(UniversalBaseModel):
    last_track_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastTrackDate"),
        pydantic.Field(
            alias="lastTrackDate", description="The date and time when the case was tracked for this account."
        ),
    ] = None
    """
    The date and time when the case was tracked for this account.
    """

    last_track_exception: typing_extensions.Annotated[
        typing.Optional[Exception],
        FieldMetadata(alias="lastTrackException"),
        pydantic.Field(alias="lastTrackException"),
    ] = None
    object: str = pydantic.Field()
    """
    Name of the object.
    """

    pacer_options: typing_extensions.Annotated[
        typing.Optional[CaseUpdatePacerOptionsResponse],
        FieldMetadata(alias="pacerOptions"),
        pydantic.Field(alias="pacerOptions"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
