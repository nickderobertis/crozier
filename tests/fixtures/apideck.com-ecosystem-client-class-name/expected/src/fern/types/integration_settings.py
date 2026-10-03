

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class IntegrationSettings(UniversalBaseModel):
    albacross_id: typing.Optional[str] = None
    automate_enabled: typing.Optional[bool] = None
    blendr_enabled: typing.Optional[bool] = None
    combidesk_enabled: typing.Optional[bool] = None
    crisp_id: typing.Optional[str] = None
    drift_id: typing.Optional[str] = None
    google_analytics_id: typing.Optional[str] = None
    google_tag_manager_id: typing.Optional[str] = None
    heap_id: typing.Optional[str] = None
    hubspot_portal_id: typing.Optional[str] = None
    integromat_enabled: typing.Optional[bool] = None
    intercom_app_id: typing.Optional[str] = None
    iubenda_cookie_policy_id: typing.Optional[str] = None
    iubenda_site_id: typing.Optional[str] = None
    journy_io_domain: typing.Optional[str] = None
    journy_io_id: typing.Optional[str] = None
    livechat_id: typing.Optional[str] = None
    metomic_id: typing.Optional[str] = None
    microsoft_flow_enabled: typing.Optional[bool] = None
    microsoft_flow_id: typing.Optional[str] = None
    onetrust_id: typing.Optional[str] = None
    piesync_enabled: typing.Optional[bool] = None
    segment_enabled: typing.Optional[bool] = None
    segment_id: typing.Optional[str] = None
    tray_io_enabled: typing.Optional[bool] = None
    zapier_beta_link: typing.Optional[str] = None
    zapier_enabled: typing.Optional[bool] = None
    zapier_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
