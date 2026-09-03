

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .participant_endpoints import ParticipantEndpoints
from .participant_industry import ParticipantIndustry
from .participant_status import ParticipantStatus


class Participant(UniversalBaseModel):
    participant_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="participantId"),
        pydantic.Field(alias="participantId", description="Eindeutige Teilnehmer-ID"),
    ] = None
    """
    Eindeutige Teilnehmer-ID
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name der Institution
    """

    industry: typing.Optional[ParticipantIndustry] = None
    endpoints: typing.Optional[ParticipantEndpoints] = pydantic.Field(default=None)
    """
    API-Endpunkte
    """

    certificates: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    TLS-Zertifikate für mTLS
    """

    status: typing.Optional[ParticipantStatus] = None
    last_seen: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastSeen"), pydantic.Field(alias="lastSeen")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
