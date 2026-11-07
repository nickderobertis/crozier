

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .replace_settings_request_services_berry import ReplaceSettingsRequestServicesBerry
from .replace_settings_request_services_cloud import ReplaceSettingsRequestServicesCloud
from .replace_settings_request_services_local import ReplaceSettingsRequestServicesLocal
from .replace_settings_request_services_modbus import ReplaceSettingsRequestServicesModbus
from .replace_settings_request_services_sd import ReplaceSettingsRequestServicesSd


class ReplaceSettingsRequestServices(UniversalBaseModel):
    cloud: typing.Optional[ReplaceSettingsRequestServicesCloud] = None
    local: typing.Optional[ReplaceSettingsRequestServicesLocal] = None
    broadcast: typing.Optional[bool] = None
    other_energy_provider: typing.Optional[bool] = None
    report_interval: typing.Optional[int] = None
    log: typing.Optional[bool] = None
    meter_proxy: typing.Optional[bool] = None
    sd: typing.Optional[ReplaceSettingsRequestServicesSd] = None
    modbus: typing.Optional[ReplaceSettingsRequestServicesModbus] = None
    berry: typing.Optional[ReplaceSettingsRequestServicesBerry] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
