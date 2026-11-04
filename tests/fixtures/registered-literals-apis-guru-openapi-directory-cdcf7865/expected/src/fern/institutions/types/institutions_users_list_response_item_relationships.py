

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InstitutionsUsersListResponseItemRelationships(UniversalBaseModel):
    """
    URLs to other entities or entity collections that have a relationship to the user entity.
    """

    institutions: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of institutions the user is affiliated with.
    """

    nodes: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the list of nodes the user is a contributor to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
