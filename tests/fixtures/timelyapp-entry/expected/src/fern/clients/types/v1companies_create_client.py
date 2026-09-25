

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1companies_create_client_external_references_item import V1CompaniesCreateClientExternalReferencesItem


class V1CompaniesCreateClient(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Name of the client
    """

    active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the client is active
    """

    color: typing.Optional[str] = pydantic.Field(default=None)
    """
    Client display color (hex code)
    """

    external_references: typing.Optional[typing.List[V1CompaniesCreateClientExternalReferencesItem]] = pydantic.Field(
        default=None
    )
    """
    External references for the client
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
