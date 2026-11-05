

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCallClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[BulkCallResponse]:
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
        HttpResponse[BulkCallResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/BulkCall/",
            method="POST",
            data={
                "AnswerUrl": answer_url,
                "CallerName": caller_name,
                "ConfirmKey": confirm_key,
                "ConfirmSound": confirm_sound,
                "CoreUUID": core_uuid,
                "Delimiter": delimiter,
                "ExtraDialString": extra_dial_string,
                "From": from_,
                "GatewayCodecs": gateway_codecs,
                "GatewayRetries": gateway_retries,
                "GatewayTimeouts": gateway_timeouts,
                "Gateways": gateways,
                "HangupOnRing": hangup_on_ring,
                "HangupUrl": hangup_url,
                "RejectCauses": reject_causes,
                "RingUrl": ring_url,
                "SendDigits": send_digits,
                "SendOnPreanswer": send_on_preanswer,
                "TimeLimit": time_limit,
                "To": to,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkCallResponse,
                    parse_obj_as(
                        type_=BulkCallResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[CallResponse]:
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
        HttpResponse[CallResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/Call/",
            method="POST",
            data={
                "AnswerUrl": answer_url,
                "AsyncAMD": async_amd,
                "AsyncAmdStatusCallback": async_amd_status_callback,
                "AsyncAmdStatusCallbackMethod": async_amd_status_callback_method,
                "CallerName": caller_name,
                "CoreUUID": core_uuid,
                "ExtraDialString": extra_dial_string,
                "From": from_,
                "GatewayCodecs": gateway_codecs,
                "GatewayRetries": gateway_retries,
                "GatewayTimeouts": gateway_timeouts,
                "Gateways": gateways,
                "HangupOnRing": hangup_on_ring,
                "HangupUrl": hangup_url,
                "MachineDetection": machine_detection,
                "MachineDetectionSilenceTimeout": machine_detection_silence_timeout,
                "MachineDetectionSpeechEndThreshold": machine_detection_speech_end_threshold,
                "MachineDetectionSpeechThreshold": machine_detection_speech_threshold,
                "MachineDetectionTimeout": machine_detection_timeout,
                "RingUrl": ring_url,
                "SendDigits": send_digits,
                "SendOnPreanswer": send_on_preanswer,
                "TimeLimit": time_limit,
                "To": to,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CallResponse,
                    parse_obj_as(
                        type_=CallResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def v01cancel_scheduled_hangup(
        self, *, sched_hangup_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CancelScheduledHangupResponse]:
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
        HttpResponse[CancelScheduledHangupResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/CancelScheduledHangup/",
            method="POST",
            data={
                "SchedHangupId": sched_hangup_id,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CancelScheduledHangupResponse,
                    parse_obj_as(
                        type_=CancelScheduledHangupResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def v01cancel_scheduled_play(
        self, *, sched_play_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CancelScheduledPlayResponse]:
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
        HttpResponse[CancelScheduledPlayResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/CancelScheduledPlay/",
            method="POST",
            data={
                "SchedPlayId": sched_play_id,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CancelScheduledPlayResponse,
                    parse_obj_as(
                        type_=CancelScheduledPlayResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[GroupCallResponse]:
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
        HttpResponse[GroupCallResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/GroupCall/",
            method="POST",
            data={
                "AnswerUrl": answer_url,
                "CallerName": caller_name,
                "ConfirmKey": confirm_key,
                "ConfirmSound": confirm_sound,
                "CoreUUID": core_uuid,
                "Delimiter": delimiter,
                "ExtraDialString": extra_dial_string,
                "From": from_,
                "GatewayCodecs": gateway_codecs,
                "GatewayRetries": gateway_retries,
                "GatewayTimeouts": gateway_timeouts,
                "Gateways": gateways,
                "HangupOnRing": hangup_on_ring,
                "HangupUrl": hangup_url,
                "RejectCauses": reject_causes,
                "RingUrl": ring_url,
                "SendDigits": send_digits,
                "SendOnPreanswer": send_on_preanswer,
                "TimeLimit": time_limit,
                "To": to,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupCallResponse,
                    parse_obj_as(
                        type_=GroupCallResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def v01hangup_all_calls(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[HangupAllCallsResponse]:
        """
        Hangs up all established calls

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[HangupAllCallsResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/HangupAllCalls/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HangupAllCallsResponse,
                    parse_obj_as(
                        type_=HangupAllCallsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def v01hangup_call(
        self,
        *,
        call_uuid: typing.Optional[str] = OMIT,
        request_uuid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[HangupCallResponse]:
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
        HttpResponse[HangupCallResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/HangupCall/",
            method="POST",
            data={
                "CallUUID": call_uuid,
                "RequestUUID": request_uuid,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HangupCallResponse,
                    parse_obj_as(
                        type_=HangupCallResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[PlayResponse]:
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
        HttpResponse[PlayResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/Play/",
            method="POST",
            data={
                "CallUUID": call_uuid,
                "Legs": legs,
                "Length": length,
                "Loop": loop,
                "Mix": mix,
                "Sounds": sounds,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PlayResponse,
                    parse_obj_as(
                        type_=PlayResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def v01play_stop(
        self, *, call_uuid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PlayStopResponse]:
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
        HttpResponse[PlayStopResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/PlayStop/",
            method="POST",
            data={
                "CallUUID": call_uuid,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PlayStopResponse,
                    parse_obj_as(
                        type_=PlayStopResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def v01record_start(
        self,
        *,
        call_uuid: typing.Optional[str] = OMIT,
        file_format: typing.Optional[RecordStartParametersFileFormat] = OMIT,
        file_name: typing.Optional[str] = OMIT,
        file_path: typing.Optional[str] = OMIT,
        time_limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RecordStartResponse]:
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
        HttpResponse[RecordStartResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/RecordStart/",
            method="POST",
            data={
                "CallUUID": call_uuid,
                "FileFormat": file_format,
                "FileName": file_name,
                "FilePath": file_path,
                "TimeLimit": time_limit,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordStartResponse,
                    parse_obj_as(
                        type_=RecordStartResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def v01record_stop(
        self, *, call_uuid: str, record_file: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RecordStopResponse]:
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
        HttpResponse[RecordStopResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/RecordStop/",
            method="POST",
            data={
                "CallUUID": call_uuid,
                "RecordFile": record_file,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordStopResponse,
                    parse_obj_as(
                        type_=RecordStopResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def v01schedule_hangup(
        self, *, call_uuid: str, time: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ScheduleHangupResponse]:
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
        HttpResponse[ScheduleHangupResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/ScheduleHangup/",
            method="POST",
            data={
                "CallUUID": call_uuid,
                "Time": time,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScheduleHangupResponse,
                    parse_obj_as(
                        type_=ScheduleHangupResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[SchedulePlayResponse]:
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
        HttpResponse[SchedulePlayResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/SchedulePlay/",
            method="POST",
            data={
                "CallUUID": call_uuid,
                "Legs": legs,
                "Length": length,
                "Loop": loop,
                "Mix": mix,
                "Sounds": sounds,
                "Time": time,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SchedulePlayResponse,
                    parse_obj_as(
                        type_=SchedulePlayResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def v01send_digits(
        self,
        *,
        call_uuid: str,
        digits: str,
        leg: typing.Optional[SendDigitsParametersLeg] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SendDigitsResponse]:
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
        HttpResponse[SendDigitsResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/SendDigits/",
            method="POST",
            data={
                "CallUUID": call_uuid,
                "Digits": digits,
                "Leg": leg,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SendDigitsResponse,
                    parse_obj_as(
                        type_=SendDigitsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[SoundTouchResponse]:
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
        HttpResponse[SoundTouchResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/SoundTouch/",
            method="POST",
            data={
                "AudioDirection": audio_direction,
                "CallUUID": call_uuid,
                "Pitch": pitch,
                "PitchOctaves": pitch_octaves,
                "PitchSemiTones": pitch_semi_tones,
                "Rate": rate,
                "Tempo": tempo,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SoundTouchResponse,
                    parse_obj_as(
                        type_=SoundTouchResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def v01sound_touch_stop(
        self, *, call_uuid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SoundTouchStopResponse]:
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
        HttpResponse[SoundTouchStopResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/SoundTouchStop/",
            method="POST",
            data={
                "CallUUID": call_uuid,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SoundTouchStopResponse,
                    parse_obj_as(
                        type_=SoundTouchStopResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def v01transfer_call(
        self, *, call_uuid: str, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TransferCallResponse]:
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
        HttpResponse[TransferCallResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/TransferCall/",
            method="POST",
            data={
                "CallUUID": call_uuid,
                "Url": url,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TransferCallResponse,
                    parse_obj_as(
                        type_=TransferCallResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCallClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[BulkCallResponse]:
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
        AsyncHttpResponse[BulkCallResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/BulkCall/",
            method="POST",
            data={
                "AnswerUrl": answer_url,
                "CallerName": caller_name,
                "ConfirmKey": confirm_key,
                "ConfirmSound": confirm_sound,
                "CoreUUID": core_uuid,
                "Delimiter": delimiter,
                "ExtraDialString": extra_dial_string,
                "From": from_,
                "GatewayCodecs": gateway_codecs,
                "GatewayRetries": gateway_retries,
                "GatewayTimeouts": gateway_timeouts,
                "Gateways": gateways,
                "HangupOnRing": hangup_on_ring,
                "HangupUrl": hangup_url,
                "RejectCauses": reject_causes,
                "RingUrl": ring_url,
                "SendDigits": send_digits,
                "SendOnPreanswer": send_on_preanswer,
                "TimeLimit": time_limit,
                "To": to,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkCallResponse,
                    parse_obj_as(
                        type_=BulkCallResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[CallResponse]:
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
        AsyncHttpResponse[CallResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/Call/",
            method="POST",
            data={
                "AnswerUrl": answer_url,
                "AsyncAMD": async_amd,
                "AsyncAmdStatusCallback": async_amd_status_callback,
                "AsyncAmdStatusCallbackMethod": async_amd_status_callback_method,
                "CallerName": caller_name,
                "CoreUUID": core_uuid,
                "ExtraDialString": extra_dial_string,
                "From": from_,
                "GatewayCodecs": gateway_codecs,
                "GatewayRetries": gateway_retries,
                "GatewayTimeouts": gateway_timeouts,
                "Gateways": gateways,
                "HangupOnRing": hangup_on_ring,
                "HangupUrl": hangup_url,
                "MachineDetection": machine_detection,
                "MachineDetectionSilenceTimeout": machine_detection_silence_timeout,
                "MachineDetectionSpeechEndThreshold": machine_detection_speech_end_threshold,
                "MachineDetectionSpeechThreshold": machine_detection_speech_threshold,
                "MachineDetectionTimeout": machine_detection_timeout,
                "RingUrl": ring_url,
                "SendDigits": send_digits,
                "SendOnPreanswer": send_on_preanswer,
                "TimeLimit": time_limit,
                "To": to,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CallResponse,
                    parse_obj_as(
                        type_=CallResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def v01cancel_scheduled_hangup(
        self, *, sched_hangup_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CancelScheduledHangupResponse]:
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
        AsyncHttpResponse[CancelScheduledHangupResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/CancelScheduledHangup/",
            method="POST",
            data={
                "SchedHangupId": sched_hangup_id,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CancelScheduledHangupResponse,
                    parse_obj_as(
                        type_=CancelScheduledHangupResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def v01cancel_scheduled_play(
        self, *, sched_play_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CancelScheduledPlayResponse]:
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
        AsyncHttpResponse[CancelScheduledPlayResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/CancelScheduledPlay/",
            method="POST",
            data={
                "SchedPlayId": sched_play_id,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CancelScheduledPlayResponse,
                    parse_obj_as(
                        type_=CancelScheduledPlayResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[GroupCallResponse]:
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
        AsyncHttpResponse[GroupCallResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/GroupCall/",
            method="POST",
            data={
                "AnswerUrl": answer_url,
                "CallerName": caller_name,
                "ConfirmKey": confirm_key,
                "ConfirmSound": confirm_sound,
                "CoreUUID": core_uuid,
                "Delimiter": delimiter,
                "ExtraDialString": extra_dial_string,
                "From": from_,
                "GatewayCodecs": gateway_codecs,
                "GatewayRetries": gateway_retries,
                "GatewayTimeouts": gateway_timeouts,
                "Gateways": gateways,
                "HangupOnRing": hangup_on_ring,
                "HangupUrl": hangup_url,
                "RejectCauses": reject_causes,
                "RingUrl": ring_url,
                "SendDigits": send_digits,
                "SendOnPreanswer": send_on_preanswer,
                "TimeLimit": time_limit,
                "To": to,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GroupCallResponse,
                    parse_obj_as(
                        type_=GroupCallResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def v01hangup_all_calls(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[HangupAllCallsResponse]:
        """
        Hangs up all established calls

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[HangupAllCallsResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/HangupAllCalls/",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HangupAllCallsResponse,
                    parse_obj_as(
                        type_=HangupAllCallsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def v01hangup_call(
        self,
        *,
        call_uuid: typing.Optional[str] = OMIT,
        request_uuid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[HangupCallResponse]:
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
        AsyncHttpResponse[HangupCallResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/HangupCall/",
            method="POST",
            data={
                "CallUUID": call_uuid,
                "RequestUUID": request_uuid,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    HangupCallResponse,
                    parse_obj_as(
                        type_=HangupCallResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[PlayResponse]:
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
        AsyncHttpResponse[PlayResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/Play/",
            method="POST",
            data={
                "CallUUID": call_uuid,
                "Legs": legs,
                "Length": length,
                "Loop": loop,
                "Mix": mix,
                "Sounds": sounds,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PlayResponse,
                    parse_obj_as(
                        type_=PlayResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def v01play_stop(
        self, *, call_uuid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PlayStopResponse]:
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
        AsyncHttpResponse[PlayStopResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/PlayStop/",
            method="POST",
            data={
                "CallUUID": call_uuid,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PlayStopResponse,
                    parse_obj_as(
                        type_=PlayStopResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def v01record_start(
        self,
        *,
        call_uuid: typing.Optional[str] = OMIT,
        file_format: typing.Optional[RecordStartParametersFileFormat] = OMIT,
        file_name: typing.Optional[str] = OMIT,
        file_path: typing.Optional[str] = OMIT,
        time_limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RecordStartResponse]:
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
        AsyncHttpResponse[RecordStartResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/RecordStart/",
            method="POST",
            data={
                "CallUUID": call_uuid,
                "FileFormat": file_format,
                "FileName": file_name,
                "FilePath": file_path,
                "TimeLimit": time_limit,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordStartResponse,
                    parse_obj_as(
                        type_=RecordStartResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def v01record_stop(
        self, *, call_uuid: str, record_file: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RecordStopResponse]:
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
        AsyncHttpResponse[RecordStopResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/RecordStop/",
            method="POST",
            data={
                "CallUUID": call_uuid,
                "RecordFile": record_file,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RecordStopResponse,
                    parse_obj_as(
                        type_=RecordStopResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def v01schedule_hangup(
        self, *, call_uuid: str, time: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ScheduleHangupResponse]:
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
        AsyncHttpResponse[ScheduleHangupResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/ScheduleHangup/",
            method="POST",
            data={
                "CallUUID": call_uuid,
                "Time": time,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScheduleHangupResponse,
                    parse_obj_as(
                        type_=ScheduleHangupResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[SchedulePlayResponse]:
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
        AsyncHttpResponse[SchedulePlayResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/SchedulePlay/",
            method="POST",
            data={
                "CallUUID": call_uuid,
                "Legs": legs,
                "Length": length,
                "Loop": loop,
                "Mix": mix,
                "Sounds": sounds,
                "Time": time,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SchedulePlayResponse,
                    parse_obj_as(
                        type_=SchedulePlayResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def v01send_digits(
        self,
        *,
        call_uuid: str,
        digits: str,
        leg: typing.Optional[SendDigitsParametersLeg] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SendDigitsResponse]:
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
        AsyncHttpResponse[SendDigitsResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/SendDigits/",
            method="POST",
            data={
                "CallUUID": call_uuid,
                "Digits": digits,
                "Leg": leg,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SendDigitsResponse,
                    parse_obj_as(
                        type_=SendDigitsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[SoundTouchResponse]:
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
        AsyncHttpResponse[SoundTouchResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/SoundTouch/",
            method="POST",
            data={
                "AudioDirection": audio_direction,
                "CallUUID": call_uuid,
                "Pitch": pitch,
                "PitchOctaves": pitch_octaves,
                "PitchSemiTones": pitch_semi_tones,
                "Rate": rate,
                "Tempo": tempo,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SoundTouchResponse,
                    parse_obj_as(
                        type_=SoundTouchResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def v01sound_touch_stop(
        self, *, call_uuid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SoundTouchStopResponse]:
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
        AsyncHttpResponse[SoundTouchStopResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/SoundTouchStop/",
            method="POST",
            data={
                "CallUUID": call_uuid,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SoundTouchStopResponse,
                    parse_obj_as(
                        type_=SoundTouchStopResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def v01transfer_call(
        self, *, call_uuid: str, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TransferCallResponse]:
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
        AsyncHttpResponse[TransferCallResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/TransferCall/",
            method="POST",
            data={
                "CallUUID": call_uuid,
                "Url": url,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TransferCallResponse,
                    parse_obj_as(
                        type_=TransferCallResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
