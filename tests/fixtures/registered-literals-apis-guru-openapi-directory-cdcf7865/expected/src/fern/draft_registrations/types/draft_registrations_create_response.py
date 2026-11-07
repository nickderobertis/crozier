

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .draft_registrations_create_response_attributes import DraftRegistrationsCreateResponseAttributes
from .draft_registrations_create_response_links import DraftRegistrationsCreateResponseLinks
from .draft_registrations_create_response_relationships import DraftRegistrationsCreateResponseRelationships


class DraftRegistrationsCreateResponse(UniversalBaseModel):
    attributes: DraftRegistrationsCreateResponseAttributes = pydantic.Field()
    """
    The properties of the Draft Registration entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the draft registration entity.
    """

    links: typing.Optional[DraftRegistrationsCreateResponseLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the draft registration entity.
    """

    relationships: typing.Optional[DraftRegistrationsCreateResponseRelationships] = pydantic.Field(default=None)
    """
    URLs to other entities or entity collections that have a relationship to the draft registration entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the draft registration entity (`draft_registrations`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
