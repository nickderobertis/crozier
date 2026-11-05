



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bulk_call_parameters import BulkCallParameters
    from .bulk_call_response import BulkCallResponse
    from .bulk_call_response_message import BulkCallResponseMessage
    from .call_notification_parameters import CallNotificationParameters
    from .call_notification_parameters_answered_by import CallNotificationParametersAnsweredBy
    from .call_notification_parameters_call_status import CallNotificationParametersCallStatus
    from .call_notification_parameters_direction import CallNotificationParametersDirection
    from .call_parameters import CallParameters
    from .call_parameters_async_amd_status_callback_method import CallParametersAsyncAmdStatusCallbackMethod
    from .call_parameters_machine_detection import CallParametersMachineDetection
    from .call_response import CallResponse
    from .call_response_message import CallResponseMessage
    from .cancel_scheduled_hangup_parameters import CancelScheduledHangupParameters
    from .cancel_scheduled_hangup_response import CancelScheduledHangupResponse
    from .cancel_scheduled_hangup_response_message import CancelScheduledHangupResponseMessage
    from .cancel_scheduled_play_parameters import CancelScheduledPlayParameters
    from .cancel_scheduled_play_response import CancelScheduledPlayResponse
    from .cancel_scheduled_play_response_message import CancelScheduledPlayResponseMessage
    from .conference_deaf_parameters import ConferenceDeafParameters
    from .conference_deaf_response import ConferenceDeafResponse
    from .conference_deaf_response_message import ConferenceDeafResponseMessage
    from .conference_hangup_parameters import ConferenceHangupParameters
    from .conference_hangup_response import ConferenceHangupResponse
    from .conference_hangup_response_message import ConferenceHangupResponseMessage
    from .conference_kick_parameters import ConferenceKickParameters
    from .conference_kick_response import ConferenceKickResponse
    from .conference_kick_response_message import ConferenceKickResponseMessage
    from .conference_list_members_parameters import ConferenceListMembersParameters
    from .conference_list_members_response import ConferenceListMembersResponse
    from .conference_list_members_response_message import ConferenceListMembersResponseMessage
    from .conference_list_parameters import ConferenceListParameters
    from .conference_list_response import ConferenceListResponse
    from .conference_list_response_message import ConferenceListResponseMessage
    from .conference_mute_parameters import ConferenceMuteParameters
    from .conference_mute_response import ConferenceMuteResponse
    from .conference_mute_response_message import ConferenceMuteResponseMessage
    from .conference_play_parameters import ConferencePlayParameters
    from .conference_play_response import ConferencePlayResponse
    from .conference_play_response_message import ConferencePlayResponseMessage
    from .conference_record_start_parameters import ConferenceRecordStartParameters
    from .conference_record_start_parameters_file_format import ConferenceRecordStartParametersFileFormat
    from .conference_record_start_response import ConferenceRecordStartResponse
    from .conference_record_start_response_message import ConferenceRecordStartResponseMessage
    from .conference_record_stop_parameters import ConferenceRecordStopParameters
    from .conference_record_stop_response import ConferenceRecordStopResponse
    from .conference_record_stop_response_message import ConferenceRecordStopResponseMessage
    from .conference_speak_parameters import ConferenceSpeakParameters
    from .conference_speak_response import ConferenceSpeakResponse
    from .conference_speak_response_message import ConferenceSpeakResponseMessage
    from .conference_undeaf_parameters import ConferenceUndeafParameters
    from .conference_undeaf_response import ConferenceUndeafResponse
    from .conference_undeaf_response_message import ConferenceUndeafResponseMessage
    from .conference_unmute_parameters import ConferenceUnmuteParameters
    from .conference_unmute_response import ConferenceUnmuteResponse
    from .conference_unmute_response_message import ConferenceUnmuteResponseMessage
    from .group_call_parameters import GroupCallParameters
    from .group_call_response import GroupCallResponse
    from .group_call_response_message import GroupCallResponseMessage
    from .hangup_all_calls_parameters import HangupAllCallsParameters
    from .hangup_all_calls_response import HangupAllCallsResponse
    from .hangup_all_calls_response_message import HangupAllCallsResponseMessage
    from .hangup_call_parameters import HangupCallParameters
    from .hangup_call_response import HangupCallResponse
    from .hangup_call_response_message import HangupCallResponseMessage
    from .play_parameters import PlayParameters
    from .play_parameters_legs import PlayParametersLegs
    from .play_response import PlayResponse
    from .play_response_message import PlayResponseMessage
    from .play_stop_parameters import PlayStopParameters
    from .play_stop_response import PlayStopResponse
    from .play_stop_response_message import PlayStopResponseMessage
    from .record_start_parameters import RecordStartParameters
    from .record_start_parameters_file_format import RecordStartParametersFileFormat
    from .record_start_response import RecordStartResponse
    from .record_start_response_message import RecordStartResponseMessage
    from .record_stop_parameters import RecordStopParameters
    from .record_stop_response import RecordStopResponse
    from .record_stop_response_message import RecordStopResponseMessage
    from .schedule_hangup_parameters import ScheduleHangupParameters
    from .schedule_hangup_response import ScheduleHangupResponse
    from .schedule_hangup_response_message import ScheduleHangupResponseMessage
    from .schedule_play_parameters import SchedulePlayParameters
    from .schedule_play_parameters_legs import SchedulePlayParametersLegs
    from .schedule_play_response import SchedulePlayResponse
    from .schedule_play_response_message import SchedulePlayResponseMessage
    from .send_digits_parameters import SendDigitsParameters
    from .send_digits_parameters_leg import SendDigitsParametersLeg
    from .send_digits_response import SendDigitsResponse
    from .send_digits_response_message import SendDigitsResponseMessage
    from .sound_touch_parameters import SoundTouchParameters
    from .sound_touch_parameters_audio_direction import SoundTouchParametersAudioDirection
    from .sound_touch_response import SoundTouchResponse
    from .sound_touch_response_message import SoundTouchResponseMessage
    from .sound_touch_stop_parameters import SoundTouchStopParameters
    from .sound_touch_stop_response import SoundTouchStopResponse
    from .sound_touch_stop_response_message import SoundTouchStopResponseMessage
    from .transfer_call_parameters import TransferCallParameters
    from .transfer_call_response import TransferCallResponse
    from .transfer_call_response_message import TransferCallResponseMessage
