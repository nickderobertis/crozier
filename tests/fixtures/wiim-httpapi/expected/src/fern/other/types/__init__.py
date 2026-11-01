



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_active_sound_card_output_mode_response import GetActiveSoundCardOutputModeResponse
    from .get_airplay_extra_delay_response import GetAirplayExtraDelayResponse
    from .get_all_routines_response import GetAllRoutinesResponse
    from .get_all_routines_response_routines_item import GetAllRoutinesResponseRoutinesItem
    from .get_all_routines_response_routines_item_steps_item import GetAllRoutinesResponseRoutinesItemStepsItem
    from .get_asr_status_response import GetAsrStatusResponse
    from .get_audio_input_capability_response import GetAudioInputCapabilityResponse
    from .get_audio_input_capability_response_audio_input_item import GetAudioInputCapabilityResponseAudioInputItem
    from .get_audio_out_max32bit_response import GetAudioOutMax32BitResponse
    from .get_button_volume_step_response import GetButtonVolumeStepResponse
    from .get_cxdish_precent_response import GetCxdishPrecentResponse
    from .get_digital_filter_type_support_list_response import GetDigitalFilterTypeSupportListResponse
    from .get_digital_filter_type_support_list_response_digital_filter_types_item import (
        GetDigitalFilterTypeSupportListResponseDigitalFilterTypesItem,
    )
    from .get_lmp_filter_capability_response import GetLmpFilterCapabilityResponse
    from .get_main_sub_extra_delay_response import GetMainSubExtraDelayResponse
    from .get_main_sub_extra_delay_response_body import GetMainSubExtraDelayResponseBody
    from .get_mv_remote_silence_update_time_response import GetMvRemoteSilenceUpdateTimeResponse
    from .get_mv_remote_update_device_ota_info_response import GetMvRemoteUpdateDeviceOtaInfoResponse
    from .get_mv_remote_update_device_ota_info_response_img_list_item import (
        GetMvRemoteUpdateDeviceOtaInfoResponseImgListItem,
    )
    from .get_mv_rom_burn_precent_response import GetMvRomBurnPrecentResponse
    from .get_mv_rom_download_status_response import GetMvRomDownloadStatusResponse
    from .get_mv_rom_download_v2status_response import GetMvRomDownloadV2StatusResponse
    from .get_remote_volume_step_response import GetRemoteVolumeStepResponse
    from .get_routine_capability_response import GetRoutineCapabilityResponse
    from .stream_services_capability_response import StreamServicesCapabilityResponse
    from .stream_services_capability_response_stream_services_item import (
        StreamServicesCapabilityResponseStreamServicesItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GetActiveSoundCardOutputModeResponse": ".get_active_sound_card_output_mode_response",
    "GetAirplayExtraDelayResponse": ".get_airplay_extra_delay_response",
    "GetAllRoutinesResponse": ".get_all_routines_response",
    "GetAllRoutinesResponseRoutinesItem": ".get_all_routines_response_routines_item",
    "GetAllRoutinesResponseRoutinesItemStepsItem": ".get_all_routines_response_routines_item_steps_item",
    "GetAsrStatusResponse": ".get_asr_status_response",
    "GetAudioInputCapabilityResponse": ".get_audio_input_capability_response",
    "GetAudioInputCapabilityResponseAudioInputItem": ".get_audio_input_capability_response_audio_input_item",
    "GetAudioOutMax32BitResponse": ".get_audio_out_max32bit_response",
    "GetButtonVolumeStepResponse": ".get_button_volume_step_response",
    "GetCxdishPrecentResponse": ".get_cxdish_precent_response",
    "GetDigitalFilterTypeSupportListResponse": ".get_digital_filter_type_support_list_response",
    "GetDigitalFilterTypeSupportListResponseDigitalFilterTypesItem": ".get_digital_filter_type_support_list_response_digital_filter_types_item",
    "GetLmpFilterCapabilityResponse": ".get_lmp_filter_capability_response",
    "GetMainSubExtraDelayResponse": ".get_main_sub_extra_delay_response",
    "GetMainSubExtraDelayResponseBody": ".get_main_sub_extra_delay_response_body",
    "GetMvRemoteSilenceUpdateTimeResponse": ".get_mv_remote_silence_update_time_response",
    "GetMvRemoteUpdateDeviceOtaInfoResponse": ".get_mv_remote_update_device_ota_info_response",
    "GetMvRemoteUpdateDeviceOtaInfoResponseImgListItem": ".get_mv_remote_update_device_ota_info_response_img_list_item",
    "GetMvRomBurnPrecentResponse": ".get_mv_rom_burn_precent_response",
    "GetMvRomDownloadStatusResponse": ".get_mv_rom_download_status_response",
    "GetMvRomDownloadV2StatusResponse": ".get_mv_rom_download_v2status_response",
    "GetRemoteVolumeStepResponse": ".get_remote_volume_step_response",
    "GetRoutineCapabilityResponse": ".get_routine_capability_response",
    "StreamServicesCapabilityResponse": ".stream_services_capability_response",
    "StreamServicesCapabilityResponseStreamServicesItem": ".stream_services_capability_response_stream_services_item",
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
