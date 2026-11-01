

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DeviceStatus(UniversalBaseModel):
    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    The device language
    """

    ssid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the device. Device's own SSID when in WiFi pairing
    mode or when device's WiFi hotspot is active
    """

    hide_ssid: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="hideSSID"),
        pydantic.Field(
            alias="hideSSID",
            description="When the device is operating as a WiFi hotspot, this flag\ndetermines whether its SSID should be hidden or visible 0:\nssid is visible 1: ssid is hidden",
        ),
    ] = None
    """
    When the device is operating as a WiFi hotspot, this flag
    determines whether its SSID should be hidden or visible 0:
    ssid is visible 1: ssid is hidden
    """

    ssid_strategy: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="SSIDStrategy"), pydantic.Field(alias="SSIDStrategy")
    ] = None
    branch: typing.Optional[str] = pydantic.Field(default=None)
    """
    Code branch
    """

    firmware: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current firmware version
    """

    build: typing.Optional[str] = pydantic.Field(default=None)
    """
    Possible values: release, debug, backup release: this is a
    release version debug: this is a debug version backup:
    this is a backup version
    """

    project: typing.Optional[str] = pydantic.Field(default=None)
    """
    The project name
    """

    priv_prj: typing.Optional[str] = pydantic.Field(default=None)
    """
    Project name which would stand for a specific board
    """

    project_build_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Code identifier for customized release
    """

    release: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Release"),
        pydantic.Field(alias="Release", description="Firmware build date Format: YYYYMMDD"),
    ] = None
    """
    Firmware build date Format: YYYYMMDD
    """

    fw_release_version: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="FW_Release_version"),
        pydantic.Field(alias="FW_Release_version", description="Reserved"),
    ] = None
    """
    Reserved
    """

    pcb_version: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PCB_version"),
        pydantic.Field(alias="PCB_version", description="PCB version/revision"),
    ] = None
    """
    PCB version/revision
    """

    cast_enable: typing.Optional[int] = pydantic.Field(default=None)
    """
    Flag for casting feature 0: casting is disabled 1: casting
    is enabled
    """

    cast_usage_report: typing.Optional[int] = pydantic.Field(default=None)
    """
    Reserved
    """

    group: typing.Optional[str] = pydantic.Field(default=None)
    """
    0 means it's a master speaker or standalone,  1 means a
    slave speaker in group
    """

    master_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Exist when working in slave mode, showing the UUID of
    master device.
    """

    slave_mask: typing.Optional[str] = pydantic.Field(default=None)
    """
    Exist when working in slave mode, showing if the device
    support mask feature. 0 means not supported.
    """

    wmrm_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    LinkPlay's MRM SDK version, Multiroom library version,
    version 4.2 or above won't work with any version below 4.2
    """

    wmrm_sub_ver: typing.Optional[str] = pydantic.Field(default=None)
    """
    Multiroom library sub version
    """

    expired: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reserved
    """

    internet: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current status of internet access: 0: not ready 1: ready
    """

    uuid_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="uuid"),
        pydantic.Field(alias="uuid", description="The unique ID of the device (will remain after device\nreboot)"),
    ] = None
    """
    The unique ID of the device (will remain after device
    reboot)
    """

    mac: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="MAC"),
        pydantic.Field(
            alias="MAC",
            description="MAC address of the device when working in hotspot mode,\nwill show on APP and also the sticker on module/device.",
        ),
    ] = None
    """
    MAC address of the device when working in hotspot mode,
    will show on APP and also the sticker on module/device.
    """

    sta_mac: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="STA_MAC"),
        pydantic.Field(alias="STA_MAC", description="MAC address of the device when working in station mode"),
    ] = None
    """
    MAC address of the device when working in station mode
    """

    bt_mac: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="BT_MAC"),
        pydantic.Field(alias="BT_MAC", description="The BT MAC address of the device"),
    ] = None
    """
    The BT MAC address of the device
    """

    ap_mac: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AP_MAC"),
        pydantic.Field(alias="AP_MAC", description="The MAC address of the AP that the device is connected to"),
    ] = None
    """
    The MAC address of the AP that the device is connected to
    """

    eth_mac: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ETH_MAC"),
        pydantic.Field(alias="ETH_MAC", description="The MAC address of the device when it's connected to\nethernet"),
    ] = None
    """
    The MAC address of the device when it's connected to
    ethernet
    """

    initial_configuration: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="InitialConfiguration"),
        pydantic.Field(
            alias="InitialConfiguration", description="Flag for initial configuration 0: not configured 1:\nconfigured"
        ),
    ] = None
    """
    Flag for initial configuration 0: not configured 1:
    configured
    """

    temperature_power_control: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reserved
    """

    temperature_cpu: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reserved
    """

    temperature_tmp102: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reserved
    """

    country_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CountryCode"),
        pydantic.Field(alias="CountryCode", description="The country code"),
    ] = None
    """
    The country code
    """

    country_region: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CountryRegion"),
        pydantic.Field(alias="CountryRegion", description="The country region"),
    ] = None
    """
    The country region
    """

    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current Date
    """

    time: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current local time
    """

    tz: typing.Optional[str] = pydantic.Field(default=None)
    """
    Timezone offset
    """

    dst_enable: typing.Optional[str] = pydantic.Field(default=None)
    """
    Daylight saving time enable
    """

    netstat: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current WiFi status: 0: no network 1: connected to the
    internet 2: connected to the local network
    """

    essid: typing.Optional[str] = pydantic.Field(default=None)
    """
    SSID of the WiFi the device is connected to in HEX format
    """

    apcli0: typing.Optional[str] = pydantic.Field(default=None)
    """
    The IP v4 address of the device over WiFi
    """

    eth0: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device's IP address when it's connected to ethernet
    """

    eth2: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device's IP address when it's connected to ethernet
    """

    eth_dhcp: typing.Optional[str] = pydantic.Field(default=None)
    """
    Flag for DHCP or Static IP Address 0: Static IP 1: IP
    Address provided by LAN/WLAN DHCP Server
    """

    eth_static_ip: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device's Static IP address (If eth_dhcp=0)
    """

    eth_static_mask: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device's Network Mask (If eth_dhcp=0)
    """

    eth_static_gateway: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device's IP Gateway (If eth_dhcp=0)
    """

    eth_static_dns1: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device's Primary DNS Server (If eth_dhcp=0)
    """

    eth_static_dns2: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device's Secondary DNS Server (If eth_dhcp=0)
    """

    hardware: typing.Optional[str] = pydantic.Field(default=None)
    """
    Hardware model
    """

    version_update: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="VersionUpdate"),
        pydantic.Field(
            alias="VersionUpdate",
            description="Flag that determines, if there is a new firmware version\navailable or not. 0: no new firmware 1: new firmware\navailable",
        ),
    ] = None
    """
    Flag that determines, if there is a new firmware version
    available or not. 0: no new firmware 1: new firmware
    available
    """

    new_ver: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="NewVer"),
        pydantic.Field(
            alias="NewVer",
            description="If there is a new firmware available (in case of\nVersionUpdate is set to 1), this is the new version number",
        ),
    ] = None
    """
    If there is a new firmware available (in case of
    VersionUpdate is set to 1), this is the new version number
    """

    mcu_ver: typing.Optional[str] = pydantic.Field(default=None)
    """
    Version of MCU on base board
    """

    mcu_ver_new: typing.Optional[str] = pydantic.Field(default=None)
    """
    New version of MCU on base board, indicates if there is a
    newer version of MCU available 0 - No new version others -
    New version
    """

    hdmi_ver: typing.Optional[str] = pydantic.Field(default=None)
    """
    HDMI version
    """

    hdmi_ver_new: typing.Optional[str] = pydantic.Field(default=None)
    """
    New HDMI version
    """

    update_check_count: typing.Optional[str] = None
    ble_remote_update_checked_counter: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="BleRemote_update_checked_counter"),
        pydantic.Field(alias="BleRemote_update_checked_counter"),
    ] = None
    ra0: typing.Optional[str] = pydantic.Field(default=None)
    """
    WiFi AP IP address, normally it is 10.10.10.254
    """

    temp_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Temporary UUID (will change after device reboot)
    """

    cap1: typing.Optional[str] = pydantic.Field(default=None)
    """
    Bit mask for the module feature, used internally
    """

    capability: typing.Optional[str] = pydantic.Field(default=None)
    """
    Bit mask for the module feature, used internally
    """

    languages: typing.Optional[str] = pydantic.Field(default=None)
    """
    Supported languages, bit mask
    """

    prompt_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates if the prompting voice would be played or not,
    you can set with command PromptEnable and PromptDisable. 0
    - No prompting voice 1 - Have prompting voice
    """

    iot_ver: typing.Optional[str] = pydantic.Field(default=None)
    """
    IOT library version, not used
    """

    alexa_ver: typing.Optional[str] = None
    alexa_beta_enable: typing.Optional[str] = None
    alexa_force_beta_cfg: typing.Optional[str] = None
    dsp_ver: typing.Optional[str] = pydantic.Field(default=None)
    """
    Version for voice processing, not used
    """

    dsp_ver_new: typing.Optional[str] = pydantic.Field(default=None)
    """
    New version for voice processing, not used
    """

    module_color_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ModuleColorNumber"),
        pydantic.Field(alias="ModuleColorNumber", description="Reserved"),
    ] = None
    """
    Reserved
    """

    module_color_string: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ModuleColorString"),
        pydantic.Field(alias="ModuleColorString", description="Reserved"),
    ] = None
    """
    Reserved
    """

    uboot_verinfo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Uboot version
    """

    streams_all: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reserved
    """

    streams: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is a bit mask: 0: If Airplay is enabled 1: If DLNA is
    enabled 2: Has TTPod support 3: Has TuneIn support 4: Has
    Pandora support 5: Has DoubanFM support
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reserved
    """

    volume_control: typing.Optional[str] = None
    external: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reserved (hex value)
    """

    preset_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    Amount of preset keys available
    """

    spotify_active: typing.Optional[str] = pydantic.Field(default=None)
    """
    Spotify status 0: Spotify is not playing 1: Spotify is
    playing
    """

    plm_support: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is a bit mask, each bit stands for an external input
    source: bit1: LineIn (Aux support) bit2: Bluetooth support
    bit3: USB support bit4: Optical support bit6: Coaxial
    support bit8: LineIn 2 support bit15: USBDAC support
    Others are reserved or not used.
    """

    mqtt_support: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reserved
    """

    lbc_support: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reserved
    """

    wifi_channel: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="WifiChannel"),
        pydantic.Field(alias="WifiChannel", description="The current connected WiFi channel"),
    ] = None
    """
    The current connected WiFi channel
    """

    rssi: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="RSSI"),
        pydantic.Field(
            alias="RSSI",
            description="RSSI Level of used WiFi Value ranges from 0 - 100. 100\nmeans best signal strength.",
        ),
    ] = None
    """
    RSSI Level of used WiFi Value ranges from 0 - 100. 100
    means best signal strength.
    """

    bssid: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="BSSID"),
        pydantic.Field(
            alias="BSSID",
            description="The Basic Service Set Identifiers:  In most cases this\nwill be the MAC Address of the Wireless Acces Point Used\n(e.g. Router)",
        ),
    ] = None
    """
    The Basic Service Set Identifiers:  In most cases this
    will be the MAC Address of the Wireless Acces Point Used
    (e.g. Router)
    """

    wlan_snr: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="wlanSnr"),
        pydantic.Field(alias="wlanSnr", description="Signal to Noise Ratio of the WiFi connection"),
    ] = None
    """
    Signal to Noise Ratio of the WiFi connection
    """

    wlan_noise: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="wlanNoise"),
        pydantic.Field(alias="wlanNoise", description="Noise level of the WiFi connection"),
    ] = None
    """
    Noise level of the WiFi connection
    """

    wlan_freq: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="wlanFreq"), pydantic.Field(alias="wlanFreq")
    ] = None
    wlan_data_rate: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="wlanDataRate"), pydantic.Field(alias="wlanDataRate")
    ] = None
    battery: typing.Optional[str] = pydantic.Field(default=None)
    """
    Battery status 0: battery is not charging 1: battery is
    charging
    """

    battery_percent: typing.Optional[str] = pydantic.Field(default=None)
    """
    Battery charge level Value ranges from 0 - 100
    """

    securemode: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reserved
    """

    auth: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of WiFi Protected Access used (Authentication Key).
    """

    encry: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of encryption used for the WiFi connection.
    """

    ota_interface_ver: typing.Optional[str] = None
    ota_api_ver: typing.Optional[str] = None
    upnp_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    UPnP Device Architecture Version
    """

    upnp_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    UPnP UUID
    """

    uart_pass_port: typing.Optional[str] = pydantic.Field(default=None)
    """
    Port used for TCP/IP Communcations/Socket Connections
    """

    communication_port: typing.Optional[str] = pydantic.Field(default=None)
    """
    TCP port for internal messages
    """

    web_firmware_update_hide: typing.Optional[str] = None
    ignore_talkstart: typing.Optional[str] = None
    silence_ota_flag: typing.Optional[str] = None
    silence_ota_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="silenceOTATime"), pydantic.Field(alias="silenceOTATime")
    ] = None
    ignore_silence_ota_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ignore_silenceOTATime"),
        pydantic.Field(alias="ignore_silenceOTATime"),
    ] = None
    new_tunein_preset_and_alarm: typing.Optional[str] = None
    iheartradio_new: typing.Optional[str] = None
    new_iheart_podcast: typing.Optional[str] = None
    tidal_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    TIDAL API version
    """

    service_version: typing.Optional[str] = None
    eq_support: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="EQ_support"), pydantic.Field(alias="EQ_support")
    ] = None
    eq_version: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="EQVersion"), pydantic.Field(alias="EQVersion")
    ] = None
    hi_fi_src_version: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="HiFiSRC_version"), pydantic.Field(alias="HiFiSRC_version")
    ] = None
    audio_channel_config: typing.Optional[str] = None
    app_timezone_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Timezone ID
    """

    avs_timezone_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Timezone ID for Alexa
    """

    tz_info_ver: typing.Optional[str] = None
    max_volume: typing.Optional[str] = pydantic.Field(default=None)
    """
    Maximum volume level (normally 100)
    """

    power_mode: typing.Optional[str] = None
    security: typing.Optional[str] = pydantic.Field(default=None)
    """
    HTTPS API version
    """

    security_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    HTTPS API security version
    """

    security_capabilities: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    HTTPS API security capabilities
    """

    public_https_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    HTTPS API public version
    """

    ble_remote_control: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="BleRemoteControl"), pydantic.Field(alias="BleRemoteControl")
    ] = None
    ble_remote_connected: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="BleRemoteConnected"), pydantic.Field(alias="BleRemoteConnected")
    ] = None
    ble_remote_exception: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="BleRemoteException"), pydantic.Field(alias="BleRemoteException")
    ] = None
    udisk: typing.Optional[str] = pydantic.Field(default=None)
    """
    USB disk status 0: no USB disk 1: USB disk is connected
    """

    umount: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reserved
    """

    auto_sense_version: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="autoSenseVersion"), pydantic.Field(alias="autoSenseVersion")
    ] = None
    set_play_mode_enable: typing.Optional[str] = None
    set_play_mode_gain: typing.Optional[str] = None
    audio_output_mode_ver: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="audioOutputModeVer"), pydantic.Field(alias="audioOutputModeVer")
    ] = None
    privacy_mode: typing.Optional[str] = None
    device_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="DeviceName"),
        pydantic.Field(alias="DeviceName", description="The device UPnP and Airplay friendly name"),
    ] = None
    """
    The device UPnP and Airplay friendly name
    """

    group_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="GroupName"),
        pydantic.Field(alias="GroupName", description="The group name of the device that it belongs to"),
    ] = None
    """
    The group name of the device that it belongs to
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
