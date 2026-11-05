

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bulk_call_response import BulkCallResponse
from ..types.call_parameters_async_amd_status_callback_method import CallParametersAsyncAmdStatusCallbackMethod
from ..types.call_parameters_machine_detection import CallParametersMachineDetection
from ..types.call_response import CallResponse
from ..types.cancel_scheduled_hangup_response import CancelScheduledHangupResponse
from ..types.cancel_scheduled_play_response import CancelScheduledPlayResponse
from ..types.group_call_response import GroupCallResponse
from ..types.hangup_all_calls_response import HangupAllCallsResponse
from ..types.hangup_call_response import HangupCallResponse
from ..types.play_parameters_legs import PlayParametersLegs
from ..types.play_response import PlayResponse
from ..types.play_stop_response import PlayStopResponse
from ..types.record_start_parameters_file_format import RecordStartParametersFileFormat
from ..types.record_start_response import RecordStartResponse
from ..types.record_stop_response import RecordStopResponse
from ..types.schedule_hangup_response import ScheduleHangupResponse
from ..types.schedule_play_parameters_legs import SchedulePlayParametersLegs
from ..types.schedule_play_response import SchedulePlayResponse
from ..types.send_digits_parameters_leg import SendDigitsParametersLeg
from ..types.send_digits_response import SendDigitsResponse
from ..types.sound_touch_parameters_audio_direction import SoundTouchParametersAudioDirection
from ..types.sound_touch_response import SoundTouchResponse
from ..types.sound_touch_stop_response import SoundTouchStopResponse
from ..types.transfer_call_response import TransferCallResponse
from .raw_client import AsyncRawCallClient, RawCallClient


OMIT = typing.cast(typing.Any, ...)


class CallClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCallClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCallClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCallClient
        """
        return self._raw_client

    def v01bulk_call(
        self,
        *,
        answer_url: str,
        delimiter: str,
        from_: str,
        gateways: str,
        to: str,
        caller_name: typing.Optional[str] = OMIT,
        confirm_key: typing.Optional[str] = OMIT,
        confirm_sound: typing.Optional[str] = OMIT,
        core_uuid: typing.Optional[str] = OMIT,
        extra_dial_string: typing.Optional[str] = OMIT,
        gateway_codecs: typing.Optional[str] = OMIT,
        gateway_retries: typing.Optional[str] = OMIT,
        gateway_timeouts: typing.Optional[str] = OMIT,
        hangup_on_ring: typing.Optional[int] = OMIT,
        hangup_url: typing.Optional[str] = OMIT,
        reject_causes: typing.Optional[str] = OMIT,
        ring_url: typing.Optional[str] = OMIT,
        send_digits: typing.Optional[str] = OMIT,
        send_on_preanswer: typing.Optional[bool] = OMIT,
        time_limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkCallResponse:
        """
        Initiates multiple concurrent outbound calls

        Parameters
        ----------
        answer_url : str
            Fully qualified URL which will provide the RestXML once the call connects

        delimiter : str
            Any character, except `/` and `,`, which will be used as a separator within several parameters

        from_ : str
            Phone number to be used as Caller ID

        gateways : str
            Comma separated FreeSWITCH gateway strings. When multiple gateways are specified, they will be tried sequentially (failover)

        to : str
            Phone number to be called

        caller_name : typing.Optional[str]
            Caller Name to be set for the call

        confirm_key : typing.Optional[str]
            DTMF tone the called party must send to accept the call

        confirm_sound : typing.Optional[str]
            Remote URL to fetch with POST HTTP request which must return a RestXML with Play, Wait and/or Speak Elements only (all others are ignored). This RESTXML is played to the called party when he answered

        core_uuid : typing.Optional[str]
            Core UUID of the desired FreeSWITCH instance (an Eqivo extension)

        extra_dial_string : typing.Optional[str]
            Additional [channel variables](https://freeswitch.org/confluence/display/FREESWITCH/Channel+Variables) to be added to the originate FreeSWITCH API call.

        gateway_codecs : typing.Optional[str]
            List of codec(s) to be used for each gateway. Enclose codec groups in single quotes

        gateway_retries : typing.Optional[str]
            List of maximum retry counts for each gateway

        gateway_timeouts : typing.Optional[str]
            List of maximum timeout amounts (in seconds) for each gateway

        hangup_on_ring : typing.Optional[int]
            Schedules the call's hangup at a given time offset (in seconds) after the destination starts ringing

        hangup_url : typing.Optional[str]
            Fully qualified URL to which the call hangup notification will be POSTed. `HangupCause` is added to the usual call [call notification parameters](#/components/schemas/CallNotificationParameters)

        reject_causes : typing.Optional[str]
            Comma separated reject causes

        ring_url : typing.Optional[str]
            Fully qualified URL to which the call ringing notification will be POSTed. `RequestUUID` and `CallUUID` is added to the usual [call notification parameters](#/components/schemas/CallNotificationParameters)

        send_digits : typing.Optional[str]
            DTMF tones to be sent when the call is answered. Each occurrence of `w` implies a 0.5 seconds delay whereas `W` will apply a whole second delay. To alter the tone duration (by default, 2000ms), append `@` and the length in milliseconds at the end of the string

        send_on_preanswer : typing.Optional[bool]
            When set to `true`, DTMF tones will be sent as early media rather than when the call is answered

        time_limit : typing.Optional[int]
            Schedules the call's hangup at a given time offset (in seconds) after the call is answered

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkCallResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.call.v01bulk_call(
            answer_url="https://example.com/answer/",
            delimiter="<",
            from_="15551234567",
            gateways="user/,sofia/gateway/PSTNgateway1/,sofia/gateway/PSTNgateway2/",
            to="15557654321",
        )
        """
        _response = self._raw_client.v01bulk_call(
            answer_url=answer_url,
            delimiter=delimiter,
            from_=from_,
            gateways=gateways,
            to=to,
            caller_name=caller_name,
            confirm_key=confirm_key,
            confirm_sound=confirm_sound,
            core_uuid=core_uuid,
            extra_dial_string=extra_dial_string,
            gateway_codecs=gateway_codecs,
            gateway_retries=gateway_retries,
            gateway_timeouts=gateway_timeouts,
            hangup_on_ring=hangup_on_ring,
            hangup_url=hangup_url,
            reject_causes=reject_causes,
            ring_url=ring_url,
            send_digits=send_digits,
            send_on_preanswer=send_on_preanswer,
            time_limit=time_limit,
            request_options=request_options,
        )
        return _response.data

    def v01call(
        self,
        *,
        answer_url: str,
        from_: str,
        gateways: str,
        to: str,
        async_amd: typing.Optional[bool] = OMIT,
        async_amd_status_callback: typing.Optional[str] = OMIT,
        async_amd_status_callback_method: typing.Optional[CallParametersAsyncAmdStatusCallbackMethod] = OMIT,
        caller_name: typing.Optional[str] = OMIT,
        core_uuid: typing.Optional[str] = OMIT,
        extra_dial_string: typing.Optional[str] = OMIT,
        gateway_codecs: typing.Optional[str] = OMIT,
        gateway_retries: typing.Optional[str] = OMIT,
        gateway_timeouts: typing.Optional[str] = OMIT,
        hangup_on_ring: typing.Optional[int] = OMIT,
        hangup_url: typing.Optional[str] = OMIT,
        machine_detection: typing.Optional[CallParametersMachineDetection] = OMIT,
        machine_detection_silence_timeout: typing.Optional[int] = OMIT,
        machine_detection_speech_end_threshold: typing.Optional[int] = OMIT,
        machine_detection_speech_threshold: typing.Optional[int] = OMIT,
        machine_detection_timeout: typing.Optional[int] = OMIT,
        ring_url: typing.Optional[str] = OMIT,
        send_digits: typing.Optional[str] = OMIT,
        send_on_preanswer: typing.Optional[bool] = OMIT,
        time_limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CallResponse:
        """
        Initiates an outbound call

        Parameters
        ----------
        answer_url : str
            Fully qualified URL which will provide the RestXML once the call connects

        from_ : str
            Phone number to be used as Caller ID

        gateways : str
            Comma separated FreeSWITCH gateway strings. When multiple gateways are specified, they will be tried sequentially (failover)

        to : str
            Phone number to be called

        async_amd : typing.Optional[bool]
            When set to `true`, the call flow execution is blocked until answering machine detection is complete (an Eqivo extension)

        async_amd_status_callback : typing.Optional[str]
            Fully qualified URL to which the answering machine detection result will be sent. `AnsweredBy` and `MachineDetectionDuration` are appended to the usual [call notification parameters](#/components/schemas/CallNotificationParameters) (an Eqivo extension)

        async_amd_status_callback_method : typing.Optional[CallParametersAsyncAmdStatusCallbackMethod]
            HTTP method to be used when answering machine detection is completed (an Eqivo extension)

        caller_name : typing.Optional[str]
            Caller Name to be set for the call

        core_uuid : typing.Optional[str]
            Core UUID of the desired FreeSWITCH instance (an Eqivo extension)

        extra_dial_string : typing.Optional[str]
            Additional [channel variables](https://freeswitch.org/confluence/display/FREESWITCH/Channel+Variables) to be added to the originate FreeSWITCH API call.

        gateway_codecs : typing.Optional[str]
            List of codec(s) to be used for each gateway. Enclose codec groups in single quotes

        gateway_retries : typing.Optional[str]
            List of maximum retry counts for each gateway

        gateway_timeouts : typing.Optional[str]
            List of maximum timeout amounts (in seconds) for each gateway

        hangup_on_ring : typing.Optional[int]
            Schedules the call's hangup at a given time offset (in seconds) after the destination starts ringing

        hangup_url : typing.Optional[str]
            Fully qualified URL to which the call hangup notification will be POSTed. `HangupCause` is added to the usual call [call notification parameters](#/components/schemas/CallNotificationParameters)

        machine_detection : typing.Optional[CallParametersMachineDetection]
            Enables answering machine detection; optionally, it waits until the greeting message has been played back (an Eqivo extension)

        machine_detection_silence_timeout : typing.Optional[int]
            Initial silence threshold (in milliseconds, an Eqivo extension)

        machine_detection_speech_end_threshold : typing.Optional[int]
            Silence threshold (in milliseconds, an Eqivo extension)

        machine_detection_speech_threshold : typing.Optional[int]
            Speech activity/utterance threshold (in milliseconds, an Eqivo extension)

        machine_detection_timeout : typing.Optional[int]
            Amount of time (in seconds) allotted for answering machine detection assessment (an Eqivo extension)

        ring_url : typing.Optional[str]
            Fully qualified URL to which the call ringing notification will be POSTed. `RequestUUID` and `CallUUID` is added to the usual [call notification parameters](#/components/schemas/CallNotificationParameters)

        send_digits : typing.Optional[str]
            DTMF tones to be sent when the call is answered. Each occurrence of `w` implies a 0.5 seconds delay whereas `W` will apply a whole second delay. To alter the tone duration (by default, 2000ms), append `@` and the length in milliseconds at the end of the string

        send_on_preanswer : typing.Optional[bool]
            When set to `true`, DTMF tones will be sent as early media rather than when the call is answered

        time_limit : typing.Optional[int]
            Schedules the call's hangup at a given time offset (in seconds) after the call is answered

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CallResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.call.v01call(
            answer_url="https://example.com/answer/",
            from_="15551234567",
            gateways="user/,sofia/gateway/PSTNgateway1/,sofia/gateway/PSTNgateway2/",
            to="15557654321",
        )
        """
        _response = self._raw_client.v01call(
            answer_url=answer_url,
            from_=from_,
            gateways=gateways,
            to=to,
            async_amd=async_amd,
            async_amd_status_callback=async_amd_status_callback,
            async_amd_status_callback_method=async_amd_status_callback_method,
            caller_name=caller_name,
            core_uuid=core_uuid,
            extra_dial_string=extra_dial_string,
            gateway_codecs=gateway_codecs,
            gateway_retries=gateway_retries,
            gateway_timeouts=gateway_timeouts,
            hangup_on_ring=hangup_on_ring,
            hangup_url=hangup_url,
            machine_detection=machine_detection,
            machine_detection_silence_timeout=machine_detection_silence_timeout,
            machine_detection_speech_end_threshold=machine_detection_speech_end_threshold,
            machine_detection_speech_threshold=machine_detection_speech_threshold,
            machine_detection_timeout=machine_detection_timeout,
            ring_url=ring_url,
            send_digits=send_digits,
            send_on_preanswer=send_on_preanswer,
            time_limit=time_limit,
            request_options=request_options,
        )
        return _response.data

    def v01cancel_scheduled_hangup(
        self, *, sched_hangup_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CancelScheduledHangupResponse:
        """
        Cancels a scheduled hangup for a call

        Parameters
        ----------
        sched_hangup_id : str
            Unique identifier returned when scheduled hangup was originally requested

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancelScheduledHangupResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.call.v01cancel_scheduled_hangup(
            sched_hangup_id="ea428fbd-ac9b-498c-8bb2-a36ac49f10fd",
        )
        """
        _response = self._raw_client.v01cancel_scheduled_hangup(
            sched_hangup_id=sched_hangup_id, request_options=request_options
        )
        return _response.data

    def v01cancel_scheduled_play(
        self, *, sched_play_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CancelScheduledPlayResponse:
        """
        Cancels a scheduled playback request

        Parameters
        ----------
        sched_play_id : str
            Unique identifier returned when scheduled playback was originally requested

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancelScheduledPlayResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.call.v01cancel_scheduled_play(
            sched_play_id="ea428fbd-ac9b-498c-8bb2-a36ac49f10fd",
        )
        """
        _response = self._raw_client.v01cancel_scheduled_play(
            sched_play_id=sched_play_id, request_options=request_options
        )
        return _response.data

    def v01group_call(
        self,
        *,
        answer_url: str,
        delimiter: str,
        from_: str,
        gateways: str,
        to: str,
        caller_name: typing.Optional[str] = OMIT,
        confirm_key: typing.Optional[str] = OMIT,
        confirm_sound: typing.Optional[str] = OMIT,
        core_uuid: typing.Optional[str] = OMIT,
        extra_dial_string: typing.Optional[str] = OMIT,
        gateway_codecs: typing.Optional[str] = OMIT,
        gateway_retries: typing.Optional[str] = OMIT,
        gateway_timeouts: typing.Optional[str] = OMIT,
        hangup_on_ring: typing.Optional[int] = OMIT,
        hangup_url: typing.Optional[str] = OMIT,
        reject_causes: typing.Optional[str] = OMIT,
        ring_url: typing.Optional[str] = OMIT,
        send_digits: typing.Optional[str] = OMIT,
        send_on_preanswer: typing.Optional[bool] = OMIT,
        time_limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupCallResponse:
        """
        Initiate multiple racing outbound calls

        Parameters
        ----------
        answer_url : str
            Fully qualified URL which will provide the RestXML once the call connects

        delimiter : str
            Any character, except `/` and `,`, which will be used as a separator within several parameters

        from_ : str
            Phone number to be used as Caller ID

        gateways : str
            Comma separated FreeSWITCH gateway strings. When multiple gateways are specified, they will be tried sequentially (failover)

        to : str
            Phone number to be called

        caller_name : typing.Optional[str]
            Caller Name to be set for the call

        confirm_key : typing.Optional[str]
            DTMF tone the called party must send to accept the call

        confirm_sound : typing.Optional[str]
            Remote URL to fetch with POST HTTP request which must return a RestXML with Play, Wait and/or Speak Elements only (all others are ignored). This RESTXML is played to the called party when he answered

        core_uuid : typing.Optional[str]
            Core UUID of the desired FreeSWITCH instance (an Eqivo extension)

        extra_dial_string : typing.Optional[str]
            Additional [channel variables](https://freeswitch.org/confluence/display/FREESWITCH/Channel+Variables) to be added to the originate FreeSWITCH API call.

        gateway_codecs : typing.Optional[str]
            List of codec(s) to be used for each gateway. Enclose codec groups in single quotes

        gateway_retries : typing.Optional[str]
            List of maximum retry counts for each gateway

        gateway_timeouts : typing.Optional[str]
            List of maximum timeout amounts (in seconds) for each gateway

        hangup_on_ring : typing.Optional[int]
            Schedules the call's hangup at a given time offset (in seconds) after the destination starts ringing

        hangup_url : typing.Optional[str]
            Fully qualified URL to which the call hangup notification will be POSTed. `HangupCause` is added to the usual call [call notification parameters](#/components/schemas/CallNotificationParameters)

        reject_causes : typing.Optional[str]
            Comma separated reject causes

        ring_url : typing.Optional[str]
            Fully qualified URL to which the call ringing notification will be POSTed. `RequestUUID` and `CallUUID` is added to the usual [call notification parameters](#/components/schemas/CallNotificationParameters)

        send_digits : typing.Optional[str]
            DTMF tones to be sent when the call is answered. Each occurrence of `w` implies a 0.5 seconds delay whereas `W` will apply a whole second delay. To alter the tone duration (by default, 2000ms), append `@` and the length in milliseconds at the end of the string

        send_on_preanswer : typing.Optional[bool]
            When set to `true`, DTMF tones will be sent as early media rather than when the call is answered

        time_limit : typing.Optional[int]
            Schedules the call's hangup at a given time offset (in seconds) after the call is answered

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupCallResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.call.v01group_call(
            answer_url="https://example.com/answer/",
            delimiter="<",
            from_="15551234567",
            gateways="user/,sofia/gateway/PSTNgateway1/,sofia/gateway/PSTNgateway2/",
            to="15557654321",
        )
        """
        _response = self._raw_client.v01group_call(
            answer_url=answer_url,
            delimiter=delimiter,
            from_=from_,
            gateways=gateways,
            to=to,
            caller_name=caller_name,
            confirm_key=confirm_key,
            confirm_sound=confirm_sound,
            core_uuid=core_uuid,
            extra_dial_string=extra_dial_string,
            gateway_codecs=gateway_codecs,
            gateway_retries=gateway_retries,
            gateway_timeouts=gateway_timeouts,
            hangup_on_ring=hangup_on_ring,
            hangup_url=hangup_url,
            reject_causes=reject_causes,
            ring_url=ring_url,
            send_digits=send_digits,
            send_on_preanswer=send_on_preanswer,
            time_limit=time_limit,
            request_options=request_options,
        )
        return _response.data

    def v01hangup_all_calls(self, *, request_options: typing.Optional[RequestOptions] = None) -> HangupAllCallsResponse:
        """
        Hangs up all established calls

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HangupAllCallsResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.call.v01hangup_all_calls()
        """
        _response = self._raw_client.v01hangup_all_calls(request_options=request_options)
        return _response.data

    def v01hangup_call(
        self,
        *,
        call_uuid: typing.Optional[str] = OMIT,
        request_uuid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HangupCallResponse:
        """
        Hangs up a specific call

        Parameters
        ----------
        call_uuid : typing.Optional[str]
            Unique identifier of the call (when established); this parameter is mutually exclusive with RequestUUID

        request_uuid : typing.Optional[str]
            Unique identifier of the API request (when the call is not established yet); this parameter is mutually exclusive with CallUUID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HangupCallResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.call.v01hangup_call()
        """
        _response = self._raw_client.v01hangup_call(
            call_uuid=call_uuid, request_uuid=request_uuid, request_options=request_options
        )
        return _response.data

    def v01play(
        self,
        *,
        call_uuid: str,
        sounds: str,
        legs: typing.Optional[PlayParametersLegs] = OMIT,
        length: typing.Optional[int] = OMIT,
        loop: typing.Optional[bool] = OMIT,
        mix: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PlayResponse:
        """
        Plays media into a live call

        Parameters
        ----------
        call_uuid : str
            Unique identifier of the call to play media into

        sounds : str
            Comma separated list of file paths/URIs to be played

        legs : typing.Optional[PlayParametersLegs]
            Call leg(s) for which the media will be played; `aleg` refers to the initial call leg, `bleg` refers to the bridged call leg, if applicable.

        length : typing.Optional[int]
            Maximum amount of time (in seconds) to playback the media

        loop : typing.Optional[bool]
            Loops the media file(s) indefinitely

        mix : typing.Optional[bool]
            Whether the media should be mixed with the call's audio stream

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlayResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.call.v01play(
            call_uuid="e69b32da-3243-4ba6-a965-5d2f64a57d48",
            sounds="/tmp/prompt.wav",
        )
        """
        _response = self._raw_client.v01play(
            call_uuid=call_uuid,
            sounds=sounds,
            legs=legs,
            length=length,
            loop=loop,
            mix=mix,
            request_options=request_options,
        )
        return _response.data

    def v01play_stop(
        self, *, call_uuid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PlayStopResponse:
        """
        Interrupts media playback on a given call

        Parameters
        ----------
        call_uuid : str
            Unique identifier of the call

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlayStopResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.call.v01play_stop(
            call_uuid="441afb63-85bc-49d4-9ac8-8459f9bf5e6b",
        )
        """
        _response = self._raw_client.v01play_stop(call_uuid=call_uuid, request_options=request_options)
        return _response.data

    def v01record_start(
        self,
        *,
        call_uuid: typing.Optional[str] = OMIT,
        file_format: typing.Optional[RecordStartParametersFileFormat] = OMIT,
        file_name: typing.Optional[str] = OMIT,
        file_path: typing.Optional[str] = OMIT,
        time_limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecordStartResponse:
        """
        Initiates recording of a given call

        Parameters
        ----------
        call_uuid : typing.Optional[str]
            Unique identifier of the call to be recorded

        file_format : typing.Optional[RecordStartParametersFileFormat]
            File format (extension)

        file_name : typing.Optional[str]
            Recording file name (without extension); if empty, a timestamp based file name will be generated

        file_path : typing.Optional[str]
            Directory path/URI where the recording file will be saved

        time_limit : typing.Optional[int]
            Maximum recording length, in seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordStartResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.call.v01record_start()
        """
        _response = self._raw_client.v01record_start(
            call_uuid=call_uuid,
            file_format=file_format,
            file_name=file_name,
            file_path=file_path,
            time_limit=time_limit,
            request_options=request_options,
        )
        return _response.data

    def v01record_stop(
        self, *, call_uuid: str, record_file: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RecordStopResponse:
        """
        Stops the recording of a given call

        Parameters
        ----------
        call_uuid : str
            Unique identifier of the call

        record_file : str
            Full path to recording file, as returned by RecordStart; `all` shorthand is also available

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordStopResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.call.v01record_stop(
            call_uuid="eacfa857-4001-4379-b79a-c7ef6d963bcb",
            record_file="/tmp/recording/sample.wav",
        )
        """
        _response = self._raw_client.v01record_stop(
            call_uuid=call_uuid, record_file=record_file, request_options=request_options
        )
        return _response.data

    def v01schedule_hangup(
        self, *, call_uuid: str, time: int, request_options: typing.Optional[RequestOptions] = None
    ) -> ScheduleHangupResponse:
        """
        Schedules a hangup for a specific call

        Parameters
        ----------
        call_uuid : str
            Unique identifier of the call

        time : int
            Time (in seconds) after which the call in question will be hung up

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduleHangupResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.call.v01schedule_hangup(
            call_uuid="f84fbadc-5df0-4c02-934b-aac0c1efb8ae",
            time=59,
        )
        """
        _response = self._raw_client.v01schedule_hangup(call_uuid=call_uuid, time=time, request_options=request_options)
        return _response.data

    def v01schedule_play(
        self,
        *,
        call_uuid: str,
        sounds: str,
        time: int,
        legs: typing.Optional[SchedulePlayParametersLegs] = OMIT,
        length: typing.Optional[int] = OMIT,
        loop: typing.Optional[bool] = OMIT,
        mix: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchedulePlayResponse:
        """
        Schedules media playback for a specific call

        Parameters
        ----------
        call_uuid : str
            Unique identifier of the call to play media into

        sounds : str
            Comma separated list of file paths/URIs to be played

        time : int
            Time (in seconds) after which the media will be playedback

        legs : typing.Optional[SchedulePlayParametersLegs]
            Call leg(s) for which the media will be played; `aleg` refers to the initial call leg, `bleg` refers to the bridged call leg, if applicable.

        length : typing.Optional[int]
            Maximum amount of time (in seconds) to playback the media

        loop : typing.Optional[bool]
            Loops the media file(s) indefinitely

        mix : typing.Optional[bool]
            Whether the media should be mixed with the call's audio stream

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchedulePlayResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.call.v01schedule_play(
            call_uuid="e69b32da-3243-4ba6-a965-5d2f64a57d48",
            sounds="/tmp/prompt.wav",
            time=29,
        )
        """
        _response = self._raw_client.v01schedule_play(
            call_uuid=call_uuid,
            sounds=sounds,
            time=time,
            legs=legs,
            length=length,
            loop=loop,
            mix=mix,
            request_options=request_options,
        )
        return _response.data

    def v01send_digits(
        self,
        *,
        call_uuid: str,
        digits: str,
        leg: typing.Optional[SendDigitsParametersLeg] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendDigitsResponse:
        """
        Emits DMTF tones to a call

        Parameters
        ----------
        call_uuid : str
            Unique identifier of the call to send DTMF to

        digits : str
            DTMF tones to be sent; each occurrence of `w` implies a 0.5 seconds delay whereas `W` will apply a whole second delay. To alter the tone duration (by default, 2000ms), append `@` and the length in milliseconds at the end of the string

        leg : typing.Optional[SendDigitsParametersLeg]
            Call leg(s) to which DTMFs will be sent; `aleg` refers to the initial call leg, `bleg` refers to the bridged call leg, if applicable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendDigitsResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.call.v01send_digits(
            call_uuid="d4cd08fe-4245-490a-ae39-5b58c6addbe8",
            digits="1w2w3W#*@1500",
        )
        """
        _response = self._raw_client.v01send_digits(
            call_uuid=call_uuid, digits=digits, leg=leg, request_options=request_options
        )
        return _response.data

    def v01sound_touch(
        self,
        *,
        call_uuid: str,
        audio_direction: typing.Optional[SoundTouchParametersAudioDirection] = OMIT,
        pitch: typing.Optional[float] = OMIT,
        pitch_octaves: typing.Optional[float] = OMIT,
        pitch_semi_tones: typing.Optional[float] = OMIT,
        rate: typing.Optional[float] = OMIT,
        tempo: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoundTouchResponse:
        """
        Applies SoundTouch effects to a live call

        Parameters
        ----------
        call_uuid : str
            Unique identifier of the call to send DTMF to

        audio_direction : typing.Optional[SoundTouchParametersAudioDirection]
            Media stream to be altered, incoming or outgoing

        pitch : typing.Optional[float]
            Adjust the pitch

        pitch_octaves : typing.Optional[float]
            Adjust the pitch in octaves

        pitch_semi_tones : typing.Optional[float]
            Adjust the pitch in semitones

        rate : typing.Optional[float]
            Adjust the rate

        tempo : typing.Optional[float]
            Adjust the tempo

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SoundTouchResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.call.v01sound_touch(
            call_uuid="b7054b68-0620-455a-8ac7-f8f126853b9d",
        )
        """
        _response = self._raw_client.v01sound_touch(
            call_uuid=call_uuid,
            audio_direction=audio_direction,
            pitch=pitch,
            pitch_octaves=pitch_octaves,
            pitch_semi_tones=pitch_semi_tones,
            rate=rate,
            tempo=tempo,
            request_options=request_options,
        )
        return _response.data

    def v01sound_touch_stop(
        self, *, call_uuid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SoundTouchStopResponse:
        """
        Removes SoundTouch effects from a given call

        Parameters
        ----------
        call_uuid : str
            Unique identifier of the call

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SoundTouchStopResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.call.v01sound_touch_stop(
            call_uuid="fe372011-face-4bc2-bbcc-893d045bf67d",
        )
        """
        _response = self._raw_client.v01sound_touch_stop(call_uuid=call_uuid, request_options=request_options)
        return _response.data

    def v01transfer_call(
        self, *, call_uuid: str, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TransferCallResponse:
        """
        Replaces the RestXML flow of a live call

        Parameters
        ----------
        call_uuid : str
            Unique identifier of the call

        url : str
            Absolute URL which will return the updated RestXML flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferCallResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.call.v01transfer_call(
            call_uuid="03694cf6-62b3-4f00-b0fc-6831ddcc2693",
            url="https://example.org/restxml/endpoint/",
        )
        """
        _response = self._raw_client.v01transfer_call(call_uuid=call_uuid, url=url, request_options=request_options)
        return _response.data


class AsyncCallClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCallClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCallClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCallClient
        """
        return self._raw_client

    async def v01bulk_call(
        self,
        *,
        answer_url: str,
        delimiter: str,
        from_: str,
        gateways: str,
        to: str,
        caller_name: typing.Optional[str] = OMIT,
        confirm_key: typing.Optional[str] = OMIT,
        confirm_sound: typing.Optional[str] = OMIT,
        core_uuid: typing.Optional[str] = OMIT,
        extra_dial_string: typing.Optional[str] = OMIT,
        gateway_codecs: typing.Optional[str] = OMIT,
        gateway_retries: typing.Optional[str] = OMIT,
        gateway_timeouts: typing.Optional[str] = OMIT,
        hangup_on_ring: typing.Optional[int] = OMIT,
        hangup_url: typing.Optional[str] = OMIT,
        reject_causes: typing.Optional[str] = OMIT,
        ring_url: typing.Optional[str] = OMIT,
        send_digits: typing.Optional[str] = OMIT,
        send_on_preanswer: typing.Optional[bool] = OMIT,
        time_limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkCallResponse:
        """
        Initiates multiple concurrent outbound calls

        Parameters
        ----------
        answer_url : str
            Fully qualified URL which will provide the RestXML once the call connects

        delimiter : str
            Any character, except `/` and `,`, which will be used as a separator within several parameters

        from_ : str
            Phone number to be used as Caller ID

        gateways : str
            Comma separated FreeSWITCH gateway strings. When multiple gateways are specified, they will be tried sequentially (failover)

        to : str
            Phone number to be called

        caller_name : typing.Optional[str]
            Caller Name to be set for the call

        confirm_key : typing.Optional[str]
            DTMF tone the called party must send to accept the call

        confirm_sound : typing.Optional[str]
            Remote URL to fetch with POST HTTP request which must return a RestXML with Play, Wait and/or Speak Elements only (all others are ignored). This RESTXML is played to the called party when he answered

        core_uuid : typing.Optional[str]
            Core UUID of the desired FreeSWITCH instance (an Eqivo extension)

        extra_dial_string : typing.Optional[str]
            Additional [channel variables](https://freeswitch.org/confluence/display/FREESWITCH/Channel+Variables) to be added to the originate FreeSWITCH API call.

        gateway_codecs : typing.Optional[str]
            List of codec(s) to be used for each gateway. Enclose codec groups in single quotes

        gateway_retries : typing.Optional[str]
            List of maximum retry counts for each gateway

        gateway_timeouts : typing.Optional[str]
            List of maximum timeout amounts (in seconds) for each gateway

        hangup_on_ring : typing.Optional[int]
            Schedules the call's hangup at a given time offset (in seconds) after the destination starts ringing

        hangup_url : typing.Optional[str]
            Fully qualified URL to which the call hangup notification will be POSTed. `HangupCause` is added to the usual call [call notification parameters](#/components/schemas/CallNotificationParameters)

        reject_causes : typing.Optional[str]
            Comma separated reject causes

        ring_url : typing.Optional[str]
            Fully qualified URL to which the call ringing notification will be POSTed. `RequestUUID` and `CallUUID` is added to the usual [call notification parameters](#/components/schemas/CallNotificationParameters)

        send_digits : typing.Optional[str]
            DTMF tones to be sent when the call is answered. Each occurrence of `w` implies a 0.5 seconds delay whereas `W` will apply a whole second delay. To alter the tone duration (by default, 2000ms), append `@` and the length in milliseconds at the end of the string

        send_on_preanswer : typing.Optional[bool]
            When set to `true`, DTMF tones will be sent as early media rather than when the call is answered

        time_limit : typing.Optional[int]
            Schedules the call's hangup at a given time offset (in seconds) after the call is answered

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkCallResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.call.v01bulk_call(
                answer_url="https://example.com/answer/",
                delimiter="<",
                from_="15551234567",
                gateways="user/,sofia/gateway/PSTNgateway1/,sofia/gateway/PSTNgateway2/",
                to="15557654321",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01bulk_call(
            answer_url=answer_url,
            delimiter=delimiter,
            from_=from_,
            gateways=gateways,
            to=to,
            caller_name=caller_name,
            confirm_key=confirm_key,
            confirm_sound=confirm_sound,
            core_uuid=core_uuid,
            extra_dial_string=extra_dial_string,
            gateway_codecs=gateway_codecs,
            gateway_retries=gateway_retries,
            gateway_timeouts=gateway_timeouts,
            hangup_on_ring=hangup_on_ring,
            hangup_url=hangup_url,
            reject_causes=reject_causes,
            ring_url=ring_url,
            send_digits=send_digits,
            send_on_preanswer=send_on_preanswer,
            time_limit=time_limit,
            request_options=request_options,
        )
        return _response.data

    async def v01call(
        self,
        *,
        answer_url: str,
        from_: str,
        gateways: str,
        to: str,
        async_amd: typing.Optional[bool] = OMIT,
        async_amd_status_callback: typing.Optional[str] = OMIT,
        async_amd_status_callback_method: typing.Optional[CallParametersAsyncAmdStatusCallbackMethod] = OMIT,
        caller_name: typing.Optional[str] = OMIT,
        core_uuid: typing.Optional[str] = OMIT,
        extra_dial_string: typing.Optional[str] = OMIT,
        gateway_codecs: typing.Optional[str] = OMIT,
        gateway_retries: typing.Optional[str] = OMIT,
        gateway_timeouts: typing.Optional[str] = OMIT,
        hangup_on_ring: typing.Optional[int] = OMIT,
        hangup_url: typing.Optional[str] = OMIT,
        machine_detection: typing.Optional[CallParametersMachineDetection] = OMIT,
        machine_detection_silence_timeout: typing.Optional[int] = OMIT,
        machine_detection_speech_end_threshold: typing.Optional[int] = OMIT,
        machine_detection_speech_threshold: typing.Optional[int] = OMIT,
        machine_detection_timeout: typing.Optional[int] = OMIT,
        ring_url: typing.Optional[str] = OMIT,
        send_digits: typing.Optional[str] = OMIT,
        send_on_preanswer: typing.Optional[bool] = OMIT,
        time_limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CallResponse:
        """
        Initiates an outbound call

        Parameters
        ----------
        answer_url : str
            Fully qualified URL which will provide the RestXML once the call connects

        from_ : str
            Phone number to be used as Caller ID

        gateways : str
            Comma separated FreeSWITCH gateway strings. When multiple gateways are specified, they will be tried sequentially (failover)

        to : str
            Phone number to be called

        async_amd : typing.Optional[bool]
            When set to `true`, the call flow execution is blocked until answering machine detection is complete (an Eqivo extension)

        async_amd_status_callback : typing.Optional[str]
            Fully qualified URL to which the answering machine detection result will be sent. `AnsweredBy` and `MachineDetectionDuration` are appended to the usual [call notification parameters](#/components/schemas/CallNotificationParameters) (an Eqivo extension)

        async_amd_status_callback_method : typing.Optional[CallParametersAsyncAmdStatusCallbackMethod]
            HTTP method to be used when answering machine detection is completed (an Eqivo extension)

        caller_name : typing.Optional[str]
            Caller Name to be set for the call

        core_uuid : typing.Optional[str]
            Core UUID of the desired FreeSWITCH instance (an Eqivo extension)

        extra_dial_string : typing.Optional[str]
            Additional [channel variables](https://freeswitch.org/confluence/display/FREESWITCH/Channel+Variables) to be added to the originate FreeSWITCH API call.

        gateway_codecs : typing.Optional[str]
            List of codec(s) to be used for each gateway. Enclose codec groups in single quotes

        gateway_retries : typing.Optional[str]
            List of maximum retry counts for each gateway

        gateway_timeouts : typing.Optional[str]
            List of maximum timeout amounts (in seconds) for each gateway

        hangup_on_ring : typing.Optional[int]
            Schedules the call's hangup at a given time offset (in seconds) after the destination starts ringing

        hangup_url : typing.Optional[str]
            Fully qualified URL to which the call hangup notification will be POSTed. `HangupCause` is added to the usual call [call notification parameters](#/components/schemas/CallNotificationParameters)

        machine_detection : typing.Optional[CallParametersMachineDetection]
            Enables answering machine detection; optionally, it waits until the greeting message has been played back (an Eqivo extension)

        machine_detection_silence_timeout : typing.Optional[int]
            Initial silence threshold (in milliseconds, an Eqivo extension)

        machine_detection_speech_end_threshold : typing.Optional[int]
            Silence threshold (in milliseconds, an Eqivo extension)

        machine_detection_speech_threshold : typing.Optional[int]
            Speech activity/utterance threshold (in milliseconds, an Eqivo extension)

        machine_detection_timeout : typing.Optional[int]
            Amount of time (in seconds) allotted for answering machine detection assessment (an Eqivo extension)

        ring_url : typing.Optional[str]
            Fully qualified URL to which the call ringing notification will be POSTed. `RequestUUID` and `CallUUID` is added to the usual [call notification parameters](#/components/schemas/CallNotificationParameters)

        send_digits : typing.Optional[str]
            DTMF tones to be sent when the call is answered. Each occurrence of `w` implies a 0.5 seconds delay whereas `W` will apply a whole second delay. To alter the tone duration (by default, 2000ms), append `@` and the length in milliseconds at the end of the string

        send_on_preanswer : typing.Optional[bool]
            When set to `true`, DTMF tones will be sent as early media rather than when the call is answered

        time_limit : typing.Optional[int]
            Schedules the call's hangup at a given time offset (in seconds) after the call is answered

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CallResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.call.v01call(
                answer_url="https://example.com/answer/",
                from_="15551234567",
                gateways="user/,sofia/gateway/PSTNgateway1/,sofia/gateway/PSTNgateway2/",
                to="15557654321",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01call(
            answer_url=answer_url,
            from_=from_,
            gateways=gateways,
            to=to,
            async_amd=async_amd,
            async_amd_status_callback=async_amd_status_callback,
            async_amd_status_callback_method=async_amd_status_callback_method,
            caller_name=caller_name,
            core_uuid=core_uuid,
            extra_dial_string=extra_dial_string,
            gateway_codecs=gateway_codecs,
            gateway_retries=gateway_retries,
            gateway_timeouts=gateway_timeouts,
            hangup_on_ring=hangup_on_ring,
            hangup_url=hangup_url,
            machine_detection=machine_detection,
            machine_detection_silence_timeout=machine_detection_silence_timeout,
            machine_detection_speech_end_threshold=machine_detection_speech_end_threshold,
            machine_detection_speech_threshold=machine_detection_speech_threshold,
            machine_detection_timeout=machine_detection_timeout,
            ring_url=ring_url,
            send_digits=send_digits,
            send_on_preanswer=send_on_preanswer,
            time_limit=time_limit,
            request_options=request_options,
        )
        return _response.data

    async def v01cancel_scheduled_hangup(
        self, *, sched_hangup_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CancelScheduledHangupResponse:
        """
        Cancels a scheduled hangup for a call

        Parameters
        ----------
        sched_hangup_id : str
            Unique identifier returned when scheduled hangup was originally requested

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancelScheduledHangupResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.call.v01cancel_scheduled_hangup(
                sched_hangup_id="ea428fbd-ac9b-498c-8bb2-a36ac49f10fd",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01cancel_scheduled_hangup(
            sched_hangup_id=sched_hangup_id, request_options=request_options
        )
        return _response.data

    async def v01cancel_scheduled_play(
        self, *, sched_play_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CancelScheduledPlayResponse:
        """
        Cancels a scheduled playback request

        Parameters
        ----------
        sched_play_id : str
            Unique identifier returned when scheduled playback was originally requested

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancelScheduledPlayResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.call.v01cancel_scheduled_play(
                sched_play_id="ea428fbd-ac9b-498c-8bb2-a36ac49f10fd",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01cancel_scheduled_play(
            sched_play_id=sched_play_id, request_options=request_options
        )
        return _response.data

    async def v01group_call(
        self,
        *,
        answer_url: str,
        delimiter: str,
        from_: str,
        gateways: str,
        to: str,
        caller_name: typing.Optional[str] = OMIT,
        confirm_key: typing.Optional[str] = OMIT,
        confirm_sound: typing.Optional[str] = OMIT,
        core_uuid: typing.Optional[str] = OMIT,
        extra_dial_string: typing.Optional[str] = OMIT,
        gateway_codecs: typing.Optional[str] = OMIT,
        gateway_retries: typing.Optional[str] = OMIT,
        gateway_timeouts: typing.Optional[str] = OMIT,
        hangup_on_ring: typing.Optional[int] = OMIT,
        hangup_url: typing.Optional[str] = OMIT,
        reject_causes: typing.Optional[str] = OMIT,
        ring_url: typing.Optional[str] = OMIT,
        send_digits: typing.Optional[str] = OMIT,
        send_on_preanswer: typing.Optional[bool] = OMIT,
        time_limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GroupCallResponse:
        """
        Initiate multiple racing outbound calls

        Parameters
        ----------
        answer_url : str
            Fully qualified URL which will provide the RestXML once the call connects

        delimiter : str
            Any character, except `/` and `,`, which will be used as a separator within several parameters

        from_ : str
            Phone number to be used as Caller ID

        gateways : str
            Comma separated FreeSWITCH gateway strings. When multiple gateways are specified, they will be tried sequentially (failover)

        to : str
            Phone number to be called

        caller_name : typing.Optional[str]
            Caller Name to be set for the call

        confirm_key : typing.Optional[str]
            DTMF tone the called party must send to accept the call

        confirm_sound : typing.Optional[str]
            Remote URL to fetch with POST HTTP request which must return a RestXML with Play, Wait and/or Speak Elements only (all others are ignored). This RESTXML is played to the called party when he answered

        core_uuid : typing.Optional[str]
            Core UUID of the desired FreeSWITCH instance (an Eqivo extension)

        extra_dial_string : typing.Optional[str]
            Additional [channel variables](https://freeswitch.org/confluence/display/FREESWITCH/Channel+Variables) to be added to the originate FreeSWITCH API call.

        gateway_codecs : typing.Optional[str]
            List of codec(s) to be used for each gateway. Enclose codec groups in single quotes

        gateway_retries : typing.Optional[str]
            List of maximum retry counts for each gateway

        gateway_timeouts : typing.Optional[str]
            List of maximum timeout amounts (in seconds) for each gateway

        hangup_on_ring : typing.Optional[int]
            Schedules the call's hangup at a given time offset (in seconds) after the destination starts ringing

        hangup_url : typing.Optional[str]
            Fully qualified URL to which the call hangup notification will be POSTed. `HangupCause` is added to the usual call [call notification parameters](#/components/schemas/CallNotificationParameters)

        reject_causes : typing.Optional[str]
            Comma separated reject causes

        ring_url : typing.Optional[str]
            Fully qualified URL to which the call ringing notification will be POSTed. `RequestUUID` and `CallUUID` is added to the usual [call notification parameters](#/components/schemas/CallNotificationParameters)

        send_digits : typing.Optional[str]
            DTMF tones to be sent when the call is answered. Each occurrence of `w` implies a 0.5 seconds delay whereas `W` will apply a whole second delay. To alter the tone duration (by default, 2000ms), append `@` and the length in milliseconds at the end of the string

        send_on_preanswer : typing.Optional[bool]
            When set to `true`, DTMF tones will be sent as early media rather than when the call is answered

        time_limit : typing.Optional[int]
            Schedules the call's hangup at a given time offset (in seconds) after the call is answered

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GroupCallResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.call.v01group_call(
                answer_url="https://example.com/answer/",
                delimiter="<",
                from_="15551234567",
                gateways="user/,sofia/gateway/PSTNgateway1/,sofia/gateway/PSTNgateway2/",
                to="15557654321",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01group_call(
            answer_url=answer_url,
            delimiter=delimiter,
            from_=from_,
            gateways=gateways,
            to=to,
            caller_name=caller_name,
            confirm_key=confirm_key,
            confirm_sound=confirm_sound,
            core_uuid=core_uuid,
            extra_dial_string=extra_dial_string,
            gateway_codecs=gateway_codecs,
            gateway_retries=gateway_retries,
            gateway_timeouts=gateway_timeouts,
            hangup_on_ring=hangup_on_ring,
            hangup_url=hangup_url,
            reject_causes=reject_causes,
            ring_url=ring_url,
            send_digits=send_digits,
            send_on_preanswer=send_on_preanswer,
            time_limit=time_limit,
            request_options=request_options,
        )
        return _response.data

    async def v01hangup_all_calls(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HangupAllCallsResponse:
        """
        Hangs up all established calls

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HangupAllCallsResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.call.v01hangup_all_calls()


        asyncio.run(main())
        """
        _response = await self._raw_client.v01hangup_all_calls(request_options=request_options)
        return _response.data

    async def v01hangup_call(
        self,
        *,
        call_uuid: typing.Optional[str] = OMIT,
        request_uuid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HangupCallResponse:
        """
        Hangs up a specific call

        Parameters
        ----------
        call_uuid : typing.Optional[str]
            Unique identifier of the call (when established); this parameter is mutually exclusive with RequestUUID

        request_uuid : typing.Optional[str]
            Unique identifier of the API request (when the call is not established yet); this parameter is mutually exclusive with CallUUID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HangupCallResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.call.v01hangup_call()


        asyncio.run(main())
        """
        _response = await self._raw_client.v01hangup_call(
            call_uuid=call_uuid, request_uuid=request_uuid, request_options=request_options
        )
        return _response.data

    async def v01play(
        self,
        *,
        call_uuid: str,
        sounds: str,
        legs: typing.Optional[PlayParametersLegs] = OMIT,
        length: typing.Optional[int] = OMIT,
        loop: typing.Optional[bool] = OMIT,
        mix: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PlayResponse:
        """
        Plays media into a live call

        Parameters
        ----------
        call_uuid : str
            Unique identifier of the call to play media into

        sounds : str
            Comma separated list of file paths/URIs to be played

        legs : typing.Optional[PlayParametersLegs]
            Call leg(s) for which the media will be played; `aleg` refers to the initial call leg, `bleg` refers to the bridged call leg, if applicable.

        length : typing.Optional[int]
            Maximum amount of time (in seconds) to playback the media

        loop : typing.Optional[bool]
            Loops the media file(s) indefinitely

        mix : typing.Optional[bool]
            Whether the media should be mixed with the call's audio stream

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlayResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.call.v01play(
                call_uuid="e69b32da-3243-4ba6-a965-5d2f64a57d48",
                sounds="/tmp/prompt.wav",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01play(
            call_uuid=call_uuid,
            sounds=sounds,
            legs=legs,
            length=length,
            loop=loop,
            mix=mix,
            request_options=request_options,
        )
        return _response.data

    async def v01play_stop(
        self, *, call_uuid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PlayStopResponse:
        """
        Interrupts media playback on a given call

        Parameters
        ----------
        call_uuid : str
            Unique identifier of the call

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PlayStopResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.call.v01play_stop(
                call_uuid="441afb63-85bc-49d4-9ac8-8459f9bf5e6b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01play_stop(call_uuid=call_uuid, request_options=request_options)
        return _response.data

    async def v01record_start(
        self,
        *,
        call_uuid: typing.Optional[str] = OMIT,
        file_format: typing.Optional[RecordStartParametersFileFormat] = OMIT,
        file_name: typing.Optional[str] = OMIT,
        file_path: typing.Optional[str] = OMIT,
        time_limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RecordStartResponse:
        """
        Initiates recording of a given call

        Parameters
        ----------
        call_uuid : typing.Optional[str]
            Unique identifier of the call to be recorded

        file_format : typing.Optional[RecordStartParametersFileFormat]
            File format (extension)

        file_name : typing.Optional[str]
            Recording file name (without extension); if empty, a timestamp based file name will be generated

        file_path : typing.Optional[str]
            Directory path/URI where the recording file will be saved

        time_limit : typing.Optional[int]
            Maximum recording length, in seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordStartResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.call.v01record_start()


        asyncio.run(main())
        """
        _response = await self._raw_client.v01record_start(
            call_uuid=call_uuid,
            file_format=file_format,
            file_name=file_name,
            file_path=file_path,
            time_limit=time_limit,
            request_options=request_options,
        )
        return _response.data

    async def v01record_stop(
        self, *, call_uuid: str, record_file: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RecordStopResponse:
        """
        Stops the recording of a given call

        Parameters
        ----------
        call_uuid : str
            Unique identifier of the call

        record_file : str
            Full path to recording file, as returned by RecordStart; `all` shorthand is also available

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordStopResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.call.v01record_stop(
                call_uuid="eacfa857-4001-4379-b79a-c7ef6d963bcb",
                record_file="/tmp/recording/sample.wav",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01record_stop(
            call_uuid=call_uuid, record_file=record_file, request_options=request_options
        )
        return _response.data

    async def v01schedule_hangup(
        self, *, call_uuid: str, time: int, request_options: typing.Optional[RequestOptions] = None
    ) -> ScheduleHangupResponse:
        """
        Schedules a hangup for a specific call

        Parameters
        ----------
        call_uuid : str
            Unique identifier of the call

        time : int
            Time (in seconds) after which the call in question will be hung up

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduleHangupResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.call.v01schedule_hangup(
                call_uuid="f84fbadc-5df0-4c02-934b-aac0c1efb8ae",
                time=59,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01schedule_hangup(
            call_uuid=call_uuid, time=time, request_options=request_options
        )
        return _response.data

    async def v01schedule_play(
        self,
        *,
        call_uuid: str,
        sounds: str,
        time: int,
        legs: typing.Optional[SchedulePlayParametersLegs] = OMIT,
        length: typing.Optional[int] = OMIT,
        loop: typing.Optional[bool] = OMIT,
        mix: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchedulePlayResponse:
        """
        Schedules media playback for a specific call

        Parameters
        ----------
        call_uuid : str
            Unique identifier of the call to play media into

        sounds : str
            Comma separated list of file paths/URIs to be played

        time : int
            Time (in seconds) after which the media will be playedback

        legs : typing.Optional[SchedulePlayParametersLegs]
            Call leg(s) for which the media will be played; `aleg` refers to the initial call leg, `bleg` refers to the bridged call leg, if applicable.

        length : typing.Optional[int]
            Maximum amount of time (in seconds) to playback the media

        loop : typing.Optional[bool]
            Loops the media file(s) indefinitely

        mix : typing.Optional[bool]
            Whether the media should be mixed with the call's audio stream

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchedulePlayResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.call.v01schedule_play(
                call_uuid="e69b32da-3243-4ba6-a965-5d2f64a57d48",
                sounds="/tmp/prompt.wav",
                time=29,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01schedule_play(
            call_uuid=call_uuid,
            sounds=sounds,
            time=time,
            legs=legs,
            length=length,
            loop=loop,
            mix=mix,
            request_options=request_options,
        )
        return _response.data

    async def v01send_digits(
        self,
        *,
        call_uuid: str,
        digits: str,
        leg: typing.Optional[SendDigitsParametersLeg] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendDigitsResponse:
        """
        Emits DMTF tones to a call

        Parameters
        ----------
        call_uuid : str
            Unique identifier of the call to send DTMF to

        digits : str
            DTMF tones to be sent; each occurrence of `w` implies a 0.5 seconds delay whereas `W` will apply a whole second delay. To alter the tone duration (by default, 2000ms), append `@` and the length in milliseconds at the end of the string

        leg : typing.Optional[SendDigitsParametersLeg]
            Call leg(s) to which DTMFs will be sent; `aleg` refers to the initial call leg, `bleg` refers to the bridged call leg, if applicable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendDigitsResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.call.v01send_digits(
                call_uuid="d4cd08fe-4245-490a-ae39-5b58c6addbe8",
                digits="1w2w3W#*@1500",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01send_digits(
            call_uuid=call_uuid, digits=digits, leg=leg, request_options=request_options
        )
        return _response.data

    async def v01sound_touch(
        self,
        *,
        call_uuid: str,
        audio_direction: typing.Optional[SoundTouchParametersAudioDirection] = OMIT,
        pitch: typing.Optional[float] = OMIT,
        pitch_octaves: typing.Optional[float] = OMIT,
        pitch_semi_tones: typing.Optional[float] = OMIT,
        rate: typing.Optional[float] = OMIT,
        tempo: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoundTouchResponse:
        """
        Applies SoundTouch effects to a live call

        Parameters
        ----------
        call_uuid : str
            Unique identifier of the call to send DTMF to

        audio_direction : typing.Optional[SoundTouchParametersAudioDirection]
            Media stream to be altered, incoming or outgoing

        pitch : typing.Optional[float]
            Adjust the pitch

        pitch_octaves : typing.Optional[float]
            Adjust the pitch in octaves

        pitch_semi_tones : typing.Optional[float]
            Adjust the pitch in semitones

        rate : typing.Optional[float]
            Adjust the rate

        tempo : typing.Optional[float]
            Adjust the tempo

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SoundTouchResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.call.v01sound_touch(
                call_uuid="b7054b68-0620-455a-8ac7-f8f126853b9d",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01sound_touch(
            call_uuid=call_uuid,
            audio_direction=audio_direction,
            pitch=pitch,
            pitch_octaves=pitch_octaves,
            pitch_semi_tones=pitch_semi_tones,
            rate=rate,
            tempo=tempo,
            request_options=request_options,
        )
        return _response.data

    async def v01sound_touch_stop(
        self, *, call_uuid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SoundTouchStopResponse:
        """
        Removes SoundTouch effects from a given call

        Parameters
        ----------
        call_uuid : str
            Unique identifier of the call

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SoundTouchStopResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.call.v01sound_touch_stop(
                call_uuid="fe372011-face-4bc2-bbcc-893d045bf67d",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01sound_touch_stop(call_uuid=call_uuid, request_options=request_options)
        return _response.data

    async def v01transfer_call(
        self, *, call_uuid: str, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> TransferCallResponse:
        """
        Replaces the RestXML flow of a live call

        Parameters
        ----------
        call_uuid : str
            Unique identifier of the call

        url : str
            Absolute URL which will return the updated RestXML flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TransferCallResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.call.v01transfer_call(
                call_uuid="03694cf6-62b3-4f00-b0fc-6831ddcc2693",
                url="https://example.org/restxml/endpoint/",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01transfer_call(
            call_uuid=call_uuid, url=url, request_options=request_options
        )
        return _response.data
