

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesProvisioningApi(UniversalBaseModel):
    version: str
    account_property_scopes_version: typing_extensions.Annotated[
        int, FieldMetadata(alias="AccountPropertyScopesVersion"), pydantic.Field(alias="AccountPropertyScopesVersion")
    ]
    account_property_scopes_federated_enabled: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="AccountPropertyScopesFederatedEnabled"),
        pydantic.Field(alias="AccountPropertyScopesFederatedEnabled"),
    ]
    account_property_scopes_published_enabled: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="AccountPropertyScopesPublishedEnabled"),
        pydantic.Field(alias="AccountPropertyScopesPublishedEnabled"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
