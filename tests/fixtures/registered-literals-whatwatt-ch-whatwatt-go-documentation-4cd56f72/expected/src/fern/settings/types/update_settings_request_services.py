

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_settings_request_services_berry import UpdateSettingsRequestServicesBerry
from .update_settings_request_services_cloud import UpdateSettingsRequestServicesCloud
from .update_settings_request_services_local import UpdateSettingsRequestServicesLocal
from .update_settings_request_services_modbus import UpdateSettingsRequestServicesModbus
from .update_settings_request_services_sd import UpdateSettingsRequestServicesSd


class UpdateSettingsRequestServices(UniversalBaseModel):
    cloud: typing.Optional[UpdateSettingsRequestServicesCloud] = None
    local: typing.Optional[UpdateSettingsRequestServicesLocal] = None
    broadcast: typing.Optional[bool] = None
    other_energy_provider: typing.Optional[bool] = None
    report_interval: typing.Optional[int] = None
    log: typing.Optional[bool] = None
    meter_proxy: typing.Optional[bool] = None
    sd: typing.Optional[UpdateSettingsRequestServicesSd] = None
    modbus: typing.Optional[UpdateSettingsRequestServicesModbus] = None
    berry: typing.Optional[UpdateSettingsRequestServicesBerry] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
