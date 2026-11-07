

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .replace_settings_response_services_berry import ReplaceSettingsResponseServicesBerry
from .replace_settings_response_services_cloud import ReplaceSettingsResponseServicesCloud
from .replace_settings_response_services_local import ReplaceSettingsResponseServicesLocal
from .replace_settings_response_services_modbus import ReplaceSettingsResponseServicesModbus
from .replace_settings_response_services_sd import ReplaceSettingsResponseServicesSd


class ReplaceSettingsResponseServices(UniversalBaseModel):
    cloud: typing.Optional[ReplaceSettingsResponseServicesCloud] = None
    local: typing.Optional[ReplaceSettingsResponseServicesLocal] = None
    broadcast: typing.Optional[bool] = None
    other_energy_provider: typing.Optional[bool] = None
    report_interval: typing.Optional[int] = None
    log: typing.Optional[bool] = None
    meter_proxy: typing.Optional[bool] = None
    sd: typing.Optional[ReplaceSettingsResponseServicesSd] = None
    modbus: typing.Optional[ReplaceSettingsResponseServicesModbus] = None
    berry: typing.Optional[ReplaceSettingsResponseServicesBerry] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
