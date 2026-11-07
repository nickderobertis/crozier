

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_settings_response_services_berry import GetSettingsResponseServicesBerry
from .get_settings_response_services_cloud import GetSettingsResponseServicesCloud
from .get_settings_response_services_local import GetSettingsResponseServicesLocal
from .get_settings_response_services_modbus import GetSettingsResponseServicesModbus
from .get_settings_response_services_sd import GetSettingsResponseServicesSd


class GetSettingsResponseServices(UniversalBaseModel):
    cloud: typing.Optional[GetSettingsResponseServicesCloud] = None
    local: typing.Optional[GetSettingsResponseServicesLocal] = None
    broadcast: typing.Optional[bool] = None
    other_energy_provider: typing.Optional[bool] = None
    report_interval: typing.Optional[int] = None
    log: typing.Optional[bool] = None
    meter_proxy: typing.Optional[bool] = None
    sd: typing.Optional[GetSettingsResponseServicesSd] = None
    modbus: typing.Optional[GetSettingsResponseServicesModbus] = None
    berry: typing.Optional[GetSettingsResponseServicesBerry] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
