

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tenants_create200response_tenant import TenantsCreate200ResponseTenant


class TenantsCreate200Response(UniversalBaseModel):
    tenant: TenantsCreate200ResponseTenant
    created: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
