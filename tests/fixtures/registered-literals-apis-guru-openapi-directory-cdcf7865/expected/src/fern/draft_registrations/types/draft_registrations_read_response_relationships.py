

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DraftRegistrationsReadResponseRelationships(UniversalBaseModel):
    """
    URLs to other entities or entity collections that have a relationship to the draft registration entity.
    """

    branched_from: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the node that this draft registration was created from.
    """

    initiator: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the user who initiated the draft registration.
    """

    registration_schema: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the detailed registration schema that this draft conforms to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
