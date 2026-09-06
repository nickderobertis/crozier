

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .domain_role_detail import DomainRoleDetail
from .status_enum import StatusEnum


class OrganisationAdminUser(UniversalBaseModel):
    domain_role_details: typing_extensions.Annotated[
        typing.Optional[typing.List[DomainRoleDetail]],
        FieldMetadata(alias="DomainRoleDetails"),
        pydantic.Field(alias="DomainRoleDetails"),
    ] = None
    status: typing_extensions.Annotated[
        typing.Optional[StatusEnum], FieldMetadata(alias="Status"), pydantic.Field(alias="Status")
    ] = None
    user_email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="UserEmail"),
        pydantic.Field(alias="UserEmail", description="User's email address"),
    ] = None
    """
    User's email address
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
