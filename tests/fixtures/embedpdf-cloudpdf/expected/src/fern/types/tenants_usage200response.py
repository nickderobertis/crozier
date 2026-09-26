

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tenants_usage200response_metrics import TenantsUsage200ResponseMetrics


class TenantsUsage200Response(UniversalBaseModel):
    tenant_id: typing_extensions.Annotated[str, FieldMetadata(alias="tenantId"), pydantic.Field(alias="tenantId")]
    period_start: typing_extensions.Annotated[
        str, FieldMetadata(alias="periodStart"), pydantic.Field(alias="periodStart")
    ]
    period_end: typing_extensions.Annotated[str, FieldMetadata(alias="periodEnd"), pydantic.Field(alias="periodEnd")]
    metrics: TenantsUsage200ResponseMetrics

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
