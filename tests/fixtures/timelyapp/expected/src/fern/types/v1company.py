

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1company_external_references_item import V1CompanyExternalReferencesItem
from .v1company_tic import V1CompanyTic


class V1Company(UniversalBaseModel):
    id: int = pydantic.Field()
    """
    Unique identifier for the client
    """

    name: str = pydantic.Field()
    """
    Name of the client
    """

    active: bool = pydantic.Field()
    """
    Whether the client is active
    """

    external_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    External ID for the client
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    iso8601
    """

    color: str = pydantic.Field()
    """
    Client display color (hex code)
    """

    external_references: typing.Optional[typing.List[V1CompanyExternalReferencesItem]] = pydantic.Field(default=None)
    """
    External references for the client
    """

    tic: typing.Optional[V1CompanyTic] = pydantic.Field(default=None)
    """
    Integration metadata (internal only). Present for synced clients.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
