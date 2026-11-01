

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawOtherClient, RawOtherClient
from .types.get_active_sound_card_output_mode_response import GetActiveSoundCardOutputModeResponse
from .types.get_airplay_extra_delay_response import GetAirplayExtraDelayResponse
from .types.get_all_routines_response import GetAllRoutinesResponse
from .types.get_asr_status_response import GetAsrStatusResponse
from .types.get_audio_input_capability_response import GetAudioInputCapabilityResponse
from .types.get_audio_out_max32bit_response import GetAudioOutMax32BitResponse
from .types.get_button_volume_step_response import GetButtonVolumeStepResponse
from .types.get_cxdish_precent_response import GetCxdishPrecentResponse
from .types.get_digital_filter_type_support_list_response import GetDigitalFilterTypeSupportListResponse
from .types.get_lmp_filter_capability_response import GetLmpFilterCapabilityResponse
from .types.get_main_sub_extra_delay_response import GetMainSubExtraDelayResponse
from .types.get_mv_remote_silence_update_time_response import GetMvRemoteSilenceUpdateTimeResponse
from .types.get_mv_remote_update_device_ota_info_response import GetMvRemoteUpdateDeviceOtaInfoResponse
from .types.get_mv_rom_burn_precent_response import GetMvRomBurnPrecentResponse
from .types.get_mv_rom_download_status_response import GetMvRomDownloadStatusResponse
from .types.get_mv_rom_download_v2status_response import GetMvRomDownloadV2StatusResponse
from .types.get_remote_volume_step_response import GetRemoteVolumeStepResponse
from .types.get_routine_capability_response import GetRoutineCapabilityResponse
from .types.stream_services_capability_response import StreamServicesCapabilityResponse


class OtherClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOtherClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOtherClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOtherClient
        """
        return self._raw_client

    def get_remote_volume_step(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetRemoteVolumeStepResponse:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=get_remote_volume_step

        Returns: {"status":"OK","remote_volume_step":1}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetRemoteVolumeStepResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_remote_volume_step()
        """
        _response = self._raw_client.get_remote_volume_step(request_options=request_options)
        return _response.data

    def set_remote_volume_step(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=set_remote_volume_step:{n}

        Parameters
        ----------
        n : int
            The volume step value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_remote_volume_step(
            n=1,
        )
        """
        _response = self._raw_client.set_remote_volume_step(n, request_options=request_options)
        return _response.data

    def get_mv_remote_silence_update_time(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMvRemoteSilenceUpdateTimeResponse:
        """
        ...

        Returns: {"start":"0:1", "end":"23:59"}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMvRemoteSilenceUpdateTimeResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_mv_remote_silence_update_time()
        """
        _response = self._raw_client.get_mv_remote_silence_update_time(request_options=request_options)
        return _response.data

    def get_spdif_out_max_cap(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_spdif_out_max_cap()
        """
        _response = self._raw_client.get_spdif_out_max_cap(request_options=request_options)
        return _response.data

    def get_coax_out_max_cap(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: 48000:16:0

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_coax_out_max_cap()
        """
        _response = self._raw_client.get_coax_out_max_cap(request_options=request_options)
        return _response.data

    def get_aux_voltage_support_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_aux_voltage_support_list()
        """
        _response = self._raw_client.get_aux_voltage_support_list(request_options=request_options)
        return _response.data

    def audio_cast_get_speaker_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.audio_cast_get_speaker_list()
        """
        _response = self._raw_client.audio_cast_get_speaker_list(request_options=request_options)
        return _response.data

    def audio_cast_scan_speaker(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.audio_cast_scan_speaker()
        """
        _response = self._raw_client.audio_cast_scan_speaker(request_options=request_options)
        return _response.data

    def audio_cast_speaker_get_transcode_buffer_time(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.audio_cast_speaker_get_transcode_buffer_time()
        """
        _response = self._raw_client.audio_cast_speaker_get_transcode_buffer_time(request_options=request_options)
        return _response.data

    def audio_cast_speaker_get_transcode_profile(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.audio_cast_speaker_get_transcode_profile()
        """
        _response = self._raw_client.audio_cast_speaker_get_transcode_profile(request_options=request_options)
        return _response.data

    def audio_cast_speaker_set_password(
        self, str1: str, str2: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str1 : str
            Unknown

        str2 : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.audio_cast_speaker_set_password(
            str1="str1",
            str2="str2",
        )
        """
        _response = self._raw_client.audio_cast_speaker_set_password(str1, str2, request_options=request_options)
        return _response.data

    def audio_cast_speaker_set_volume(
        self, str: str, volume: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        volume : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.audio_cast_speaker_set_volume(
            str="str",
            volume=1,
        )
        """
        _response = self._raw_client.audio_cast_speaker_set_volume(str, volume, request_options=request_options)
        return _response.data

    def get_sound_card_mode_support_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_sound_card_mode_support_list()
        """
        _response = self._raw_client.get_sound_card_mode_support_list(request_options=request_options)
        return _response.data

    def get_active_sound_card_output_mode(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetActiveSoundCardOutputModeResponse:
        """
        ...

        Returns: {"index":"1","mode":"AUDIO_OUTPUT_AUX_MODE","cardId":"hw:0,1","devName":"Speaker Out","btSource":"0","audioCast":"0"}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetActiveSoundCardOutputModeResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_active_sound_card_output_mode()
        """
        _response = self._raw_client.get_active_sound_card_output_mode(request_options=request_options)
        return _response.data

    def set_light_operation_bright_config(
        self, s: int, b: int, d: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Example: https://10.10.10.254/httpapi.asp?command=setLightOperationBrightConfig:{%22auto_sense_enable%22:0,%22default_bright%22:1,%22disable%22:1}

        Turns the screen of the WiiM Ultra on or off

        Parameters
        ----------
        s : int
            autosense?

        b : int
            brightness?

        d : int
            disable: 1 (off) or 0 (on)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_light_operation_bright_config(
            s=1,
            b=1,
            d=1,
        )
        """
        _response = self._raw_client.set_light_operation_bright_config(s, b, d, request_options=request_options)
        return _response.data

    def get_mv_remote_update_start_check(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: http://10.10.10.254/httpapi.asp?command=getMvRemoteUpdateStartCheck

        Search for the firmware updates available

        Returns: OK

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_mv_remote_update_start_check()
        """
        _response = self._raw_client.get_mv_remote_update_start_check(request_options=request_options)
        return _response.data

    def get_mv_remote_update_start(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: http://10.10.10.254/httpapi.asp?command=getMvRemoteUpdateStart

        After calling the interface, if a new version is available, the device starts to download updates. At the end of the download, the update process starts.

        WARNING: DO NOT POWER OFF DURING THIS PROCESS!!

        Returns: OK

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_mv_remote_update_start()
        """
        _response = self._raw_client.get_mv_remote_update_start(request_options=request_options)
        return _response.data

    def get_mv_remote_update_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: http://10.10.10.254/httpapi.asp?command=getMvRemoteUpdateStatus

        Get the download progress.

        Value    Meaning
        - 10    Under review
        - 20  OK
        - 21    The verification of the downloaded update file failed
        - 22    Downloading the update file failed
        - 23    The verification of the downloaded update file failed
        - 25    Start downloading
        - 27    Download complete
        - 30    Downloading and verification completed

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_mv_remote_update_status()
        """
        _response = self._raw_client.get_mv_remote_update_status(request_options=request_options)
        return _response.data

    def get_mv_rom_burn_precent(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMvRomBurnPrecentResponse:
        """
        Example: http://10.10.10.254/httpapi.asp?command=getMvRomBurnPrecent

        Status of updating

        Returns: { "status" : "0", "progress" : "50"}

        | Fields     | Meaning |
        | ---------|---------|
        | status     | State   |
        | progress | Progress between 0 to 100% |

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMvRomBurnPrecentResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_mv_rom_burn_precent()
        """
        _response = self._raw_client.get_mv_rom_burn_precent(request_options=request_options)
        return _response.data

    def easy_link_response_stop(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.easy_link_response_stop()
        """
        _response = self._raw_client.easy_link_response_stop(request_options=request_options)
        return _response.data

    def notify_upgrade_type_firmware(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.notify_upgrade_type_firmware()
        """
        _response = self._raw_client.notify_upgrade_type_firmware(request_options=request_options)
        return _response.data

    def get_lmp_filter_capability(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetLmpFilterCapabilityResponse:
        """
        ...

        Returns: { "version": "1.1" }

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLmpFilterCapabilityResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_lmp_filter_capability()
        """
        _response = self._raw_client.get_lmp_filter_capability(request_options=request_options)
        return _response.data

    def get_stream_service_config(
        self, source: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        source : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_stream_service_config(
            source="source",
        )
        """
        _response = self._raw_client.get_stream_service_config(source, request_options=request_options)
        return _response.data

    def set_handshake_code(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_handshake_code(
            str="str",
        )
        """
        _response = self._raw_client.set_handshake_code(str, request_options=request_options)
        return _response.data

    def getsyslog_ip(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.getsyslog_ip(
            str="str",
        )
        """
        _response = self._raw_client.getsyslog_ip(str, request_options=request_options)
        return _response.data

    def get_status_ip(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_status_ip(
            str="str",
        )
        """
        _response = self._raw_client.get_status_ip(str, request_options=request_options)
        return _response.data

    def get_update_server(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_update_server()
        """
        _response = self._raw_client.get_update_server(request_options=request_options)
        return _response.data

    def get_weather_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_weather_info()
        """
        _response = self._raw_client.get_weather_info(request_options=request_options)
        return _response.data

    def set_access_pin(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_access_pin(
            str="str",
        )
        """
        _response = self._raw_client.set_access_pin(str, request_options=request_options)
        return _response.data

    def set_language(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_language(
            str="str",
        )
        """
        _response = self._raw_client.set_language(str, request_options=request_options)
        return _response.data

    def auto_play_set(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.auto_play_set()
        """
        _response = self._raw_client.auto_play_set(request_options=request_options)
        return _response.data

    def get_mv_rom_download_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMvRomDownloadStatusResponse:
        """
        ...

        Returns: {"status":"0","count":"0","dcount":"0","wcount":"0","tsize":"0","dsize":"0","wsize":"0","csize":"0", "cdsize":"0", "cwsize":"0", "progress":"0","name":"","ver":"0","new_ver":"0"}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMvRomDownloadStatusResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_mv_rom_download_status()
        """
        _response = self._raw_client.get_mv_rom_download_status(request_options=request_options)
        return _response.data

    def get_mv_rom_download_v2status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMvRomDownloadV2StatusResponse:
        """
        ...

        Returns: {"status":"0","progress":"0","name":"","ver":"0","new_ver":"0"}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMvRomDownloadV2StatusResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_mv_rom_download_v2status()
        """
        _response = self._raw_client.get_mv_rom_download_v2status(request_options=request_options)
        return _response.data

    def set_hex_group_name(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_hex_group_name(
            str="str",
        )
        """
        _response = self._raw_client.set_hex_group_name(str, request_options=request_options)
        return _response.data

    def set_mv_remote_silence_ota_time(
        self, str: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_mv_remote_silence_ota_time(
            str="str",
        )
        """
        _response = self._raw_client.set_mv_remote_silence_ota_time(str, request_options=request_options)
        return _response.data

    def set_mv_remote_silence_update_time(
        self, str: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_mv_remote_silence_update_time(
            str="str",
        )
        """
        _response = self._raw_client.set_mv_remote_silence_update_time(str, request_options=request_options)
        return _response.data

    def set_timezone(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_timezone(
            str="str",
        )
        """
        _response = self._raw_client.set_timezone(str, request_options=request_options)
        return _response.data

    def check_access_pin(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.check_access_pin()
        """
        _response = self._raw_client.check_access_pin(request_options=request_options)
        return _response.data

    def set_update_server(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_update_server(
            str="str",
        )
        """
        _response = self._raw_client.set_update_server(str, request_options=request_options)
        return _response.data

    def set_weather_location(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_weather_location(
            str="str",
        )
        """
        _response = self._raw_client.set_weather_location(str, request_options=request_options)
        return _response.data

    def start_check(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.start_check()
        """
        _response = self._raw_client.start_check(request_options=request_options)
        return _response.data

    def getbatteryval(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.getbatteryval()
        """
        _response = self._raw_client.getbatteryval(request_options=request_options)
        return _response.data

    def get_asr_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetAsrStatusResponse:
        """
        ...

        Returns: { "times_talk_on": "0", "times_request_succeed": "0", "times_request_failed": "0", "times_vad_time_out": "0", "times_play_failed": "0", "open_failed": "0", "capture_failed": "0", "mode": "normal", "score": "0", "volume": "18", "play_status": "0", "config_score": "0", "config_interval": "0", "trigger_test_mode": "0", "trigger_mis_test_mode": "0", "trigger_recording": "0", "have_prompt": "0", "fallback_enable": "0", "profile": "near", "hands_free": "0", "status": "ok", "id": "0" }

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAsrStatusResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_asr_status()
        """
        _response = self._raw_client.get_asr_status(request_options=request_options)
        return _response.data

    def get_lp_auth_code(self, str: str, str2: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        str2 : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_lp_auth_code(
            str="str",
            str2="str2",
        )
        """
        _response = self._raw_client.get_lp_auth_code(str, str2, request_options=request_options)
        return _response.data

    def set_token_params(self, str: str, str2: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        str2 : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_token_params(
            str="str",
            str2="str2",
        )
        """
        _response = self._raw_client.set_token_params(str, str2, request_options=request_options)
        return _response.data

    def talkset_prompt(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.talkset_prompt(
            n=1,
        )
        """
        _response = self._raw_client.talkset_prompt(n, request_options=request_options)
        return _response.data

    def talkset_alarm_pre_wake(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.talkset_alarm_pre_wake(
            str="str",
        )
        """
        _response = self._raw_client.talkset_alarm_pre_wake(str, request_options=request_options)
        return _response.data

    def talkset_alarm_tone(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.talkset_alarm_tone(
            n=1,
        )
        """
        _response = self._raw_client.talkset_alarm_tone(n, request_options=request_options)
        return _response.data

    def talkset_alarm_tone_preview(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.talkset_alarm_tone_preview(
            n=1,
        )
        """
        _response = self._raw_client.talkset_alarm_tone_preview(n, request_options=request_options)
        return _response.data

    def talkset_alarm_volume(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.talkset_alarm_volume(
            n=1,
        )
        """
        _response = self._raw_client.talkset_alarm_volume(n, request_options=request_options)
        return _response.data

    def talkset_alarmcommon(
        self, str: str, n1: int, n2: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        n1 : int
            Unknown

        n2 : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.talkset_alarmcommon(
            str="str",
            n1=1,
            n2=1,
        )
        """
        _response = self._raw_client.talkset_alarmcommon(str, n1, n2, request_options=request_options)
        return _response.data

    def set_sync_play_extra_delay(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_sync_play_extra_delay(
            n=1,
        )
        """
        _response = self._raw_client.set_sync_play_extra_delay(n, request_options=request_options)
        return _response.data

    def set_initial_configuration(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_initial_configuration(
            n=1,
        )
        """
        _response = self._raw_client.set_initial_configuration(n, request_options=request_options)
        return _response.data

    def get_ui_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_ui_config()
        """
        _response = self._raw_client.get_ui_config(request_options=request_options)
        return _response.data

    def get_spdif_auto_sense_enable(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_spdif_auto_sense_enable()
        """
        _response = self._raw_client.get_spdif_auto_sense_enable(request_options=request_options)
        return _response.data

    def get_spdif_in_noise_remove(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_spdif_in_noise_remove()
        """
        _response = self._raw_client.get_spdif_in_noise_remove(request_options=request_options)
        return _response.data

    def phono_mode_switch_set(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.phono_mode_switch_set(
            str="str",
        )
        """
        _response = self._raw_client.phono_mode_switch_set(str, request_options=request_options)
        return _response.data

    def set_play_mode_volume_enable(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_play_mode_volume_enable(
            str="str",
        )
        """
        _response = self._raw_client.set_play_mode_volume_enable(str, request_options=request_options)
        return _response.data

    def get_ui_wallpaper_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_ui_wallpaper_list()
        """
        _response = self._raw_client.get_ui_wallpaper_list(request_options=request_options)
        return _response.data

    def set_play_mode_volume_value(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_play_mode_volume_value(
            str="str",
        )
        """
        _response = self._raw_client.set_play_mode_volume_value(str, request_options=request_options)
        return _response.data

    def set_power_mode_time(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_power_mode_time(
            str="str",
        )
        """
        _response = self._raw_client.set_power_mode_time(str, request_options=request_options)
        return _response.data

    def get_button_volume_step(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetButtonVolumeStepResponse:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=get_button_volume_step

        Returns: {"status":"OK","button_volume_step":2}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetButtonVolumeStepResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_button_volume_step()
        """
        _response = self._raw_client.get_button_volume_step(request_options=request_options)
        return _response.data

    def set_button_volume_step(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=set_button_volume_step:{str}

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_button_volume_step(
            str="str",
        )
        """
        _response = self._raw_client.set_button_volume_step(str, request_options=request_options)
        return _response.data

    def get_aux_auto_sense_enable(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: 0 or 1, where 0 means AUX auto-sense is disabled and 1 means AUX auto-sense is enabled

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_aux_auto_sense_enable()
        """
        _response = self._raw_client.get_aux_auto_sense_enable(request_options=request_options)
        return _response.data

    def set_ui_config(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_ui_config(
            str="str",
        )
        """
        _response = self._raw_client.set_ui_config(str, request_options=request_options)
        return _response.data

    def set_spdif_auto_sense_enable(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_spdif_auto_sense_enable(
            n=1,
        )
        """
        _response = self._raw_client.set_spdif_auto_sense_enable(n, request_options=request_options)
        return _response.data

    def set_spdif_in_noise_remove(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_spdif_in_noise_remove(
            str="str",
        )
        """
        _response = self._raw_client.set_spdif_in_noise_remove(str, request_options=request_options)
        return _response.data

    def get_channel_mode(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns an integer representing the current channel mode. The meaning of the values is currently unknown.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_channel_mode()
        """
        _response = self._raw_client.get_channel_mode(request_options=request_options)
        return _response.data

    def get_auto_sense_enable(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: 0 or 1, where 0 means auto-sense is disabled and 1 means auto-sense is enabled

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_auto_sense_enable()
        """
        _response = self._raw_client.get_auto_sense_enable(request_options=request_options)
        return _response.data

    def start_reboot_time(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.start_reboot_time()
        """
        _response = self._raw_client.start_reboot_time(request_options=request_options)
        return _response.data

    def led_switch_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.led_switch_get()
        """
        _response = self._raw_client.led_switch_get(request_options=request_options)
        return _response.data

    def get_mqa_receiver_cap(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: 0 or 1, where 0 means MQA is not supported and 1 means MQA is supported

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_mqa_receiver_cap()
        """
        _response = self._raw_client.get_mqa_receiver_cap(request_options=request_options)
        return _response.data

    def reload_button_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.reload_button_get()
        """
        _response = self._raw_client.reload_button_get(request_options=request_options)
        return _response.data

    def set_aux_auto_sense_enable(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_aux_auto_sense_enable(
            n=1,
        )
        """
        _response = self._raw_client.set_aux_auto_sense_enable(n, request_options=request_options)
        return _response.data

    def get_low_priority_prompt_disable(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: 0 or 1, where 0 means low priority prompts are enabled and 1 means low priority prompts are disabled

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_low_priority_prompt_disable()
        """
        _response = self._raw_client.get_low_priority_prompt_disable(request_options=request_options)
        return _response.data

    def get_soft_mute(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_soft_mute()
        """
        _response = self._raw_client.get_soft_mute(request_options=request_options)
        return _response.data

    def get_line_in_max_cap(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: 48000:16:0, which means a maximum sampling rate of 48000 Hz, a maximum bit depth of 16 bits, and a maximum channel count of 0 (unknown)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_line_in_max_cap()
        """
        _response = self._raw_client.get_line_in_max_cap(request_options=request_options)
        return _response.data

    def get_aux_in_max_cap(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: 48000:16:0, which means a maximum sampling rate of 48000 Hz, a maximum bit depth of 16 bits, and a maximum channel count of 0 (unknown)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_aux_in_max_cap()
        """
        _response = self._raw_client.get_aux_in_max_cap(request_options=request_options)
        return _response.data

    def get_uac_out_max_cap(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_uac_out_max_cap()
        """
        _response = self._raw_client.get_uac_out_max_cap(request_options=request_options)
        return _response.data

    def get_hdmi_auto_sense_enable(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: 0 or 1, where 0 means HDMI auto-sense is disabled and 1 means HDMI auto-sense is enabled

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_hdmi_auto_sense_enable()
        """
        _response = self._raw_client.get_hdmi_auto_sense_enable(request_options=request_options)
        return _response.data

    def set_channel_mode(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_channel_mode(
            n=1,
        )
        """
        _response = self._raw_client.set_channel_mode(n, request_options=request_options)
        return _response.data

    def get_sync_play_extra_delay(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_sync_play_extra_delay()
        """
        _response = self._raw_client.get_sync_play_extra_delay(request_options=request_options)
        return _response.data

    def get_light_operation_bright_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_light_operation_bright_config()
        """
        _response = self._raw_client.get_light_operation_bright_config(request_options=request_options)
        return _response.data

    def set_ui_wallpaper_list(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_ui_wallpaper_list(
            str="str",
        )
        """
        _response = self._raw_client.set_ui_wallpaper_list(str, request_options=request_options)
        return _response.data

    def get_main_sub_extra_delay(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMainSubExtraDelayResponse:
        """
        ...

        Returns, without Subwoofer attached: {"category": "mainsubdelay", "body": {"errorType": "-1000", "mainSubExtraDelay": "-1000.000", "mainDelay": "-1000.000", "subDelay": "-1000.000", "errorDescribe": "unknow error"}}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMainSubExtraDelayResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_main_sub_extra_delay()
        """
        _response = self._raw_client.get_main_sub_extra_delay(request_options=request_options)
        return _response.data

    def cast_disable(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.cast_disable()
        """
        _response = self._raw_client.cast_disable(request_options=request_options)
        return _response.data

    def cast_disable_usage_report(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.cast_disable_usage_report()
        """
        _response = self._raw_client.cast_disable_usage_report(request_options=request_options)
        return _response.data

    def set_auto_sense_enable(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_auto_sense_enable(
            str="str",
        )
        """
        _response = self._raw_client.set_auto_sense_enable(str, request_options=request_options)
        return _response.data

    def phono_mode_switch_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.phono_mode_switch_get()
        """
        _response = self._raw_client.phono_mode_switch_get(request_options=request_options)
        return _response.data

    def get_play_mode_volume_enable(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_play_mode_volume_enable()
        """
        _response = self._raw_client.get_play_mode_volume_enable(request_options=request_options)
        return _response.data

    def set_volume_control(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_volume_control(
            n=1,
        )
        """
        _response = self._raw_client.set_volume_control(n, request_options=request_options)
        return _response.data

    def get_play_mode_volume_value(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_play_mode_volume_value()
        """
        _response = self._raw_client.get_play_mode_volume_value(request_options=request_options)
        return _response.data

    def set_mqa_receiver_cap(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_mqa_receiver_cap(
            str="str",
        )
        """
        _response = self._raw_client.set_mqa_receiver_cap(str, request_options=request_options)
        return _response.data

    def get_power_mode_time(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_power_mode_time()
        """
        _response = self._raw_client.get_power_mode_time(request_options=request_options)
        return _response.data

    def set_max_volume(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_max_volume(
            n=1,
        )
        """
        _response = self._raw_client.set_max_volume(n, request_options=request_options)
        return _response.data

    def enable_cast(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.enable_cast()
        """
        _response = self._raw_client.enable_cast(request_options=request_options)
        return _response.data

    def reload_button_update(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.reload_button_update(
            str="str",
        )
        """
        _response = self._raw_client.reload_button_update(str, request_options=request_options)
        return _response.data

    def enable_cast_usage_report(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.enable_cast_usage_report()
        """
        _response = self._raw_client.enable_cast_usage_report(request_options=request_options)
        return _response.data

    def disable_low_priority_prompt(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.disable_low_priority_prompt(
            str="str",
        )
        """
        _response = self._raw_client.disable_low_priority_prompt(str, request_options=request_options)
        return _response.data

    def set_soft_mute(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_soft_mute(
            str="str",
        )
        """
        _response = self._raw_client.set_soft_mute(str, request_options=request_options)
        return _response.data

    def set_hdmi_auto_sense_enable(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_hdmi_auto_sense_enable(
            n=1,
        )
        """
        _response = self._raw_client.set_hdmi_auto_sense_enable(n, request_options=request_options)
        return _response.data

    def set_spdif_out_max_cap(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_spdif_out_max_cap(
            str="str",
        )
        """
        _response = self._raw_client.set_spdif_out_max_cap(str, request_options=request_options)
        return _response.data

    def set_coax_out_max_cap(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_coax_out_max_cap(
            str="str",
        )
        """
        _response = self._raw_client.set_coax_out_max_cap(str, request_options=request_options)
        return _response.data

    def set_line_in_max_cap(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_line_in_max_cap(
            str="str",
        )
        """
        _response = self._raw_client.set_line_in_max_cap(str, request_options=request_options)
        return _response.data

    def set_aux_in_max_cap(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_aux_in_max_cap(
            str="str",
        )
        """
        _response = self._raw_client.set_aux_in_max_cap(str, request_options=request_options)
        return _response.data

    def set_uac_out_max_cap(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_uac_out_max_cap(
            str="str",
        )
        """
        _response = self._raw_client.set_uac_out_max_cap(str, request_options=request_options)
        return _response.data

    def enable_sys_info(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.enable_sys_info(
            n=1,
        )
        """
        _response = self._raw_client.enable_sys_info(n, request_options=request_options)
        return _response.data

    def get_airplay_extra_delay(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAirplayExtraDelayResponse:
        """
        Makes a call to https://10.10.10.254/httpapi?command=GetAirplayExtraDelay

        Returns: {"AirplayExtraDelay":-10}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAirplayExtraDelayResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_airplay_extra_delay()
        """
        _response = self._raw_client.get_airplay_extra_delay(request_options=request_options)
        return _response.data

    def get_current_wireless_connect(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi?command=GetCurrentWirelessConnect

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_current_wireless_connect()
        """
        _response = self._raw_client.get_current_wireless_connect(request_options=request_options)
        return _response.data

    def slave_alert_get(self, ip: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        ip : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.slave_alert_get(
            ip="ip",
        )
        """
        _response = self._raw_client.slave_alert_get(ip, request_options=request_options)
        return _response.data

    def slave_talk_set_alarm_volume(
        self, ip: str, n: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        ip : str
            Unknown

        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.slave_talk_set_alarm_volume(
            ip="ip",
            n=1,
        )
        """
        _response = self._raw_client.slave_talk_set_alarm_volume(ip, n, request_options=request_options)
        return _response.data

    def squeezelite_auto_connect_enable(
        self, n: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.squeezelite_auto_connect_enable(
            n=1,
        )
        """
        _response = self._raw_client.squeezelite_auto_connect_enable(n, request_options=request_options)
        return _response.data

    def squeezelite_connect_server(self, ip: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        ip : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.squeezelite_connect_server(
            ip="ip",
        )
        """
        _response = self._raw_client.squeezelite_connect_server(ip, request_options=request_options)
        return _response.data

    def squeezelite_discover(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.squeezelite_discover()
        """
        _response = self._raw_client.squeezelite_discover(request_options=request_options)
        return _response.data

    def squeezelite_get_state(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.squeezelite_get_state()
        """
        _response = self._raw_client.squeezelite_get_state(request_options=request_options)
        return _response.data

    def get_setup_router_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_setup_router_info()
        """
        _response = self._raw_client.get_setup_router_info(request_options=request_options)
        return _response.data

    def set_setup_router_info(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_setup_router_info(
            str="str",
        )
        """
        _response = self._raw_client.set_setup_router_info(str, request_options=request_options)
        return _response.data

    def alert_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.alert_get()
        """
        _response = self._raw_client.alert_get(request_options=request_options)
        return _response.data

    def tvs_logout(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.tvs_logout()
        """
        _response = self._raw_client.tvs_logout(request_options=request_options)
        return _response.data

    def get_tvs_state(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_tvs_state()
        """
        _response = self._raw_client.get_tvs_state(request_options=request_options)
        return _response.data

    def get_tvs_dev_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_tvs_dev_info()
        """
        _response = self._raw_client.get_tvs_dev_info(request_options=request_options)
        return _response.data

    def set_tvs_access_token(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_tvs_access_token(
            str="str",
        )
        """
        _response = self._raw_client.set_tvs_access_token(str, request_options=request_options)
        return _response.data

    def set_tvs_debug_mode(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_tvs_debug_mode(
            str="str",
        )
        """
        _response = self._raw_client.set_tvs_debug_mode(str, request_options=request_options)
        return _response.data

    def set_tvs_client_id(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_tvs_client_id(
            str="str",
        )
        """
        _response = self._raw_client.set_tvs_client_id(str, request_options=request_options)
        return _response.data

    def create_routine(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.create_routine(
            str="str",
        )
        """
        _response = self._raw_client.create_routine(str, request_options=request_options)
        return _response.data

    def get_all_routines(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetAllRoutinesResponse:
        """
        ...

        Returns: { "routines": [ { "updateDate": "2025-10-12T12:03:48Z", "steps": [ { "type": "subwoofer", "payload": { "subOutput": 0 } }, { "type": "loopMode", "payload": { "mode": 3 } } ], "createDate": "2025-10-12T12:03:48Z", "id": "E59E781B-CE00-4347-9E5B-A82F47C675AC", "name": "Spotify Liked", "index": 1 } ] }

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAllRoutinesResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_all_routines()
        """
        _response = self._raw_client.get_all_routines(request_options=request_options)
        return _response.data

    def get_routine_capability(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetRoutineCapabilityResponse:
        """
        ...

        Returns: { "version": "1.1" }

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetRoutineCapabilityResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_routine_capability()
        """
        _response = self._raw_client.get_routine_capability(request_options=request_options)
        return _response.data

    def get_audio_input_capability(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAudioInputCapabilityResponse:
        """
        ...

        Returns: { "ver": "1.0", "audioInput": [ { "mode": "wifi" }, { "mode": "line-in" }, { "mode": "bluetooth" }, { "mode": "optical" }, { "mode": "HDMI" } ] }

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAudioInputCapabilityResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_audio_input_capability()
        """
        _response = self._raw_client.get_audio_input_capability(request_options=request_options)
        return _response.data

    def get_audio_out_max32bit(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAudioOutMax32BitResponse:
        """
        ...

        Returns: 0 or 1

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAudioOutMax32BitResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_audio_out_max32bit()
        """
        _response = self._raw_client.get_audio_out_max32bit(request_options=request_options)
        return _response.data

    def set_audio_out_max32bit(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        n: 0 or 1

        Parameters
        ----------
        n : int
            The desired audio output maximum 32-bit support (0 or 1)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_audio_out_max32bit(
            n=1,
        )
        """
        _response = self._raw_client.set_audio_out_max32bit(n, request_options=request_options)
        return _response.data

    def get_audio_output_vrms(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown (possibly the output type or identifier)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_audio_output_vrms(
            str="str",
        )
        """
        _response = self._raw_client.get_audio_output_vrms(str, request_options=request_options)
        return _response.data

    def get_audio_output_vrms_support_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_audio_output_vrms_support_list()
        """
        _response = self._raw_client.get_audio_output_vrms_support_list(request_options=request_options)
        return _response.data

    def set_audio_output_vrms(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown (possibly the output type or identifier)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_audio_output_vrms(
            str="str",
        )
        """
        _response = self._raw_client.set_audio_output_vrms(str, request_options=request_options)
        return _response.data

    def get_cbl_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_cbl_status()
        """
        _response = self._raw_client.get_cbl_status(request_options=request_options)
        return _response.data

    def get_cec_power_ctrl(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: 0 or 1

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_cec_power_ctrl()
        """
        _response = self._raw_client.get_cec_power_ctrl(request_options=request_options)
        return _response.data

    def set_cec_power_ctrl(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        n: 0 or 1

        Parameters
        ----------
        n : int
            The desired CEC power control status (0 or 1)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_cec_power_ctrl(
            n=1,
        )
        """
        _response = self._raw_client.set_cec_power_ctrl(n, request_options=request_options)
        return _response.data

    def get_cxdish_precent(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCxdishPrecentResponse:
        """
        ...

        Returns: {"status":"0","progress":"0"}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCxdishPrecentResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_cxdish_precent()
        """
        _response = self._raw_client.get_cxdish_precent(request_options=request_options)
        return _response.data

    def get_digital_filter_type_support_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDigitalFilterTypeSupportListResponse:
        """
        ...

        Returns: [ { "index": 1, "args": [ "amixer cset name='ES9018 DigiFilt' 0" ], "value": "Fast Roll-Off" }, { "index": 2, "args": [ "amixer cset name='ES9018 DigiFilt' 1" ], "value": "Slow Roll-Off" }, { "index": 3, "args": [ "amixer cset name='ES9018 DigiFilt' 2" ], "value": "Minimum Phase" } ]

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDigitalFilterTypeSupportListResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_digital_filter_type_support_list()
        """
        _response = self._raw_client.get_digital_filter_type_support_list(request_options=request_options)
        return _response.data

    def get_digital_filter_type(self, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        ...

        Returns: 1, 2, or 3 corresponding to the supported digital filter types

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_digital_filter_type()
        """
        _response = self._raw_client.get_digital_filter_type(request_options=request_options)
        return _response.data

    def set_digital_filter_type(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            The digital filter type to set (1, 2, or 3)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_digital_filter_type(
            n=1,
        )
        """
        _response = self._raw_client.set_digital_filter_type(n, request_options=request_options)
        return _response.data

    def get_output_digital_filter_type(
        self, str: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown (possibly the output type or identifier)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_output_digital_filter_type(
            str="str",
        )
        """
        _response = self._raw_client.get_output_digital_filter_type(str, request_options=request_options)
        return _response.data

    def get_output_digital_filter_type_support_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_output_digital_filter_type_support_list()
        """
        _response = self._raw_client.get_output_digital_filter_type_support_list(request_options=request_options)
        return _response.data

    def set_output_digital_filter_type(
        self, str: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown (possibly the output type or identifier)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_output_digital_filter_type(
            str="str",
        )
        """
        _response = self._raw_client.set_output_digital_filter_type(str, request_options=request_options)
        return _response.data

    def get_digital_input_audio_type_support(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: 0x1

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_digital_input_audio_type_support()
        """
        _response = self._raw_client.get_digital_input_audio_type_support(request_options=request_options)
        return _response.data

    def get_output_voltage(self, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        ...

        Returns an integer

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_output_voltage()
        """
        _response = self._raw_client.get_output_voltage(request_options=request_options)
        return _response.data

    def set_output_voltage(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            The desired output voltage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_output_voltage(
            n=1,
        )
        """
        _response = self._raw_client.set_output_voltage(n, request_options=request_options)
        return _response.data

    def get_feature_capability(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_feature_capability()
        """
        _response = self._raw_client.get_feature_capability(request_options=request_options)
        return _response.data

    def get_play_mode_gain_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_play_mode_gain_config()
        """
        _response = self._raw_client.get_play_mode_gain_config(request_options=request_options)
        return _response.data

    def set_play_mode_gain_config(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_play_mode_gain_config(
            str="str",
        )
        """
        _response = self._raw_client.set_play_mode_gain_config(str, request_options=request_options)
        return _response.data

    def mediaserver_scan(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.mediaserver_scan()
        """
        _response = self._raw_client.mediaserver_scan(request_options=request_options)
        return _response.data

    def mediaserver_udiskumount(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.mediaserver_udiskumount()
        """
        _response = self._raw_client.mediaserver_udiskumount(request_options=request_options)
        return _response.data

    def get_input_mode_support_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_input_mode_support_list()
        """
        _response = self._raw_client.get_input_mode_support_list(request_options=request_options)
        return _response.data

    def get_mode_rename(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, str]:
        """
        ...

        Returns: {"Line-In" : "", "SPDIF-In" : "PC"}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_mode_rename()
        """
        _response = self._raw_client.get_mode_rename(request_options=request_options)
        return _response.data

    def set_mode_rename(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_mode_rename(
            str="str",
        )
        """
        _response = self._raw_client.set_mode_rename(str, request_options=request_options)
        return _response.data

    def set_music_explicit(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        n: 0 or 1

        Parameters
        ----------
        n : int
            The desired music explicit content filter status (0 or 1)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_music_explicit(
            n=1,
        )
        """
        _response = self._raw_client.set_music_explicit(n, request_options=request_options)
        return _response.data

    def get_mv_remote_update_device_ota_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMvRemoteUpdateDeviceOtaInfoResponse:
        """
        ...

        Returns: {"language":"en_us","projectId":"0fb639765679eb9a7cf7d68761e2d71b6a2d62ea47cc049db3c7df61d6816fc9","fwVersion":"Linkplay.5.0.739659","version":"1.0","macAddr":"E8:2D:29:7C:45:40","serialNumber":"","deviceUid":"FA98F353DDFE707499E52529","imgList":[{"imgName":"hdmi","imgVersion":"71"},{"imgName":"moduleMulti","imgVersion":"Linkplay.5.0.739659"},{"imgName":"gc4a_zip","imgVersion":"Linkplay.5.0.739659"}]}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMvRemoteUpdateDeviceOtaInfoResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.get_mv_remote_update_device_ota_info()
        """
        _response = self._raw_client.get_mv_remote_update_device_ota_info(request_options=request_options)
        return _response.data

    def set_tunein_favorite_state(
        self, song_id: str, status: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        songId: The ID of the song
        status: 0 for not favorite, 1 for favorite

        Parameters
        ----------
        song_id : str
            The ID of the song

        status : int
            0 for not favorite, 1 for favorite

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_tunein_favorite_state(
            song_id="songId",
            status=1,
        )
        """
        _response = self._raw_client.set_tunein_favorite_state(song_id, status, request_options=request_options)
        return _response.data

    def set_tunein_location(
        self, latitude: str, longitude: str, serial: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        latitude: Latitude of the location
        longitude: Longitude of the location
        serial: Device serial number

        Parameters
        ----------
        latitude : str
            Latitude of the location

        longitude : str
            Longitude of the location

        serial : str
            Device serial number

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_tunein_location(
            latitude="latitude",
            longitude="longitude",
            serial="serial",
        )
        """
        _response = self._raw_client.set_tunein_location(latitude, longitude, serial, request_options=request_options)
        return _response.data

    def set_tunein_token(
        self,
        username: str,
        token: str,
        refresh_token: str,
        expires_in: int,
        userid: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        ...

        username: TuneIn account username
        token: Authentication token
        refreshToken: Token used to refresh the authentication token
        expires_in: Time in seconds until the token expires
        userid: TuneIn user ID

        Parameters
        ----------
        username : str
            TuneIn account username

        token : str
            Authentication token

        refresh_token : str
            Token used to refresh the authentication token

        expires_in : int
            Time in seconds until the token expires

        userid : str
            TuneIn user ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.set_tunein_token(
            username="username",
            token="token",
            refresh_token="refreshToken",
            expires_in=1,
            userid="userid",
        )
        """
        _response = self._raw_client.set_tunein_token(
            username, token, refresh_token, expires_in, userid, request_options=request_options
        )
        return _response.data

    def stream_services_capability(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StreamServicesCapabilityResponse:
        """
        ...

        Returns: { "version": "1.6", "encrypt": "1.0", "streamServices": [ { "id": "Prime", "version": "1.4", "quality": [ "SD", "HD", "UHD" ] }, { ... } ] }

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StreamServicesCapabilityResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.stream_services_capability()
        """
        _response = self._raw_client.stream_services_capability(request_options=request_options)
        return _response.data

    def tidal_login(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            The OAuth code obtained from Tidal authentication flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.other.tidal_login(
            str="str",
        )
        """
        _response = self._raw_client.tidal_login(str, request_options=request_options)
        return _response.data


class AsyncOtherClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOtherClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOtherClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOtherClient
        """
        return self._raw_client

    async def get_remote_volume_step(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetRemoteVolumeStepResponse:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=get_remote_volume_step

        Returns: {"status":"OK","remote_volume_step":1}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetRemoteVolumeStepResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_remote_volume_step()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_remote_volume_step(request_options=request_options)
        return _response.data

    async def set_remote_volume_step(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=set_remote_volume_step:{n}

        Parameters
        ----------
        n : int
            The volume step value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_remote_volume_step(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_remote_volume_step(n, request_options=request_options)
        return _response.data

    async def get_mv_remote_silence_update_time(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMvRemoteSilenceUpdateTimeResponse:
        """
        ...

        Returns: {"start":"0:1", "end":"23:59"}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMvRemoteSilenceUpdateTimeResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_mv_remote_silence_update_time()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mv_remote_silence_update_time(request_options=request_options)
        return _response.data

    async def get_spdif_out_max_cap(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_spdif_out_max_cap()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_spdif_out_max_cap(request_options=request_options)
        return _response.data

    async def get_coax_out_max_cap(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: 48000:16:0

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_coax_out_max_cap()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_coax_out_max_cap(request_options=request_options)
        return _response.data

    async def get_aux_voltage_support_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_aux_voltage_support_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_aux_voltage_support_list(request_options=request_options)
        return _response.data

    async def audio_cast_get_speaker_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.audio_cast_get_speaker_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.audio_cast_get_speaker_list(request_options=request_options)
        return _response.data

    async def audio_cast_scan_speaker(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.audio_cast_scan_speaker()


        asyncio.run(main())
        """
        _response = await self._raw_client.audio_cast_scan_speaker(request_options=request_options)
        return _response.data

    async def audio_cast_speaker_get_transcode_buffer_time(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.audio_cast_speaker_get_transcode_buffer_time()


        asyncio.run(main())
        """
        _response = await self._raw_client.audio_cast_speaker_get_transcode_buffer_time(request_options=request_options)
        return _response.data

    async def audio_cast_speaker_get_transcode_profile(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.audio_cast_speaker_get_transcode_profile()


        asyncio.run(main())
        """
        _response = await self._raw_client.audio_cast_speaker_get_transcode_profile(request_options=request_options)
        return _response.data

    async def audio_cast_speaker_set_password(
        self, str1: str, str2: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str1 : str
            Unknown

        str2 : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.audio_cast_speaker_set_password(
                str1="str1",
                str2="str2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.audio_cast_speaker_set_password(str1, str2, request_options=request_options)
        return _response.data

    async def audio_cast_speaker_set_volume(
        self, str: str, volume: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        volume : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.audio_cast_speaker_set_volume(
                str="str",
                volume=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.audio_cast_speaker_set_volume(str, volume, request_options=request_options)
        return _response.data

    async def get_sound_card_mode_support_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_sound_card_mode_support_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sound_card_mode_support_list(request_options=request_options)
        return _response.data

    async def get_active_sound_card_output_mode(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetActiveSoundCardOutputModeResponse:
        """
        ...

        Returns: {"index":"1","mode":"AUDIO_OUTPUT_AUX_MODE","cardId":"hw:0,1","devName":"Speaker Out","btSource":"0","audioCast":"0"}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetActiveSoundCardOutputModeResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_active_sound_card_output_mode()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_active_sound_card_output_mode(request_options=request_options)
        return _response.data

    async def set_light_operation_bright_config(
        self, s: int, b: int, d: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Example: https://10.10.10.254/httpapi.asp?command=setLightOperationBrightConfig:{%22auto_sense_enable%22:0,%22default_bright%22:1,%22disable%22:1}

        Turns the screen of the WiiM Ultra on or off

        Parameters
        ----------
        s : int
            autosense?

        b : int
            brightness?

        d : int
            disable: 1 (off) or 0 (on)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_light_operation_bright_config(
                s=1,
                b=1,
                d=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_light_operation_bright_config(s, b, d, request_options=request_options)
        return _response.data

    async def get_mv_remote_update_start_check(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: http://10.10.10.254/httpapi.asp?command=getMvRemoteUpdateStartCheck

        Search for the firmware updates available

        Returns: OK

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_mv_remote_update_start_check()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mv_remote_update_start_check(request_options=request_options)
        return _response.data

    async def get_mv_remote_update_start(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: http://10.10.10.254/httpapi.asp?command=getMvRemoteUpdateStart

        After calling the interface, if a new version is available, the device starts to download updates. At the end of the download, the update process starts.

        WARNING: DO NOT POWER OFF DURING THIS PROCESS!!

        Returns: OK

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_mv_remote_update_start()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mv_remote_update_start(request_options=request_options)
        return _response.data

    async def get_mv_remote_update_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Example: http://10.10.10.254/httpapi.asp?command=getMvRemoteUpdateStatus

        Get the download progress.

        Value    Meaning
        - 10    Under review
        - 20  OK
        - 21    The verification of the downloaded update file failed
        - 22    Downloading the update file failed
        - 23    The verification of the downloaded update file failed
        - 25    Start downloading
        - 27    Download complete
        - 30    Downloading and verification completed

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_mv_remote_update_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mv_remote_update_status(request_options=request_options)
        return _response.data

    async def get_mv_rom_burn_precent(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMvRomBurnPrecentResponse:
        """
        Example: http://10.10.10.254/httpapi.asp?command=getMvRomBurnPrecent

        Status of updating

        Returns: { "status" : "0", "progress" : "50"}

        | Fields     | Meaning |
        | ---------|---------|
        | status     | State   |
        | progress | Progress between 0 to 100% |

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMvRomBurnPrecentResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_mv_rom_burn_precent()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mv_rom_burn_precent(request_options=request_options)
        return _response.data

    async def easy_link_response_stop(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.easy_link_response_stop()


        asyncio.run(main())
        """
        _response = await self._raw_client.easy_link_response_stop(request_options=request_options)
        return _response.data

    async def notify_upgrade_type_firmware(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.notify_upgrade_type_firmware()


        asyncio.run(main())
        """
        _response = await self._raw_client.notify_upgrade_type_firmware(request_options=request_options)
        return _response.data

    async def get_lmp_filter_capability(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetLmpFilterCapabilityResponse:
        """
        ...

        Returns: { "version": "1.1" }

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLmpFilterCapabilityResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_lmp_filter_capability()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_lmp_filter_capability(request_options=request_options)
        return _response.data

    async def get_stream_service_config(
        self, source: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        source : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_stream_service_config(
                source="source",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_stream_service_config(source, request_options=request_options)
        return _response.data

    async def set_handshake_code(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_handshake_code(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_handshake_code(str, request_options=request_options)
        return _response.data

    async def getsyslog_ip(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.getsyslog_ip(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getsyslog_ip(str, request_options=request_options)
        return _response.data

    async def get_status_ip(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_status_ip(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_status_ip(str, request_options=request_options)
        return _response.data

    async def get_update_server(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_update_server()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_update_server(request_options=request_options)
        return _response.data

    async def get_weather_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_weather_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_weather_info(request_options=request_options)
        return _response.data

    async def set_access_pin(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_access_pin(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_access_pin(str, request_options=request_options)
        return _response.data

    async def set_language(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_language(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_language(str, request_options=request_options)
        return _response.data

    async def auto_play_set(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.auto_play_set()


        asyncio.run(main())
        """
        _response = await self._raw_client.auto_play_set(request_options=request_options)
        return _response.data

    async def get_mv_rom_download_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMvRomDownloadStatusResponse:
        """
        ...

        Returns: {"status":"0","count":"0","dcount":"0","wcount":"0","tsize":"0","dsize":"0","wsize":"0","csize":"0", "cdsize":"0", "cwsize":"0", "progress":"0","name":"","ver":"0","new_ver":"0"}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMvRomDownloadStatusResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_mv_rom_download_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mv_rom_download_status(request_options=request_options)
        return _response.data

    async def get_mv_rom_download_v2status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMvRomDownloadV2StatusResponse:
        """
        ...

        Returns: {"status":"0","progress":"0","name":"","ver":"0","new_ver":"0"}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMvRomDownloadV2StatusResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_mv_rom_download_v2status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mv_rom_download_v2status(request_options=request_options)
        return _response.data

    async def set_hex_group_name(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_hex_group_name(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_hex_group_name(str, request_options=request_options)
        return _response.data

    async def set_mv_remote_silence_ota_time(
        self, str: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_mv_remote_silence_ota_time(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_mv_remote_silence_ota_time(str, request_options=request_options)
        return _response.data

    async def set_mv_remote_silence_update_time(
        self, str: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_mv_remote_silence_update_time(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_mv_remote_silence_update_time(str, request_options=request_options)
        return _response.data

    async def set_timezone(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_timezone(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_timezone(str, request_options=request_options)
        return _response.data

    async def check_access_pin(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.check_access_pin()


        asyncio.run(main())
        """
        _response = await self._raw_client.check_access_pin(request_options=request_options)
        return _response.data

    async def set_update_server(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_update_server(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_update_server(str, request_options=request_options)
        return _response.data

    async def set_weather_location(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_weather_location(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_weather_location(str, request_options=request_options)
        return _response.data

    async def start_check(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.start_check()


        asyncio.run(main())
        """
        _response = await self._raw_client.start_check(request_options=request_options)
        return _response.data

    async def getbatteryval(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.getbatteryval()


        asyncio.run(main())
        """
        _response = await self._raw_client.getbatteryval(request_options=request_options)
        return _response.data

    async def get_asr_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetAsrStatusResponse:
        """
        ...

        Returns: { "times_talk_on": "0", "times_request_succeed": "0", "times_request_failed": "0", "times_vad_time_out": "0", "times_play_failed": "0", "open_failed": "0", "capture_failed": "0", "mode": "normal", "score": "0", "volume": "18", "play_status": "0", "config_score": "0", "config_interval": "0", "trigger_test_mode": "0", "trigger_mis_test_mode": "0", "trigger_recording": "0", "have_prompt": "0", "fallback_enable": "0", "profile": "near", "hands_free": "0", "status": "ok", "id": "0" }

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAsrStatusResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_asr_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_asr_status(request_options=request_options)
        return _response.data

    async def get_lp_auth_code(
        self, str: str, str2: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        str2 : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_lp_auth_code(
                str="str",
                str2="str2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_lp_auth_code(str, str2, request_options=request_options)
        return _response.data

    async def set_token_params(
        self, str: str, str2: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        str2 : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_token_params(
                str="str",
                str2="str2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_token_params(str, str2, request_options=request_options)
        return _response.data

    async def talkset_prompt(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.talkset_prompt(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.talkset_prompt(n, request_options=request_options)
        return _response.data

    async def talkset_alarm_pre_wake(
        self, str: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.talkset_alarm_pre_wake(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.talkset_alarm_pre_wake(str, request_options=request_options)
        return _response.data

    async def talkset_alarm_tone(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.talkset_alarm_tone(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.talkset_alarm_tone(n, request_options=request_options)
        return _response.data

    async def talkset_alarm_tone_preview(
        self, n: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.talkset_alarm_tone_preview(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.talkset_alarm_tone_preview(n, request_options=request_options)
        return _response.data

    async def talkset_alarm_volume(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.talkset_alarm_volume(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.talkset_alarm_volume(n, request_options=request_options)
        return _response.data

    async def talkset_alarmcommon(
        self, str: str, n1: int, n2: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        n1 : int
            Unknown

        n2 : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.talkset_alarmcommon(
                str="str",
                n1=1,
                n2=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.talkset_alarmcommon(str, n1, n2, request_options=request_options)
        return _response.data

    async def set_sync_play_extra_delay(
        self, n: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_sync_play_extra_delay(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_sync_play_extra_delay(n, request_options=request_options)
        return _response.data

    async def set_initial_configuration(
        self, n: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_initial_configuration(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_initial_configuration(n, request_options=request_options)
        return _response.data

    async def get_ui_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_ui_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_ui_config(request_options=request_options)
        return _response.data

    async def get_spdif_auto_sense_enable(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_spdif_auto_sense_enable()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_spdif_auto_sense_enable(request_options=request_options)
        return _response.data

    async def get_spdif_in_noise_remove(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_spdif_in_noise_remove()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_spdif_in_noise_remove(request_options=request_options)
        return _response.data

    async def phono_mode_switch_set(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.phono_mode_switch_set(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.phono_mode_switch_set(str, request_options=request_options)
        return _response.data

    async def set_play_mode_volume_enable(
        self, str: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_play_mode_volume_enable(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_play_mode_volume_enable(str, request_options=request_options)
        return _response.data

    async def get_ui_wallpaper_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_ui_wallpaper_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_ui_wallpaper_list(request_options=request_options)
        return _response.data

    async def set_play_mode_volume_value(
        self, str: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_play_mode_volume_value(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_play_mode_volume_value(str, request_options=request_options)
        return _response.data

    async def set_power_mode_time(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_power_mode_time(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_power_mode_time(str, request_options=request_options)
        return _response.data

    async def get_button_volume_step(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetButtonVolumeStepResponse:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=get_button_volume_step

        Returns: {"status":"OK","button_volume_step":2}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetButtonVolumeStepResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_button_volume_step()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_button_volume_step(request_options=request_options)
        return _response.data

    async def set_button_volume_step(
        self, str: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi.asp?command=set_button_volume_step:{str}

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_button_volume_step(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_button_volume_step(str, request_options=request_options)
        return _response.data

    async def get_aux_auto_sense_enable(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: 0 or 1, where 0 means AUX auto-sense is disabled and 1 means AUX auto-sense is enabled

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_aux_auto_sense_enable()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_aux_auto_sense_enable(request_options=request_options)
        return _response.data

    async def set_ui_config(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_ui_config(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_ui_config(str, request_options=request_options)
        return _response.data

    async def set_spdif_auto_sense_enable(
        self, n: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_spdif_auto_sense_enable(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_spdif_auto_sense_enable(n, request_options=request_options)
        return _response.data

    async def set_spdif_in_noise_remove(
        self, str: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_spdif_in_noise_remove(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_spdif_in_noise_remove(str, request_options=request_options)
        return _response.data

    async def get_channel_mode(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns an integer representing the current channel mode. The meaning of the values is currently unknown.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_channel_mode()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_channel_mode(request_options=request_options)
        return _response.data

    async def get_auto_sense_enable(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: 0 or 1, where 0 means auto-sense is disabled and 1 means auto-sense is enabled

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_auto_sense_enable()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_auto_sense_enable(request_options=request_options)
        return _response.data

    async def start_reboot_time(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.start_reboot_time()


        asyncio.run(main())
        """
        _response = await self._raw_client.start_reboot_time(request_options=request_options)
        return _response.data

    async def led_switch_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.led_switch_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.led_switch_get(request_options=request_options)
        return _response.data

    async def get_mqa_receiver_cap(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: 0 or 1, where 0 means MQA is not supported and 1 means MQA is supported

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_mqa_receiver_cap()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mqa_receiver_cap(request_options=request_options)
        return _response.data

    async def reload_button_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.reload_button_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.reload_button_get(request_options=request_options)
        return _response.data

    async def set_aux_auto_sense_enable(
        self, n: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_aux_auto_sense_enable(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_aux_auto_sense_enable(n, request_options=request_options)
        return _response.data

    async def get_low_priority_prompt_disable(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: 0 or 1, where 0 means low priority prompts are enabled and 1 means low priority prompts are disabled

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_low_priority_prompt_disable()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_low_priority_prompt_disable(request_options=request_options)
        return _response.data

    async def get_soft_mute(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_soft_mute()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_soft_mute(request_options=request_options)
        return _response.data

    async def get_line_in_max_cap(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: 48000:16:0, which means a maximum sampling rate of 48000 Hz, a maximum bit depth of 16 bits, and a maximum channel count of 0 (unknown)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_line_in_max_cap()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_line_in_max_cap(request_options=request_options)
        return _response.data

    async def get_aux_in_max_cap(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: 48000:16:0, which means a maximum sampling rate of 48000 Hz, a maximum bit depth of 16 bits, and a maximum channel count of 0 (unknown)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_aux_in_max_cap()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_aux_in_max_cap(request_options=request_options)
        return _response.data

    async def get_uac_out_max_cap(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_uac_out_max_cap()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_uac_out_max_cap(request_options=request_options)
        return _response.data

    async def get_hdmi_auto_sense_enable(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: 0 or 1, where 0 means HDMI auto-sense is disabled and 1 means HDMI auto-sense is enabled

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_hdmi_auto_sense_enable()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_hdmi_auto_sense_enable(request_options=request_options)
        return _response.data

    async def set_channel_mode(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_channel_mode(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_channel_mode(n, request_options=request_options)
        return _response.data

    async def get_sync_play_extra_delay(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_sync_play_extra_delay()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sync_play_extra_delay(request_options=request_options)
        return _response.data

    async def get_light_operation_bright_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_light_operation_bright_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_light_operation_bright_config(request_options=request_options)
        return _response.data

    async def set_ui_wallpaper_list(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_ui_wallpaper_list(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_ui_wallpaper_list(str, request_options=request_options)
        return _response.data

    async def get_main_sub_extra_delay(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMainSubExtraDelayResponse:
        """
        ...

        Returns, without Subwoofer attached: {"category": "mainsubdelay", "body": {"errorType": "-1000", "mainSubExtraDelay": "-1000.000", "mainDelay": "-1000.000", "subDelay": "-1000.000", "errorDescribe": "unknow error"}}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMainSubExtraDelayResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_main_sub_extra_delay()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_main_sub_extra_delay(request_options=request_options)
        return _response.data

    async def cast_disable(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.cast_disable()


        asyncio.run(main())
        """
        _response = await self._raw_client.cast_disable(request_options=request_options)
        return _response.data

    async def cast_disable_usage_report(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.cast_disable_usage_report()


        asyncio.run(main())
        """
        _response = await self._raw_client.cast_disable_usage_report(request_options=request_options)
        return _response.data

    async def set_auto_sense_enable(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_auto_sense_enable(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_auto_sense_enable(str, request_options=request_options)
        return _response.data

    async def phono_mode_switch_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.phono_mode_switch_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.phono_mode_switch_get(request_options=request_options)
        return _response.data

    async def get_play_mode_volume_enable(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_play_mode_volume_enable()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_play_mode_volume_enable(request_options=request_options)
        return _response.data

    async def set_volume_control(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_volume_control(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_volume_control(n, request_options=request_options)
        return _response.data

    async def get_play_mode_volume_value(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_play_mode_volume_value()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_play_mode_volume_value(request_options=request_options)
        return _response.data

    async def set_mqa_receiver_cap(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_mqa_receiver_cap(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_mqa_receiver_cap(str, request_options=request_options)
        return _response.data

    async def get_power_mode_time(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_power_mode_time()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_power_mode_time(request_options=request_options)
        return _response.data

    async def set_max_volume(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_max_volume(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_max_volume(n, request_options=request_options)
        return _response.data

    async def enable_cast(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.enable_cast()


        asyncio.run(main())
        """
        _response = await self._raw_client.enable_cast(request_options=request_options)
        return _response.data

    async def reload_button_update(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.reload_button_update(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reload_button_update(str, request_options=request_options)
        return _response.data

    async def enable_cast_usage_report(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.enable_cast_usage_report()


        asyncio.run(main())
        """
        _response = await self._raw_client.enable_cast_usage_report(request_options=request_options)
        return _response.data

    async def disable_low_priority_prompt(
        self, str: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.disable_low_priority_prompt(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disable_low_priority_prompt(str, request_options=request_options)
        return _response.data

    async def set_soft_mute(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_soft_mute(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_soft_mute(str, request_options=request_options)
        return _response.data

    async def set_hdmi_auto_sense_enable(
        self, n: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_hdmi_auto_sense_enable(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_hdmi_auto_sense_enable(n, request_options=request_options)
        return _response.data

    async def set_spdif_out_max_cap(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_spdif_out_max_cap(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_spdif_out_max_cap(str, request_options=request_options)
        return _response.data

    async def set_coax_out_max_cap(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_coax_out_max_cap(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_coax_out_max_cap(str, request_options=request_options)
        return _response.data

    async def set_line_in_max_cap(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_line_in_max_cap(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_line_in_max_cap(str, request_options=request_options)
        return _response.data

    async def set_aux_in_max_cap(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_aux_in_max_cap(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_aux_in_max_cap(str, request_options=request_options)
        return _response.data

    async def set_uac_out_max_cap(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_uac_out_max_cap(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_uac_out_max_cap(str, request_options=request_options)
        return _response.data

    async def enable_sys_info(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.enable_sys_info(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enable_sys_info(n, request_options=request_options)
        return _response.data

    async def get_airplay_extra_delay(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAirplayExtraDelayResponse:
        """
        Makes a call to https://10.10.10.254/httpapi?command=GetAirplayExtraDelay

        Returns: {"AirplayExtraDelay":-10}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAirplayExtraDelayResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_airplay_extra_delay()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_airplay_extra_delay(request_options=request_options)
        return _response.data

    async def get_current_wireless_connect(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Makes a call to https://10.10.10.254/httpapi?command=GetCurrentWirelessConnect

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_current_wireless_connect()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_current_wireless_connect(request_options=request_options)
        return _response.data

    async def slave_alert_get(self, ip: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        ip : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.slave_alert_get(
                ip="ip",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slave_alert_get(ip, request_options=request_options)
        return _response.data

    async def slave_talk_set_alarm_volume(
        self, ip: str, n: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        ip : str
            Unknown

        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.slave_talk_set_alarm_volume(
                ip="ip",
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slave_talk_set_alarm_volume(ip, n, request_options=request_options)
        return _response.data

    async def squeezelite_auto_connect_enable(
        self, n: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.squeezelite_auto_connect_enable(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.squeezelite_auto_connect_enable(n, request_options=request_options)
        return _response.data

    async def squeezelite_connect_server(
        self, ip: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        ip : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.squeezelite_connect_server(
                ip="ip",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.squeezelite_connect_server(ip, request_options=request_options)
        return _response.data

    async def squeezelite_discover(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.squeezelite_discover()


        asyncio.run(main())
        """
        _response = await self._raw_client.squeezelite_discover(request_options=request_options)
        return _response.data

    async def squeezelite_get_state(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.squeezelite_get_state()


        asyncio.run(main())
        """
        _response = await self._raw_client.squeezelite_get_state(request_options=request_options)
        return _response.data

    async def get_setup_router_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_setup_router_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_setup_router_info(request_options=request_options)
        return _response.data

    async def set_setup_router_info(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_setup_router_info(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_setup_router_info(str, request_options=request_options)
        return _response.data

    async def alert_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.alert_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.alert_get(request_options=request_options)
        return _response.data

    async def tvs_logout(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.tvs_logout()


        asyncio.run(main())
        """
        _response = await self._raw_client.tvs_logout(request_options=request_options)
        return _response.data

    async def get_tvs_state(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_tvs_state()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tvs_state(request_options=request_options)
        return _response.data

    async def get_tvs_dev_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_tvs_dev_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_tvs_dev_info(request_options=request_options)
        return _response.data

    async def set_tvs_access_token(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_tvs_access_token(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_tvs_access_token(str, request_options=request_options)
        return _response.data

    async def set_tvs_debug_mode(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_tvs_debug_mode(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_tvs_debug_mode(str, request_options=request_options)
        return _response.data

    async def set_tvs_client_id(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_tvs_client_id(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_tvs_client_id(str, request_options=request_options)
        return _response.data

    async def create_routine(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.create_routine(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_routine(str, request_options=request_options)
        return _response.data

    async def get_all_routines(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAllRoutinesResponse:
        """
        ...

        Returns: { "routines": [ { "updateDate": "2025-10-12T12:03:48Z", "steps": [ { "type": "subwoofer", "payload": { "subOutput": 0 } }, { "type": "loopMode", "payload": { "mode": 3 } } ], "createDate": "2025-10-12T12:03:48Z", "id": "E59E781B-CE00-4347-9E5B-A82F47C675AC", "name": "Spotify Liked", "index": 1 } ] }

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAllRoutinesResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_all_routines()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_routines(request_options=request_options)
        return _response.data

    async def get_routine_capability(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetRoutineCapabilityResponse:
        """
        ...

        Returns: { "version": "1.1" }

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetRoutineCapabilityResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_routine_capability()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_routine_capability(request_options=request_options)
        return _response.data

    async def get_audio_input_capability(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAudioInputCapabilityResponse:
        """
        ...

        Returns: { "ver": "1.0", "audioInput": [ { "mode": "wifi" }, { "mode": "line-in" }, { "mode": "bluetooth" }, { "mode": "optical" }, { "mode": "HDMI" } ] }

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAudioInputCapabilityResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_audio_input_capability()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_audio_input_capability(request_options=request_options)
        return _response.data

    async def get_audio_out_max32bit(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAudioOutMax32BitResponse:
        """
        ...

        Returns: 0 or 1

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAudioOutMax32BitResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_audio_out_max32bit()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_audio_out_max32bit(request_options=request_options)
        return _response.data

    async def set_audio_out_max32bit(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        n: 0 or 1

        Parameters
        ----------
        n : int
            The desired audio output maximum 32-bit support (0 or 1)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_audio_out_max32bit(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_audio_out_max32bit(n, request_options=request_options)
        return _response.data

    async def get_audio_output_vrms(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown (possibly the output type or identifier)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_audio_output_vrms(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_audio_output_vrms(str, request_options=request_options)
        return _response.data

    async def get_audio_output_vrms_support_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_audio_output_vrms_support_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_audio_output_vrms_support_list(request_options=request_options)
        return _response.data

    async def set_audio_output_vrms(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown (possibly the output type or identifier)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_audio_output_vrms(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_audio_output_vrms(str, request_options=request_options)
        return _response.data

    async def get_cbl_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_cbl_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cbl_status(request_options=request_options)
        return _response.data

    async def get_cec_power_ctrl(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        ...

        Returns: 0 or 1

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_cec_power_ctrl()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cec_power_ctrl(request_options=request_options)
        return _response.data

    async def set_cec_power_ctrl(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        n: 0 or 1

        Parameters
        ----------
        n : int
            The desired CEC power control status (0 or 1)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_cec_power_ctrl(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_cec_power_ctrl(n, request_options=request_options)
        return _response.data

    async def get_cxdish_precent(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCxdishPrecentResponse:
        """
        ...

        Returns: {"status":"0","progress":"0"}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCxdishPrecentResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_cxdish_precent()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cxdish_precent(request_options=request_options)
        return _response.data

    async def get_digital_filter_type_support_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDigitalFilterTypeSupportListResponse:
        """
        ...

        Returns: [ { "index": 1, "args": [ "amixer cset name='ES9018 DigiFilt' 0" ], "value": "Fast Roll-Off" }, { "index": 2, "args": [ "amixer cset name='ES9018 DigiFilt' 1" ], "value": "Slow Roll-Off" }, { "index": 3, "args": [ "amixer cset name='ES9018 DigiFilt' 2" ], "value": "Minimum Phase" } ]

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDigitalFilterTypeSupportListResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_digital_filter_type_support_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_digital_filter_type_support_list(request_options=request_options)
        return _response.data

    async def get_digital_filter_type(self, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        ...

        Returns: 1, 2, or 3 corresponding to the supported digital filter types

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_digital_filter_type()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_digital_filter_type(request_options=request_options)
        return _response.data

    async def set_digital_filter_type(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            The digital filter type to set (1, 2, or 3)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_digital_filter_type(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_digital_filter_type(n, request_options=request_options)
        return _response.data

    async def get_output_digital_filter_type(
        self, str: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown (possibly the output type or identifier)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_output_digital_filter_type(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_output_digital_filter_type(str, request_options=request_options)
        return _response.data

    async def get_output_digital_filter_type_support_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_output_digital_filter_type_support_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_output_digital_filter_type_support_list(request_options=request_options)
        return _response.data

    async def set_output_digital_filter_type(
        self, str: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown (possibly the output type or identifier)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_output_digital_filter_type(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_output_digital_filter_type(str, request_options=request_options)
        return _response.data

    async def get_digital_input_audio_type_support(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        ...

        Returns: 0x1

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_digital_input_audio_type_support()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_digital_input_audio_type_support(request_options=request_options)
        return _response.data

    async def get_output_voltage(self, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        ...

        Returns an integer

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_output_voltage()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_output_voltage(request_options=request_options)
        return _response.data

    async def set_output_voltage(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        n : int
            The desired output voltage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_output_voltage(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_output_voltage(n, request_options=request_options)
        return _response.data

    async def get_feature_capability(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_feature_capability()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_feature_capability(request_options=request_options)
        return _response.data

    async def get_play_mode_gain_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_play_mode_gain_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_play_mode_gain_config(request_options=request_options)
        return _response.data

    async def set_play_mode_gain_config(
        self, str: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_play_mode_gain_config(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_play_mode_gain_config(str, request_options=request_options)
        return _response.data

    async def mediaserver_scan(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.mediaserver_scan()


        asyncio.run(main())
        """
        _response = await self._raw_client.mediaserver_scan(request_options=request_options)
        return _response.data

    async def mediaserver_udiskumount(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.mediaserver_udiskumount()


        asyncio.run(main())
        """
        _response = await self._raw_client.mediaserver_udiskumount(request_options=request_options)
        return _response.data

    async def get_input_mode_support_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_input_mode_support_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_input_mode_support_list(request_options=request_options)
        return _response.data

    async def get_mode_rename(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        ...

        Returns: {"Line-In" : "", "SPDIF-In" : "PC"}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_mode_rename()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mode_rename(request_options=request_options)
        return _response.data

    async def set_mode_rename(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            Unknown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_mode_rename(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_mode_rename(str, request_options=request_options)
        return _response.data

    async def set_music_explicit(self, n: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        n: 0 or 1

        Parameters
        ----------
        n : int
            The desired music explicit content filter status (0 or 1)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_music_explicit(
                n=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_music_explicit(n, request_options=request_options)
        return _response.data

    async def get_mv_remote_update_device_ota_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetMvRemoteUpdateDeviceOtaInfoResponse:
        """
        ...

        Returns: {"language":"en_us","projectId":"0fb639765679eb9a7cf7d68761e2d71b6a2d62ea47cc049db3c7df61d6816fc9","fwVersion":"Linkplay.5.0.739659","version":"1.0","macAddr":"E8:2D:29:7C:45:40","serialNumber":"","deviceUid":"FA98F353DDFE707499E52529","imgList":[{"imgName":"hdmi","imgVersion":"71"},{"imgName":"moduleMulti","imgVersion":"Linkplay.5.0.739659"},{"imgName":"gc4a_zip","imgVersion":"Linkplay.5.0.739659"}]}

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetMvRemoteUpdateDeviceOtaInfoResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.get_mv_remote_update_device_ota_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mv_remote_update_device_ota_info(request_options=request_options)
        return _response.data

    async def set_tunein_favorite_state(
        self, song_id: str, status: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        songId: The ID of the song
        status: 0 for not favorite, 1 for favorite

        Parameters
        ----------
        song_id : str
            The ID of the song

        status : int
            0 for not favorite, 1 for favorite

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_tunein_favorite_state(
                song_id="songId",
                status=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_tunein_favorite_state(song_id, status, request_options=request_options)
        return _response.data

    async def set_tunein_location(
        self, latitude: str, longitude: str, serial: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        ...

        latitude: Latitude of the location
        longitude: Longitude of the location
        serial: Device serial number

        Parameters
        ----------
        latitude : str
            Latitude of the location

        longitude : str
            Longitude of the location

        serial : str
            Device serial number

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_tunein_location(
                latitude="latitude",
                longitude="longitude",
                serial="serial",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_tunein_location(
            latitude, longitude, serial, request_options=request_options
        )
        return _response.data

    async def set_tunein_token(
        self,
        username: str,
        token: str,
        refresh_token: str,
        expires_in: int,
        userid: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        ...

        username: TuneIn account username
        token: Authentication token
        refreshToken: Token used to refresh the authentication token
        expires_in: Time in seconds until the token expires
        userid: TuneIn user ID

        Parameters
        ----------
        username : str
            TuneIn account username

        token : str
            Authentication token

        refresh_token : str
            Token used to refresh the authentication token

        expires_in : int
            Time in seconds until the token expires

        userid : str
            TuneIn user ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.set_tunein_token(
                username="username",
                token="token",
                refresh_token="refreshToken",
                expires_in=1,
                userid="userid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_tunein_token(
            username, token, refresh_token, expires_in, userid, request_options=request_options
        )
        return _response.data

    async def stream_services_capability(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StreamServicesCapabilityResponse:
        """
        ...

        Returns: { "version": "1.6", "encrypt": "1.0", "streamServices": [ { "id": "Prime", "version": "1.4", "quality": [ "SD", "HD", "UHD" ] }, { ... } ] }

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StreamServicesCapabilityResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.stream_services_capability()


        asyncio.run(main())
        """
        _response = await self._raw_client.stream_services_capability(request_options=request_options)
        return _response.data

    async def tidal_login(self, str: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        ...

        Parameters
        ----------
        str : str
            The OAuth code obtained from Tidal authentication flow

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.other.tidal_login(
                str="str",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tidal_login(str, request_options=request_options)
        return _response.data
