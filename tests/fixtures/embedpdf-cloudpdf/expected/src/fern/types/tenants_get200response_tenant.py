

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tenants_get200response_tenant_status import TenantsGet200ResponseTenantStatus


class TenantsGet200ResponseTenant(UniversalBaseModel):
    id: str
    name: str
    auto_provisioned: typing_extensions.Annotated[
        bool, FieldMetadata(alias="autoProvisioned"), pydantic.Field(alias="autoProvisioned")
    ]
    status: typing.Optional[TenantsGet200ResponseTenantStatus] = None
    created_at: typing_extensions.Annotated[float, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
