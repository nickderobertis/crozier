

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .registrations_read_response_attributes import RegistrationsReadResponseAttributes
from .registrations_read_response_links import RegistrationsReadResponseLinks
from .registrations_read_response_relationships import RegistrationsReadResponseRelationships


class RegistrationsReadResponse(UniversalBaseModel):
    attributes: typing.Optional[RegistrationsReadResponseAttributes] = pydantic.Field(default=None)
    """
    The properties of the registration entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the registration.
    """

    links: typing.Optional[RegistrationsReadResponseLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the registrations entity.
    """

    relationships: typing.Optional[RegistrationsReadResponseRelationships] = pydantic.Field(default=None)
    """
    URLs to other entities or entity collections that have a relationship to the registration entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the registration entity (`registrations`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
