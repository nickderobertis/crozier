

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetDraftRegistrationsDraftIdInstitutionsResponseRelationships(UniversalBaseModel):
    """
    URLs to other entities or entity collections that have a relationship to the institution entity.
    """

    nodes: typing.Optional[str] = pydantic.Field(default=None)
    """
    A relationship to the nodes affiliated with the institution.
    """

    registrations: typing.Optional[str] = pydantic.Field(default=None)
    """
    A relationship to the registrations affiliated with the institution.
    """

    users: typing.Optional[str] = pydantic.Field(default=None)
    """
    A relationship to the users affiliated with the institution.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
