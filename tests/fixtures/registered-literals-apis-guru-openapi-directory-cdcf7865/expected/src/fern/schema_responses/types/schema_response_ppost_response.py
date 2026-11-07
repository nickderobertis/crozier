

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .schema_response_ppost_response_attributes import SchemaResponsePpostResponseAttributes
from .schema_response_ppost_response_links import SchemaResponsePpostResponseLinks
from .schema_response_ppost_response_relationships import SchemaResponsePpostResponseRelationships


class SchemaResponsePpostResponse(UniversalBaseModel):
    attributes: SchemaResponsePpostResponseAttributes = pydantic.Field()
    """
    The properties of the Schema Response.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the Schema Response.
    """

    links: typing.Optional[SchemaResponsePpostResponseLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the Schema Response entity.
    """

    relationships: typing.Optional[SchemaResponsePpostResponseRelationships] = pydantic.Field(default=None)
    """
    Links to other entities or entity collections that have a relationship to the file entity.
    """

    type: str = pydantic.Field()
    """
    The type identifier of the Schema Response (`schema-response`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
