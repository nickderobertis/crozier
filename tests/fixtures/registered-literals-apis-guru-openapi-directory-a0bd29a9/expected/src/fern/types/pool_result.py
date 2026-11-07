

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .domain_user_credentials import DomainUserCredentials
from .hot_pool_settings import HotPoolSettings
from .provisioning_status_result import ProvisioningStatusResult
from .vm_specs import VmSpecs


class PoolResult(UniversalBaseModel):
    domain_user_credentials: typing_extensions.Annotated[
        typing.Optional[DomainUserCredentials],
        FieldMetadata(alias="domainUserCredentials"),
        pydantic.Field(alias="domainUserCredentials"),
    ] = None
    hot_pool_settings: typing_extensions.Annotated[
        typing.Optional[HotPoolSettings],
        FieldMetadata(alias="hotPoolSettings"),
        pydantic.Field(alias="hotPoolSettings"),
    ] = None
    pool_group_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="poolGroupName"), pydantic.Field(alias="poolGroupName")
    ]
    provisioning_status: typing_extensions.Annotated[
        typing.Optional[ProvisioningStatusResult],
        FieldMetadata(alias="provisioningStatus"),
        pydantic.Field(alias="provisioningStatus"),
    ] = None
    tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    user_group_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userGroupName"), pydantic.Field(alias="userGroupName")
    ] = None
    vm_specs: typing_extensions.Annotated[VmSpecs, FieldMetadata(alias="vmSpecs"), pydantic.Field(alias="vmSpecs")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
