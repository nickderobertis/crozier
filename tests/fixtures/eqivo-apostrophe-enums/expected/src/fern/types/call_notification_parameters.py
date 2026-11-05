

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .call_notification_parameters_answered_by import CallNotificationParametersAnsweredBy
from .call_notification_parameters_call_status import CallNotificationParametersCallStatus
from .call_notification_parameters_direction import CallNotificationParametersDirection


class CallNotificationParameters(UniversalBaseModel):
    a_leg_request_uuid: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ALegRequestUUID"),
        pydantic.Field(alias="ALegRequestUUID", description="A leg call request's unique identifier"),
    ] = None
    """
    A leg call request's unique identifier
    """

    a_leg_uuid: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ALegUUID"),
        pydantic.Field(alias="ALegUUID", description="A leg call's unique identifier, assigned by FreeSWITCH"),
    ] = None
    """
    A leg call's unique identifier, assigned by FreeSWITCH
    """

    answered_by: typing_extensions.Annotated[
        typing.Optional[CallNotificationParametersAnsweredBy],
        FieldMetadata(alias="AnsweredBy"),
        pydantic.Field(alias="AnsweredBy", description="Answering actor, when answering machine detection is enabled"),
    ] = None
    """
    Answering actor, when answering machine detection is enabled
    """

    call_status: typing_extensions.Annotated[
        CallNotificationParametersCallStatus,
        FieldMetadata(alias="CallStatus"),
        pydantic.Field(alias="CallStatus", description="Call's current status"),
    ]
    """
    Call's current status
    """

    call_uuid: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="CallUUID"),
        pydantic.Field(alias="CallUUID", description="Call's unique identifier, assigned by FreeSWITCH"),
    ]
    """
    Call's unique identifier, assigned by FreeSWITCH
    """

    caller_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="CallerName"),
        pydantic.Field(alias="CallerName", description="Caller name set for the call"),
    ]
    """
    Caller name set for the call
    """

    core_uuid: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="CoreUUID"),
        pydantic.Field(alias="CoreUUID", description="FreeSWITCH's instance unique identifier (Eqivo extension)"),
    ]
    """
    FreeSWITCH's instance unique identifier (Eqivo extension)
    """

    direction: typing_extensions.Annotated[
        CallNotificationParametersDirection,
        FieldMetadata(alias="Direction"),
        pydantic.Field(alias="Direction", description="Call's direction"),
    ]
    """
    Call's direction
    """

    forwarded_from: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ForwardedFrom"),
        pydantic.Field(alias="ForwardedFrom", description="Original call destination (before diversion)"),
    ] = None
    """
    Original call destination (before diversion)
    """

    from_: typing_extensions.Annotated[
        str, FieldMetadata(alias="From"), pydantic.Field(alias="From", description="Caller ID set for the call")
    ]
    """
    Caller ID set for the call
    """

    machine_detection_duration: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="MachineDetectionDuration"),
        pydantic.Field(
            alias="MachineDetectionDuration",
            description="Actual answering machine detection assessment duration (in milliseconds)",
        ),
    ] = None
    """
    Actual answering machine detection assessment duration (in milliseconds)
    """

    rest_api_server: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="RestApiServer"),
        pydantic.Field(
            alias="RestApiServer", description="Eqivo Rest API server which controls the call (Eqivo extension)"
        ),
    ]
    """
    Eqivo Rest API server which controls the call (Eqivo extension)
    """

    scheduled_hangup_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ScheduledHangupId"),
        pydantic.Field(alias="ScheduledHangupId", description="Unique identifier of the scheduled hangup task"),
    ] = None
    """
    Unique identifier of the scheduled hangup task
    """

    to: typing_extensions.Annotated[
        str, FieldMetadata(alias="To"), pydantic.Field(alias="To", description="Called phone number")
    ]
    """
    Called phone number
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
