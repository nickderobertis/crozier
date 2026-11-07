

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .registrations_citation_read_response_attributes import RegistrationsCitationReadResponseAttributes
from .registrations_citation_read_response_links import RegistrationsCitationReadResponseLinks


class RegistrationsCitationReadResponse(UniversalBaseModel):
    attributes: typing.Optional[RegistrationsCitationReadResponseAttributes] = pydantic.Field(default=None)
    """
    The properties of the citation entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the entity being cited.
    """

    links: typing.Optional[RegistrationsCitationReadResponseLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the citation entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the citation entity (either `node-citation`, `preprint-citation`, or `registration-citation`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
