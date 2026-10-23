

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .me_response_environments_item import MeResponseEnvironmentsItem
from .me_response_organization_access import MeResponseOrganizationAccess
from .me_response_workspaces_item import MeResponseWorkspacesItem


class MeResponse(UniversalBaseModel):
    organization_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="organizationId"), pydantic.Field(alias="organizationId")
    ] = None
    organization_access: typing_extensions.Annotated[
        typing.Optional[MeResponseOrganizationAccess],
        FieldMetadata(alias="organizationAccess"),
        pydantic.Field(alias="organizationAccess"),
    ] = None
    workspaces: typing.Optional[typing.List[MeResponseWorkspacesItem]] = None
    environments: typing.Optional[typing.List[MeResponseEnvironmentsItem]] = pydantic.Field(default=None)
    """
    Deprecated alias of `workspaces`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
