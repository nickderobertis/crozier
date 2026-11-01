



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        BluetoothDeviceList,
        BluetoothDeviceListListItem,
        DeviceDebugInfo,
        DeviceStatus,
        PlayerStatus,
        PlayerStatusStatus,
        PresetList,
        PresetListPresetListItem,
        StaticIpInfo,
        TrackMetadata,
        TrackMetadataMetaData,
    )
    from . import (
        alarm_clock,
        alexa,
        amazon_music,
        audio_output_control,
        bluetooth,
        device_control,
        device_information,
        equalizer,
        generic,
        multiroom,
        network,
        other,
        playback_control,
        presets,
        room_correction,
        source_input_switch,
        track_metadata,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .device_control import GetHwErrorInfoResponse, GetHwErrorInfoResponseSoundCardHwError
    from .environment import FernApiEnvironment
    from .equalizer import (
        EqGetSourceModesResponseItem,
        GetEqStatResponse,
        GetEqStatResponseEqStat,
        LoadEqByNameRequestName,
    )
    from .other import (
        GetActiveSoundCardOutputModeResponse,
        GetAirplayExtraDelayResponse,
        GetAllRoutinesResponse,
        GetAllRoutinesResponseRoutinesItem,
        GetAllRoutinesResponseRoutinesItemStepsItem,
        GetAsrStatusResponse,
        GetAudioInputCapabilityResponse,
        GetAudioInputCapabilityResponseAudioInputItem,
        GetAudioOutMax32BitResponse,
        GetButtonVolumeStepResponse,
        GetCxdishPrecentResponse,
        GetDigitalFilterTypeSupportListResponse,
        GetDigitalFilterTypeSupportListResponseDigitalFilterTypesItem,
        GetLmpFilterCapabilityResponse,
        GetMainSubExtraDelayResponse,
        GetMainSubExtraDelayResponseBody,
        GetMvRemoteSilenceUpdateTimeResponse,
        GetMvRemoteUpdateDeviceOtaInfoResponse,
        GetMvRemoteUpdateDeviceOtaInfoResponseImgListItem,
        GetMvRomBurnPrecentResponse,
        GetMvRomDownloadStatusResponse,
        GetMvRomDownloadV2StatusResponse,
        GetRemoteVolumeStepResponse,
        GetRoutineCapabilityResponse,
        StreamServicesCapabilityResponse,
        StreamServicesCapabilityResponseStreamServicesItem,
    )
    from .room_correction import RoomCorrGetResponse, RoomCorrGetResponseEqBandItem
    from .source_input_switch import SetPlayerCmdSwitchModeRequestMode
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BluetoothDeviceList": ".types",
    "BluetoothDeviceListListItem": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DeviceDebugInfo": ".types",
    "DeviceStatus": ".types",
    "EqGetSourceModesResponseItem": ".equalizer",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GetActiveSoundCardOutputModeResponse": ".other",
    "GetAirplayExtraDelayResponse": ".other",
    "GetAllRoutinesResponse": ".other",
    "GetAllRoutinesResponseRoutinesItem": ".other",
    "GetAllRoutinesResponseRoutinesItemStepsItem": ".other",
    "GetAsrStatusResponse": ".other",
    "GetAudioInputCapabilityResponse": ".other",
    "GetAudioInputCapabilityResponseAudioInputItem": ".other",
    "GetAudioOutMax32BitResponse": ".other",
    "GetButtonVolumeStepResponse": ".other",
    "GetCxdishPrecentResponse": ".other",
    "GetDigitalFilterTypeSupportListResponse": ".other",
    "GetDigitalFilterTypeSupportListResponseDigitalFilterTypesItem": ".other",
    "GetEqStatResponse": ".equalizer",
    "GetEqStatResponseEqStat": ".equalizer",
    "GetHwErrorInfoResponse": ".device_control",
    "GetHwErrorInfoResponseSoundCardHwError": ".device_control",
    "GetLmpFilterCapabilityResponse": ".other",
    "GetMainSubExtraDelayResponse": ".other",
    "GetMainSubExtraDelayResponseBody": ".other",
    "GetMvRemoteSilenceUpdateTimeResponse": ".other",
    "GetMvRemoteUpdateDeviceOtaInfoResponse": ".other",
    "GetMvRemoteUpdateDeviceOtaInfoResponseImgListItem": ".other",
    "GetMvRomBurnPrecentResponse": ".other",
    "GetMvRomDownloadStatusResponse": ".other",
    "GetMvRomDownloadV2StatusResponse": ".other",
    "GetRemoteVolumeStepResponse": ".other",
    "GetRoutineCapabilityResponse": ".other",
    "LoadEqByNameRequestName": ".equalizer",
    "PlayerStatus": ".types",
    "PlayerStatusStatus": ".types",
    "PresetList": ".types",
    "PresetListPresetListItem": ".types",
    "RoomCorrGetResponse": ".room_correction",
    "RoomCorrGetResponseEqBandItem": ".room_correction",
    "SetPlayerCmdSwitchModeRequestMode": ".source_input_switch",
    "StaticIpInfo": ".types",
    "StreamServicesCapabilityResponse": ".other",
    "StreamServicesCapabilityResponseStreamServicesItem": ".other",
    "TrackMetadata": ".types",
    "TrackMetadataMetaData": ".types",
    "__version__": ".version",
    "alarm_clock": ".alarm_clock",
    "alexa": ".alexa",
    "amazon_music": ".amazon_music",
    "audio_output_control": ".audio_output_control",
    "bluetooth": ".bluetooth",
    "device_control": ".device_control",
    "device_information": ".device_information",
    "equalizer": ".equalizer",
    "generic": ".generic",
    "multiroom": ".multiroom",
    "network": ".network",
    "other": ".other",
    "playback_control": ".playback_control",
    "presets": ".presets",
    "room_correction": ".room_correction",
    "source_input_switch": ".source_input_switch",
    "track_metadata": ".track_metadata",
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
    "AsyncFernApi",
    "BluetoothDeviceList",
    "BluetoothDeviceListListItem",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "DeviceDebugInfo",
    "DeviceStatus",
    "EqGetSourceModesResponseItem",
    "FernApi",
    "FernApiEnvironment",
    "GetActiveSoundCardOutputModeResponse",
    "GetAirplayExtraDelayResponse",
    "GetAllRoutinesResponse",
    "GetAllRoutinesResponseRoutinesItem",
    "GetAllRoutinesResponseRoutinesItemStepsItem",
    "GetAsrStatusResponse",
    "GetAudioInputCapabilityResponse",
    "GetAudioInputCapabilityResponseAudioInputItem",
    "GetAudioOutMax32BitResponse",
    "GetButtonVolumeStepResponse",
    "GetCxdishPrecentResponse",
    "GetDigitalFilterTypeSupportListResponse",
    "GetDigitalFilterTypeSupportListResponseDigitalFilterTypesItem",
    "GetEqStatResponse",
    "GetEqStatResponseEqStat",
    "GetHwErrorInfoResponse",
    "GetHwErrorInfoResponseSoundCardHwError",
    "GetLmpFilterCapabilityResponse",
    "GetMainSubExtraDelayResponse",
    "GetMainSubExtraDelayResponseBody",
    "GetMvRemoteSilenceUpdateTimeResponse",
    "GetMvRemoteUpdateDeviceOtaInfoResponse",
    "GetMvRemoteUpdateDeviceOtaInfoResponseImgListItem",
    "GetMvRomBurnPrecentResponse",
    "GetMvRomDownloadStatusResponse",
    "GetMvRomDownloadV2StatusResponse",
    "GetRemoteVolumeStepResponse",
    "GetRoutineCapabilityResponse",
    "LoadEqByNameRequestName",
    "PlayerStatus",
    "PlayerStatusStatus",
    "PresetList",
    "PresetListPresetListItem",
    "RoomCorrGetResponse",
    "RoomCorrGetResponseEqBandItem",
    "SetPlayerCmdSwitchModeRequestMode",
    "StaticIpInfo",
    "StreamServicesCapabilityResponse",
    "StreamServicesCapabilityResponseStreamServicesItem",
    "TrackMetadata",
    "TrackMetadataMetaData",
    "__version__",
    "alarm_clock",
    "alexa",
    "amazon_music",
    "audio_output_control",
    "bluetooth",
    "device_control",
    "device_information",
    "equalizer",
    "generic",
    "multiroom",
    "network",
    "other",
    "playback_control",
    "presets",
    "room_correction",
    "source_input_switch",
    "track_metadata",
]
