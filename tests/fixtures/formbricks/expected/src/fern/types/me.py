

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .me_environments_item import MeEnvironmentsItem
from .me_organization_access import MeOrganizationAccess
from .me_workspaces_item import MeWorkspacesItem


class Me(UniversalBaseModel):
    organization_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="organizationId"), pydantic.Field(alias="organizationId")
    ]
    organization_access: typing_extensions.Annotated[
        MeOrganizationAccess, FieldMetadata(alias="organizationAccess"), pydantic.Field(alias="organizationAccess")
    ]
    workspaces: typing.List[MeWorkspacesItem]
    environments: typing.List[MeEnvironmentsItem] = pydantic.Field()
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
