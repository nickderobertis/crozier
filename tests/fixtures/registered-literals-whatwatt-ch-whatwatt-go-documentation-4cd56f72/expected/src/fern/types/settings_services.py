

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .settings_services_berry import SettingsServicesBerry
from .settings_services_cloud import SettingsServicesCloud
from .settings_services_local import SettingsServicesLocal
from .settings_services_modbus import SettingsServicesModbus
from .settings_services_sd import SettingsServicesSd


class SettingsServices(UniversalBaseModel):
    cloud: typing.Optional[SettingsServicesCloud] = None
    local: typing.Optional[SettingsServicesLocal] = None
    broadcast: typing.Optional[bool] = None
    other_energy_provider: typing.Optional[bool] = None
    report_interval: typing.Optional[int] = None
    log: typing.Optional[bool] = None
    meter_proxy: typing.Optional[bool] = None
    sd: typing.Optional[SettingsServicesSd] = None
    modbus: typing.Optional[SettingsServicesModbus] = None
    berry: typing.Optional[SettingsServicesBerry] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
