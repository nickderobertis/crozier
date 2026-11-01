



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
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
_dynamic_imports: typing.Dict[str, str] = {
    "GetActiveSoundCardOutputModeResponse": ".types",
    "GetAirplayExtraDelayResponse": ".types",
    "GetAllRoutinesResponse": ".types",
    "GetAllRoutinesResponseRoutinesItem": ".types",
    "GetAllRoutinesResponseRoutinesItemStepsItem": ".types",
    "GetAsrStatusResponse": ".types",
    "GetAudioInputCapabilityResponse": ".types",
    "GetAudioInputCapabilityResponseAudioInputItem": ".types",
    "GetAudioOutMax32BitResponse": ".types",
    "GetButtonVolumeStepResponse": ".types",
    "GetCxdishPrecentResponse": ".types",
    "GetDigitalFilterTypeSupportListResponse": ".types",
    "GetDigitalFilterTypeSupportListResponseDigitalFilterTypesItem": ".types",
    "GetLmpFilterCapabilityResponse": ".types",
    "GetMainSubExtraDelayResponse": ".types",
    "GetMainSubExtraDelayResponseBody": ".types",
    "GetMvRemoteSilenceUpdateTimeResponse": ".types",
    "GetMvRemoteUpdateDeviceOtaInfoResponse": ".types",
    "GetMvRemoteUpdateDeviceOtaInfoResponseImgListItem": ".types",
    "GetMvRomBurnPrecentResponse": ".types",
    "GetMvRomDownloadStatusResponse": ".types",
    "GetMvRomDownloadV2StatusResponse": ".types",
    "GetRemoteVolumeStepResponse": ".types",
    "GetRoutineCapabilityResponse": ".types",
    "StreamServicesCapabilityResponse": ".types",
    "StreamServicesCapabilityResponseStreamServicesItem": ".types",
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
    "StreamServicesCapabilityResponse",
    "StreamServicesCapabilityResponseStreamServicesItem",
]
