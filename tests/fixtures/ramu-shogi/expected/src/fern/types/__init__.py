



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .ai_support_player_settings import AiSupportPlayerSettings
    from .ai_support_player_settings_mode import AiSupportPlayerSettingsMode
    from .ai_support_settings import AiSupportSettings
    from .analysis_snapshot_detail import AnalysisSnapshotDetail
    from .analysis_snapshot_entry import AnalysisSnapshotEntry
    from .analysis_snapshot_summary import AnalysisSnapshotSummary
    from .api_error_response import ApiErrorResponse
    from .auth_session_response import AuthSessionResponse
    from .auth_session_response_one import AuthSessionResponseOne
    from .auth_session_response_zero import AuthSessionResponseZero
    from .auth_session_user import AuthSessionUser
    from .complete_nnue_upload_response import CompleteNnueUploadResponse
    from .create_analysis_snapshot_response import CreateAnalysisSnapshotResponse
    from .create_room_response import CreateRoomResponse
    from .game_record_detail import GameRecordDetail
    from .game_record_participant import GameRecordParticipant
    from .game_record_seat import GameRecordSeat
    from .game_record_source import GameRecordSource
    from .game_record_status import GameRecordStatus
    from .game_record_summary import GameRecordSummary
    from .game_record_visibility import GameRecordVisibility
    from .game_result_payload import GameResultPayload
    from .get_analysis_snapshot_response import GetAnalysisSnapshotResponse
    from .get_game_response import GetGameResponse
    from .get_public_game_response import GetPublicGameResponse
    from .get_user_settings_response import GetUserSettingsResponse
    from .get_user_settings_response_document import GetUserSettingsResponseDocument
    from .initialize_nnue_upload_response import InitializeNnueUploadResponse
    from .json_value import JsonValue
    from .list_analysis_snapshots_response import ListAnalysisSnapshotsResponse
    from .list_games_response import ListGamesResponse
    from .list_nnue_files_response import ListNnueFilesResponse
    from .list_public_games_response import ListPublicGamesResponse
    from .list_user_settings_response import ListUserSettingsResponse
    from .nnue_file_summary import NnueFileSummary
    from .nnue_upload_status import NnueUploadStatus
    from .ok_response import OkResponse
    from .pass_rights_config import PassRightsConfig
    from .put_user_settings_response import PutUserSettingsResponse
    from .room_info import RoomInfo
    from .room_info_player import RoomInfoPlayer
    from .room_info_players import RoomInfoPlayers
    from .room_settings import RoomSettings
    from .room_status import RoomStatus
    from .time_control_settings import TimeControlSettings, TimeControlSettings_Byoyomi, TimeControlSettings_Fischer
    from .time_control_settings_byoyomi import TimeControlSettingsByoyomi
    from .time_control_settings_fischer import TimeControlSettingsFischer
    from .update_game_visibility_response import UpdateGameVisibilityResponse
    from .update_profile_response import UpdateProfileResponse
    from .upload_nnue_part_response import UploadNnuePartResponse
    from .user_settings_document import UserSettingsDocument
    from .user_settings_document_key import UserSettingsDocumentKey
