

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PlanResourceHeaders(UniversalBaseModel):
    client_tenant_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="clientTenantId"), pydantic.Field(alias="clientTenantId")
    ] = None
    home_tenant_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="homeTenantId"), pydantic.Field(alias="homeTenantId")
    ] = None
    identity_principal_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="identityPrincipalId"), pydantic.Field(alias="identityPrincipalId")
    ] = None
    identity_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="identityUrl"), pydantic.Field(alias="identityUrl")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
