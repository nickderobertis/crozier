

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SchemaResponsePpostResponseRelationships(UniversalBaseModel):
    """
    Links to other entities or entity collections that have a relationship to the file entity.
    """

    actions: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the Registration Schema Actions endpoint for this Schema Response.
    """

    initiated_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the User who initiated the creation of the Schema Response.
    """

    registration: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the Registration for this Schema Response.
    """

    registration_schema: typing.Optional[str] = pydantic.Field(default=None)
    """
    A link to the Registration Schema for this Schema Response.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
