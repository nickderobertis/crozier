

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .schema_response_blocks_read_response_attributes import SchemaResponseBlocksReadResponseAttributes
from .schema_response_blocks_read_response_links import SchemaResponseBlocksReadResponseLinks
from .schema_response_blocks_read_response_relationships import SchemaResponseBlocksReadResponseRelationships


class SchemaResponseBlocksReadResponse(UniversalBaseModel):
    attributes: typing.Optional[SchemaResponseBlocksReadResponseAttributes] = pydantic.Field(default=None)
    """
    The attributes of the Registration Schema Block.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the Registration Schema Block.
    """

    links: typing.Optional[SchemaResponseBlocksReadResponseLinks] = pydantic.Field(default=None)
    """
    URLs to alternative representations of the  Registration Schema Block.
    """

    relationships: typing.Optional[SchemaResponseBlocksReadResponseRelationships] = pydantic.Field(default=None)
    """
    Links to other entities or entity collections that have a relationship to the Schema Response Action.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the Registration Schema Block (`schema-blocks`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
