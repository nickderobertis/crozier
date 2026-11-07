

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_draft_registrations_draft_id_institutions_response_attributes import (
    GetDraftRegistrationsDraftIdInstitutionsResponseAttributes,
)
from .get_draft_registrations_draft_id_institutions_response_links import (
    GetDraftRegistrationsDraftIdInstitutionsResponseLinks,
)
from .get_draft_registrations_draft_id_institutions_response_relationships import (
    GetDraftRegistrationsDraftIdInstitutionsResponseRelationships,
)


class GetDraftRegistrationsDraftIdInstitutionsResponse(UniversalBaseModel):
    attributes: typing.Optional[GetDraftRegistrationsDraftIdInstitutionsResponseAttributes] = pydantic.Field(
        default=None
    )
    """
    The properties of the institution entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the institution entity.
    """

    links: typing.Optional[GetDraftRegistrationsDraftIdInstitutionsResponseLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the institutions entity.
    """

    relationships: typing.Optional[GetDraftRegistrationsDraftIdInstitutionsResponseRelationships] = pydantic.Field(
        default=None
    )
    """
    URLs to other entities or entity collections that have a relationship to the institution entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the institution entity (`institutions`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
