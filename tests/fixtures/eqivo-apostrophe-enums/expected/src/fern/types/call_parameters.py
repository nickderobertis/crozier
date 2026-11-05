

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .call_parameters_async_amd_status_callback_method import CallParametersAsyncAmdStatusCallbackMethod
from .call_parameters_machine_detection import CallParametersMachineDetection


class CallParameters(UniversalBaseModel):
    answer_url: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="AnswerUrl"),
        pydantic.Field(
            alias="AnswerUrl", description="Fully qualified URL which will provide the RestXML once the call connects"
        ),
    ]
    """
    Fully qualified URL which will provide the RestXML once the call connects
    """

    async_amd: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="AsyncAMD"),
        pydantic.Field(
            alias="AsyncAMD",
            description="When set to `true`, the call flow execution is blocked until answering machine detection is complete (an Eqivo extension)",
        ),
    ] = None
    """
    When set to `true`, the call flow execution is blocked until answering machine detection is complete (an Eqivo extension)
    """

    async_amd_status_callback: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AsyncAmdStatusCallback"),
        pydantic.Field(
            alias="AsyncAmdStatusCallback",
            description="Fully qualified URL to which the answering machine detection result will be sent. `AnsweredBy` and `MachineDetectionDuration` are appended to the usual [call notification parameters](#/components/schemas/CallNotificationParameters) (an Eqivo extension)",
        ),
    ] = None
    """
    Fully qualified URL to which the answering machine detection result will be sent. `AnsweredBy` and `MachineDetectionDuration` are appended to the usual [call notification parameters](#/components/schemas/CallNotificationParameters) (an Eqivo extension)
    """

    async_amd_status_callback_method: typing_extensions.Annotated[
        typing.Optional[CallParametersAsyncAmdStatusCallbackMethod],
        FieldMetadata(alias="AsyncAmdStatusCallbackMethod"),
        pydantic.Field(
            alias="AsyncAmdStatusCallbackMethod",
            description="HTTP method to be used when answering machine detection is completed (an Eqivo extension)",
        ),
    ] = None
    """
    HTTP method to be used when answering machine detection is completed (an Eqivo extension)
    """

    caller_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CallerName"),
        pydantic.Field(alias="CallerName", description="Caller Name to be set for the call"),
    ] = None
    """
    Caller Name to be set for the call
    """

    core_uuid: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CoreUUID"),
        pydantic.Field(
            alias="CoreUUID", description="Core UUID of the desired FreeSWITCH instance (an Eqivo extension)"
        ),
    ] = None
    """
    Core UUID of the desired FreeSWITCH instance (an Eqivo extension)
    """

    extra_dial_string: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ExtraDialString"),
        pydantic.Field(
            alias="ExtraDialString",
            description="Additional [channel variables](https://freeswitch.org/confluence/display/FREESWITCH/Channel+Variables) to be added to the originate FreeSWITCH API call.",
        ),
    ] = None
    """
    Additional [channel variables](https://freeswitch.org/confluence/display/FREESWITCH/Channel+Variables) to be added to the originate FreeSWITCH API call.
    """

    from_: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="From"),
        pydantic.Field(alias="From", description="Phone number to be used as Caller ID"),
    ]
    """
    Phone number to be used as Caller ID
    """

    gateway_codecs: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="GatewayCodecs"),
        pydantic.Field(
            alias="GatewayCodecs",
            description="List of codec(s) to be used for each gateway. Enclose codec groups in single quotes",
        ),
    ] = None
    """
    List of codec(s) to be used for each gateway. Enclose codec groups in single quotes
    """

    gateway_retries: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="GatewayRetries"),
        pydantic.Field(alias="GatewayRetries", description="List of maximum retry counts for each gateway"),
    ] = None
    """
    List of maximum retry counts for each gateway
    """

    gateway_timeouts: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="GatewayTimeouts"),
        pydantic.Field(
            alias="GatewayTimeouts", description="List of maximum timeout amounts (in seconds) for each gateway"
        ),
    ] = None
    """
    List of maximum timeout amounts (in seconds) for each gateway
    """

    gateways: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Gateways"),
        pydantic.Field(
            alias="Gateways",
            description="Comma separated FreeSWITCH gateway strings. When multiple gateways are specified, they will be tried sequentially (failover)",
        ),
    ]
    """
    Comma separated FreeSWITCH gateway strings. When multiple gateways are specified, they will be tried sequentially (failover)
    """

    hangup_on_ring: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="HangupOnRing"),
        pydantic.Field(
            alias="HangupOnRing",
            description="Schedules the call's hangup at a given time offset (in seconds) after the destination starts ringing",
        ),
    ] = None
    """
    Schedules the call's hangup at a given time offset (in seconds) after the destination starts ringing
    """

    hangup_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="HangupUrl"),
        pydantic.Field(
            alias="HangupUrl",
            description="Fully qualified URL to which the call hangup notification will be POSTed. `HangupCause` is added to the usual call [call notification parameters](#/components/schemas/CallNotificationParameters)",
        ),
    ] = None
    """
    Fully qualified URL to which the call hangup notification will be POSTed. `HangupCause` is added to the usual call [call notification parameters](#/components/schemas/CallNotificationParameters)
    """

    machine_detection: typing_extensions.Annotated[
        typing.Optional[CallParametersMachineDetection],
        FieldMetadata(alias="MachineDetection"),
        pydantic.Field(
            alias="MachineDetection",
            description="Enables answering machine detection; optionally, it waits until the greeting message has been played back (an Eqivo extension)",
        ),
    ] = None
    """
    Enables answering machine detection; optionally, it waits until the greeting message has been played back (an Eqivo extension)
    """

    machine_detection_silence_timeout: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="MachineDetectionSilenceTimeout"),
        pydantic.Field(
            alias="MachineDetectionSilenceTimeout",
            description="Initial silence threshold (in milliseconds, an Eqivo extension)",
        ),
    ] = None
    """
    Initial silence threshold (in milliseconds, an Eqivo extension)
    """

    machine_detection_speech_end_threshold: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="MachineDetectionSpeechEndThreshold"),
        pydantic.Field(
            alias="MachineDetectionSpeechEndThreshold",
            description="Silence threshold (in milliseconds, an Eqivo extension)",
        ),
    ] = None
    """
    Silence threshold (in milliseconds, an Eqivo extension)
    """

    machine_detection_speech_threshold: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="MachineDetectionSpeechThreshold"),
        pydantic.Field(
            alias="MachineDetectionSpeechThreshold",
            description="Speech activity/utterance threshold (in milliseconds, an Eqivo extension)",
        ),
    ] = None
    """
    Speech activity/utterance threshold (in milliseconds, an Eqivo extension)
    """

    machine_detection_timeout: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="MachineDetectionTimeout"),
        pydantic.Field(
            alias="MachineDetectionTimeout",
            description="Amount of time (in seconds) allotted for answering machine detection assessment (an Eqivo extension)",
        ),
    ] = None
    """
    Amount of time (in seconds) allotted for answering machine detection assessment (an Eqivo extension)
    """

    ring_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="RingUrl"),
        pydantic.Field(
            alias="RingUrl",
            description="Fully qualified URL to which the call ringing notification will be POSTed. `RequestUUID` and `CallUUID` is added to the usual [call notification parameters](#/components/schemas/CallNotificationParameters)",
        ),
    ] = None
    """
    Fully qualified URL to which the call ringing notification will be POSTed. `RequestUUID` and `CallUUID` is added to the usual [call notification parameters](#/components/schemas/CallNotificationParameters)
    """

    send_digits: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="SendDigits"),
        pydantic.Field(
            alias="SendDigits",
            description="DTMF tones to be sent when the call is answered. Each occurrence of `w` implies a 0.5 seconds delay whereas `W` will apply a whole second delay. To alter the tone duration (by default, 2000ms), append `@` and the length in milliseconds at the end of the string",
        ),
    ] = None
    """
    DTMF tones to be sent when the call is answered. Each occurrence of `w` implies a 0.5 seconds delay whereas `W` will apply a whole second delay. To alter the tone duration (by default, 2000ms), append `@` and the length in milliseconds at the end of the string
    """

    send_on_preanswer: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="SendOnPreanswer"),
        pydantic.Field(
            alias="SendOnPreanswer",
            description="When set to `true`, DTMF tones will be sent as early media rather than when the call is answered",
        ),
    ] = None
    """
    When set to `true`, DTMF tones will be sent as early media rather than when the call is answered
    """

    time_limit: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="TimeLimit"),
        pydantic.Field(
            alias="TimeLimit",
            description="Schedules the call's hangup at a given time offset (in seconds) after the call is answered",
        ),
    ] = None
    """
    Schedules the call's hangup at a given time offset (in seconds) after the call is answered
    """

    to: typing_extensions.Annotated[
        str, FieldMetadata(alias="To"), pydantic.Field(alias="To", description="Phone number to be called")
    ]
    """
    Phone number to be called
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
