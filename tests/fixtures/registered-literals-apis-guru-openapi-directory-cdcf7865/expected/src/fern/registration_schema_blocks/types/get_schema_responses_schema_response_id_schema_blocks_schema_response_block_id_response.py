

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_schema_responses_schema_response_id_schema_blocks_schema_response_block_id_response_attributes import (
    GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseAttributes,
)
from .get_schema_responses_schema_response_id_schema_blocks_schema_response_block_id_response_links import (
    GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseLinks,
)
from .get_schema_responses_schema_response_id_schema_blocks_schema_response_block_id_response_relationships import (
    GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseRelationships,
)


class GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponse(UniversalBaseModel):
    attributes: typing.Optional[
        GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseAttributes
    ] = pydantic.Field(default=None)
    """
    The attributes of the Registration Schema Block.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the Registration Schema Block.
    """

    links: typing.Optional[GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseLinks] = (
        pydantic.Field(default=None)
    )
    """
    URLs to alternative representations of the  Registration Schema Block.
    """

    relationships: typing.Optional[
        GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseRelationships
    ] = pydantic.Field(default=None)
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
