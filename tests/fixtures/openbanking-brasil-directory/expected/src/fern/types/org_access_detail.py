

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .domain_role_detail import DomainRoleDetail


class OrgAccessDetail(UniversalBaseModel):
    domain_role_details: typing_extensions.Annotated[
        typing.Optional[typing.List[DomainRoleDetail]],
        FieldMetadata(alias="DomainRoleDetails"),
        pydantic.Field(
            alias="DomainRoleDetails", description="Array of domain, role and status of domain role mapping"
        ),
    ] = None
    """
    Array of domain, role and status of domain role mapping
    """

    org_admin: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="OrgAdmin"),
        pydantic.Field(alias="OrgAdmin", description="Is the user the org admin of the current org"),
    ] = None
    """
    Is the user the org admin of the current org
    """

    org_registration_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OrgRegistrationNumber"),
        pydantic.Field(alias="OrgRegistrationNumber", description="CNPJ/Registration number of the org"),
    ] = None
    """
    CNPJ/Registration number of the org
    """

    organisation_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OrganisationName"),
        pydantic.Field(alias="OrganisationName", description="Name of the organisation."),
    ] = None
    """
    Name of the organisation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
