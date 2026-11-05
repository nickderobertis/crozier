

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BulkCallParameters(UniversalBaseModel):
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

    caller_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CallerName"),
        pydantic.Field(alias="CallerName", description="Caller Name to be set for the call"),
    ] = None
    """
    Caller Name to be set for the call
    """

    confirm_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ConfirmKey"),
        pydantic.Field(alias="ConfirmKey", description="DTMF tone the called party must send to accept the call"),
    ] = None
    """
    DTMF tone the called party must send to accept the call
    """

    confirm_sound: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ConfirmSound"),
        pydantic.Field(
            alias="ConfirmSound",
            description="Remote URL to fetch with POST HTTP request which must return a RestXML with Play, Wait and/or Speak Elements only (all others are ignored). This RESTXML is played to the called party when he answered",
        ),
    ] = None
    """
    Remote URL to fetch with POST HTTP request which must return a RestXML with Play, Wait and/or Speak Elements only (all others are ignored). This RESTXML is played to the called party when he answered
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

    delimiter: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Delimiter"),
        pydantic.Field(
            alias="Delimiter",
            description="Any character, except `/` and `,`, which will be used as a separator within several parameters",
        ),
    ]
    """
    Any character, except `/` and `,`, which will be used as a separator within several parameters
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

    reject_causes: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="RejectCauses"),
        pydantic.Field(alias="RejectCauses", description="Comma separated reject causes"),
    ] = None
    """
    Comma separated reject causes
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
