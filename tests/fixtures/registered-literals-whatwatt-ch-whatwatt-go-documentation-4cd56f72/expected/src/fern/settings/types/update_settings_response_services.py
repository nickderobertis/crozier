

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_settings_response_services_berry import UpdateSettingsResponseServicesBerry
from .update_settings_response_services_cloud import UpdateSettingsResponseServicesCloud
from .update_settings_response_services_local import UpdateSettingsResponseServicesLocal
from .update_settings_response_services_modbus import UpdateSettingsResponseServicesModbus
from .update_settings_response_services_sd import UpdateSettingsResponseServicesSd


class UpdateSettingsResponseServices(UniversalBaseModel):
    cloud: typing.Optional[UpdateSettingsResponseServicesCloud] = None
    local: typing.Optional[UpdateSettingsResponseServicesLocal] = None
    broadcast: typing.Optional[bool] = None
    other_energy_provider: typing.Optional[bool] = None
    report_interval: typing.Optional[int] = None
    log: typing.Optional[bool] = None
    meter_proxy: typing.Optional[bool] = None
    sd: typing.Optional[UpdateSettingsResponseServicesSd] = None
    modbus: typing.Optional[UpdateSettingsResponseServicesModbus] = None
    berry: typing.Optional[UpdateSettingsResponseServicesBerry] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
