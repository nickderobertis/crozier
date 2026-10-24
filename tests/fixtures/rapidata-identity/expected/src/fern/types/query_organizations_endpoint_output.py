

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .org_role import OrgRole


class QueryOrganizationsEndpointOutput(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The id of the organization.
    """

    name: str = pydantic.Field()
    """
    The human-readable name of the organization.
    """

    role: OrgRole = pydantic.Field()
    """
    The caller's role in the organization.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