_dynamic_imports: typing.Dict[str, str] = {
    "AiSupportPlayerSettings": ".ai_support_player_settings",
    "AiSupportPlayerSettingsMode": ".ai_support_player_settings_mode",
    "AiSupportSettings": ".ai_support_settings",
    "AnalysisSnapshotDetail": ".analysis_snapshot_detail",
    "AnalysisSnapshotEntry": ".analysis_snapshot_entry",
    "AnalysisSnapshotSummary": ".analysis_snapshot_summary",
    "ApiErrorResponse": ".api_error_response",
    "AuthSessionResponse": ".auth_session_response",
    "AuthSessionResponseOne": ".auth_session_response_one",
    "AuthSessionResponseZero": ".auth_session_response_zero",
    "AuthSessionUser": ".auth_session_user",
    "CompleteNnueUploadResponse": ".complete_nnue_upload_response",
    "CreateAnalysisSnapshotResponse": ".create_analysis_snapshot_response",
    "CreateRoomResponse": ".create_room_response",
    "GameRecordDetail": ".game_record_detail",
    "GameRecordParticipant": ".game_record_participant",
    "GameRecordSeat": ".game_record_seat",
    "GameRecordSource": ".game_record_source",
    "GameRecordStatus": ".game_record_status",
    "GameRecordSummary": ".game_record_summary",
    "GameRecordVisibility": ".game_record_visibility",
    "GameResultPayload": ".game_result_payload",
    "GetAnalysisSnapshotResponse": ".get_analysis_snapshot_response",
    "GetGameResponse": ".get_game_response",
    "GetPublicGameResponse": ".get_public_game_response",
    "GetUserSettingsResponse": ".get_user_settings_response",
    "GetUserSettingsResponseDocument": ".get_user_settings_response_document",
    "InitializeNnueUploadResponse": ".initialize_nnue_upload_response",
    "JsonValue": ".json_value",
    "ListAnalysisSnapshotsResponse": ".list_analysis_snapshots_response",
    "ListGamesResponse": ".list_games_response",
    "ListNnueFilesResponse": ".list_nnue_files_response",
    "ListPublicGamesResponse": ".list_public_games_response",
    "ListUserSettingsResponse": ".list_user_settings_response",
    "NnueFileSummary": ".nnue_file_summary",
    "NnueUploadStatus": ".nnue_upload_status",
    "OkResponse": ".ok_response",
    "PassRightsConfig": ".pass_rights_config",
    "PutUserSettingsResponse": ".put_user_settings_response",
    "RoomInfo": ".room_info",
    "RoomInfoPlayer": ".room_info_player",
    "RoomInfoPlayers": ".room_info_players",
    "RoomSettings": ".room_settings",
    "RoomStatus": ".room_status",
    "TimeControlSettings": ".time_control_settings",
    "TimeControlSettingsByoyomi": ".time_control_settings_byoyomi",
    "TimeControlSettingsFischer": ".time_control_settings_fischer",
    "TimeControlSettings_Byoyomi": ".time_control_settings",
    "TimeControlSettings_Fischer": ".time_control_settings",
    "UpdateGameVisibilityResponse": ".update_game_visibility_response",
    "UpdateProfileResponse": ".update_profile_response",
    "UploadNnuePartResponse": ".upload_nnue_part_response",
    "UserSettingsDocument": ".user_settings_document",
    "UserSettingsDocumentKey": ".user_settings_document_key",
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
    "AiSupportPlayerSettings",
    "AiSupportPlayerSettingsMode",
    "AiSupportSettings",
    "AnalysisSnapshotDetail",
    "AnalysisSnapshotEntry",
    "AnalysisSnapshotSummary",
    "ApiErrorResponse",
    "AuthSessionResponse",
    "AuthSessionResponseOne",
    "AuthSessionResponseZero",
    "AuthSessionUser",
    "CompleteNnueUploadResponse",
    "CreateAnalysisSnapshotResponse",
    "CreateRoomResponse",
    "GameRecordDetail",
    "GameRecordParticipant",
    "GameRecordSeat",
    "GameRecordSource",
    "GameRecordStatus",
    "GameRecordSummary",
    "GameRecordVisibility",
    "GameResultPayload",
    "GetAnalysisSnapshotResponse",
    "GetGameResponse",
    "GetPublicGameResponse",
    "GetUserSettingsResponse",
    "GetUserSettingsResponseDocument",
    "InitializeNnueUploadResponse",
    "JsonValue",
    "ListAnalysisSnapshotsResponse",
    "ListGamesResponse",
    "ListNnueFilesResponse",
    "ListPublicGamesResponse",
    "ListUserSettingsResponse",
    "NnueFileSummary",
    "NnueUploadStatus",
    "OkResponse",
    "PassRightsConfig",
    "PutUserSettingsResponse",
    "RoomInfo",
    "RoomInfoPlayer",
    "RoomInfoPlayers",
    "RoomSettings",
    "RoomStatus",
    "TimeControlSettings",
    "TimeControlSettingsByoyomi",
    "TimeControlSettingsFischer",
    "TimeControlSettings_Byoyomi",
    "TimeControlSettings_Fischer",
    "UpdateGameVisibilityResponse",
    "UpdateProfileResponse",
    "UploadNnuePartResponse",
    "UserSettingsDocument",
    "UserSettingsDocumentKey",
]