_dynamic_imports: typing.Dict[str, str] = {
    "BulkCallParameters": ".bulk_call_parameters",
    "BulkCallResponse": ".bulk_call_response",
    "BulkCallResponseMessage": ".bulk_call_response_message",
    "CallNotificationParameters": ".call_notification_parameters",
    "CallNotificationParametersAnsweredBy": ".call_notification_parameters_answered_by",
    "CallNotificationParametersCallStatus": ".call_notification_parameters_call_status",
    "CallNotificationParametersDirection": ".call_notification_parameters_direction",
    "CallParameters": ".call_parameters",
    "CallParametersAsyncAmdStatusCallbackMethod": ".call_parameters_async_amd_status_callback_method",
    "CallParametersMachineDetection": ".call_parameters_machine_detection",
    "CallResponse": ".call_response",
    "CallResponseMessage": ".call_response_message",
    "CancelScheduledHangupParameters": ".cancel_scheduled_hangup_parameters",
    "CancelScheduledHangupResponse": ".cancel_scheduled_hangup_response",
    "CancelScheduledHangupResponseMessage": ".cancel_scheduled_hangup_response_message",
    "CancelScheduledPlayParameters": ".cancel_scheduled_play_parameters",
    "CancelScheduledPlayResponse": ".cancel_scheduled_play_response",
    "CancelScheduledPlayResponseMessage": ".cancel_scheduled_play_response_message",
    "ConferenceDeafParameters": ".conference_deaf_parameters",
    "ConferenceDeafResponse": ".conference_deaf_response",
    "ConferenceDeafResponseMessage": ".conference_deaf_response_message",
    "ConferenceHangupParameters": ".conference_hangup_parameters",
    "ConferenceHangupResponse": ".conference_hangup_response",
    "ConferenceHangupResponseMessage": ".conference_hangup_response_message",
    "ConferenceKickParameters": ".conference_kick_parameters",
    "ConferenceKickResponse": ".conference_kick_response",
    "ConferenceKickResponseMessage": ".conference_kick_response_message",
    "ConferenceListMembersParameters": ".conference_list_members_parameters",
    "ConferenceListMembersResponse": ".conference_list_members_response",
    "ConferenceListMembersResponseMessage": ".conference_list_members_response_message",
    "ConferenceListParameters": ".conference_list_parameters",
    "ConferenceListResponse": ".conference_list_response",
    "ConferenceListResponseMessage": ".conference_list_response_message",
    "ConferenceMuteParameters": ".conference_mute_parameters",
    "ConferenceMuteResponse": ".conference_mute_response",
    "ConferenceMuteResponseMessage": ".conference_mute_response_message",
    "ConferencePlayParameters": ".conference_play_parameters",
    "ConferencePlayResponse": ".conference_play_response",
    "ConferencePlayResponseMessage": ".conference_play_response_message",
    "ConferenceRecordStartParameters": ".conference_record_start_parameters",
    "ConferenceRecordStartParametersFileFormat": ".conference_record_start_parameters_file_format",
    "ConferenceRecordStartResponse": ".conference_record_start_response",
    "ConferenceRecordStartResponseMessage": ".conference_record_start_response_message",
    "ConferenceRecordStopParameters": ".conference_record_stop_parameters",
    "ConferenceRecordStopResponse": ".conference_record_stop_response",
    "ConferenceRecordStopResponseMessage": ".conference_record_stop_response_message",
    "ConferenceSpeakParameters": ".conference_speak_parameters",
    "ConferenceSpeakResponse": ".conference_speak_response",
    "ConferenceSpeakResponseMessage": ".conference_speak_response_message",
    "ConferenceUndeafParameters": ".conference_undeaf_parameters",
    "ConferenceUndeafResponse": ".conference_undeaf_response",
    "ConferenceUndeafResponseMessage": ".conference_undeaf_response_message",
    "ConferenceUnmuteParameters": ".conference_unmute_parameters",
    "ConferenceUnmuteResponse": ".conference_unmute_response",
    "ConferenceUnmuteResponseMessage": ".conference_unmute_response_message",
    "GroupCallParameters": ".group_call_parameters",
    "GroupCallResponse": ".group_call_response",
    "GroupCallResponseMessage": ".group_call_response_message",
    "HangupAllCallsParameters": ".hangup_all_calls_parameters",
    "HangupAllCallsResponse": ".hangup_all_calls_response",
    "HangupAllCallsResponseMessage": ".hangup_all_calls_response_message",
    "HangupCallParameters": ".hangup_call_parameters",
    "HangupCallResponse": ".hangup_call_response",
    "HangupCallResponseMessage": ".hangup_call_response_message",
    "PlayParameters": ".play_parameters",
    "PlayParametersLegs": ".play_parameters_legs",
    "PlayResponse": ".play_response",
    "PlayResponseMessage": ".play_response_message",
    "PlayStopParameters": ".play_stop_parameters",
    "PlayStopResponse": ".play_stop_response",
    "PlayStopResponseMessage": ".play_stop_response_message",
    "RecordStartParameters": ".record_start_parameters",
    "RecordStartParametersFileFormat": ".record_start_parameters_file_format",
    "RecordStartResponse": ".record_start_response",
    "RecordStartResponseMessage": ".record_start_response_message",
    "RecordStopParameters": ".record_stop_parameters",
    "RecordStopResponse": ".record_stop_response",
    "RecordStopResponseMessage": ".record_stop_response_message",
    "ScheduleHangupParameters": ".schedule_hangup_parameters",
    "ScheduleHangupResponse": ".schedule_hangup_response",
    "ScheduleHangupResponseMessage": ".schedule_hangup_response_message",
    "SchedulePlayParameters": ".schedule_play_parameters",
    "SchedulePlayParametersLegs": ".schedule_play_parameters_legs",
    "SchedulePlayResponse": ".schedule_play_response",
    "SchedulePlayResponseMessage": ".schedule_play_response_message",
    "SendDigitsParameters": ".send_digits_parameters",
    "SendDigitsParametersLeg": ".send_digits_parameters_leg",
    "SendDigitsResponse": ".send_digits_response",
    "SendDigitsResponseMessage": ".send_digits_response_message",
    "SoundTouchParameters": ".sound_touch_parameters",
    "SoundTouchParametersAudioDirection": ".sound_touch_parameters_audio_direction",
    "SoundTouchResponse": ".sound_touch_response",
    "SoundTouchResponseMessage": ".sound_touch_response_message",
    "SoundTouchStopParameters": ".sound_touch_stop_parameters",
    "SoundTouchStopResponse": ".sound_touch_stop_response",
    "SoundTouchStopResponseMessage": ".sound_touch_stop_response_message",
    "TransferCallParameters": ".transfer_call_parameters",
    "TransferCallResponse": ".transfer_call_response",
    "TransferCallResponseMessage": ".transfer_call_response_message",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "BulkCallParameters",
    "BulkCallResponse",
    "BulkCallResponseMessage",
    "CallNotificationParameters",
    "CallNotificationParametersAnsweredBy",
    "CallNotificationParametersCallStatus",
    "CallNotificationParametersDirection",
    "CallParameters",
    "CallParametersAsyncAmdStatusCallbackMethod",
    "CallParametersMachineDetection",
    "CallResponse",
    "CallResponseMessage",
    "CancelScheduledHangupParameters",
    "CancelScheduledHangupResponse",
    "CancelScheduledHangupResponseMessage",
    "CancelScheduledPlayParameters",
    "CancelScheduledPlayResponse",
    "CancelScheduledPlayResponseMessage",
    "ConferenceDeafParameters",
    "ConferenceDeafResponse",
    "ConferenceDeafResponseMessage",
    "ConferenceHangupParameters",
    "ConferenceHangupResponse",
    "ConferenceHangupResponseMessage",
    "ConferenceKickParameters",
    "ConferenceKickResponse",
    "ConferenceKickResponseMessage",
    "ConferenceListMembersParameters",
    "ConferenceListMembersResponse",
    "ConferenceListMembersResponseMessage",
    "ConferenceListParameters",
    "ConferenceListResponse",
    "ConferenceListResponseMessage",
    "ConferenceMuteParameters",
    "ConferenceMuteResponse",
    "ConferenceMuteResponseMessage",
    "ConferencePlayParameters",
    "ConferencePlayResponse",
    "ConferencePlayResponseMessage",
    "ConferenceRecordStartParameters",
    "ConferenceRecordStartParametersFileFormat",
    "ConferenceRecordStartResponse",
    "ConferenceRecordStartResponseMessage",
    "ConferenceRecordStopParameters",
    "ConferenceRecordStopResponse",
    "ConferenceRecordStopResponseMessage",
    "ConferenceSpeakParameters",
    "ConferenceSpeakResponse",
    "ConferenceSpeakResponseMessage",
    "ConferenceUndeafParameters",
    "ConferenceUndeafResponse",
    "ConferenceUndeafResponseMessage",
    "ConferenceUnmuteParameters",
    "ConferenceUnmuteResponse",
    "ConferenceUnmuteResponseMessage",
    "GroupCallParameters",
    "GroupCallResponse",
    "GroupCallResponseMessage",
    "HangupAllCallsParameters",
    "HangupAllCallsResponse",
    "HangupAllCallsResponseMessage",
    "HangupCallParameters",
    "HangupCallResponse",
    "HangupCallResponseMessage",
    "PlayParameters",
    "PlayParametersLegs",
    "PlayResponse",
    "PlayResponseMessage",
    "PlayStopParameters",
    "PlayStopResponse",
    "PlayStopResponseMessage",
    "RecordStartParameters",
    "RecordStartParametersFileFormat",
    "RecordStartResponse",
    "RecordStartResponseMessage",
    "RecordStopParameters",
    "RecordStopResponse",
    "RecordStopResponseMessage",
    "ScheduleHangupParameters",
    "ScheduleHangupResponse",
    "ScheduleHangupResponseMessage",
    "SchedulePlayParameters",
    "SchedulePlayParametersLegs",
    "SchedulePlayResponse",
    "SchedulePlayResponseMessage",
    "SendDigitsParameters",
    "SendDigitsParametersLeg",
    "SendDigitsResponse",
    "SendDigitsResponseMessage",
    "SoundTouchParameters",
    "SoundTouchParametersAudioDirection",
    "SoundTouchResponse",
    "SoundTouchResponseMessage",
    "SoundTouchStopParameters",
    "SoundTouchStopResponse",
    "SoundTouchStopResponseMessage",
    "TransferCallParameters",
    "TransferCallResponse",
    "TransferCallResponseMessage",
]
