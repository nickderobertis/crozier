

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .schema_response_action_read_response_attributes import SchemaResponseActionReadResponseAttributes
from .schema_response_action_read_response_links import SchemaResponseActionReadResponseLinks
from .schema_response_action_read_response_relationships import SchemaResponseActionReadResponseRelationships


class SchemaResponseActionReadResponse(UniversalBaseModel):
    attributes: typing.Optional[SchemaResponseActionReadResponseAttributes] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the Schema Response Action.
    """

    links: typing.Optional[SchemaResponseActionReadResponseLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the Registration Schema entity.
    """

    relationships: typing.Optional[SchemaResponseActionReadResponseRelationships] = pydantic.Field(default=None)
    """
    Links to other entities or entity collections that have a relationship to the Schema Response Action entity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the Schema Response Action (`schema-response-actions`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
