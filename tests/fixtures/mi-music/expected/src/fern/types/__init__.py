



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .cmd_status_resp import CmdStatusResp
    from .download_json_resp import DownloadJsonResp
    from .http_validation_error import HttpValidationError
    from .latest_version_resp import LatestVersionResp
    from .music_info_item import MusicInfoItem
    from .music_info_resp import MusicInfoResp
    from .play_list_music_obj import PlayListMusicObj
    from .play_list_obj import PlayListObj
    from .playing_music_resp import PlayingMusicResp
    from .playlist_musics_resp import PlaylistMusicsResp
    from .playlist_names_resp import PlaylistNamesResp
    from .ret_msg import RetMsg
    from .set_volume_resp import SetVolumeResp
    from .upload_cookie_resp import UploadCookieResp
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
    from .version_resp import VersionResp
    from .volume_resp import VolumeResp
    from .ws_token_resp import WsTokenResp
_dynamic_imports: typing.Dict[str, str] = {
    "CmdStatusResp": ".cmd_status_resp",
    "DownloadJsonResp": ".download_json_resp",
    "HttpValidationError": ".http_validation_error",
    "LatestVersionResp": ".latest_version_resp",
    "MusicInfoItem": ".music_info_item",
    "MusicInfoResp": ".music_info_resp",
    "PlayListMusicObj": ".play_list_music_obj",
    "PlayListObj": ".play_list_obj",
    "PlayingMusicResp": ".playing_music_resp",
    "PlaylistMusicsResp": ".playlist_musics_resp",
    "PlaylistNamesResp": ".playlist_names_resp",
    "RetMsg": ".ret_msg",
    "SetVolumeResp": ".set_volume_resp",
    "UploadCookieResp": ".upload_cookie_resp",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
    "VersionResp": ".version_resp",
    "VolumeResp": ".volume_resp",
    "WsTokenResp": ".ws_token_resp",
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
    "CmdStatusResp",
    "DownloadJsonResp",
    "HttpValidationError",
    "LatestVersionResp",
    "MusicInfoItem",
    "MusicInfoResp",
    "PlayListMusicObj",
    "PlayListObj",
    "PlayingMusicResp",
    "PlaylistMusicsResp",
    "PlaylistNamesResp",
    "RetMsg",
    "SetVolumeResp",
    "UploadCookieResp",
    "ValidationError",
    "ValidationErrorLocItem",
    "VersionResp",
    "VolumeResp",
    "WsTokenResp",
]
