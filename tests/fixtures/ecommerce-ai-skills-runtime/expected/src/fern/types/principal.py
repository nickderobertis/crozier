

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .principal_tenant_mode import PrincipalTenantMode
from .role import Role


class Principal(UniversalBaseModel):
    tenant_id: str
    tenant_name: str
    tenant_mode: PrincipalTenantMode
    user_id: str
    email: str
    role: Role

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
