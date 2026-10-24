

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .demo_session_tenant_mode import DemoSessionTenantMode


class DemoSession(UniversalBaseModel):
    api_key: str
    tenant_id: str
    tenant_mode: DemoSessionTenantMode
    warning: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
