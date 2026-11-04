



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_schema_responses_schema_response_id_schema_blocks_schema_response_block_id_response import (
        GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponse,
    )
    from .get_schema_responses_schema_response_id_schema_blocks_schema_response_block_id_response_attributes import (
        GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseAttributes,
    )
    from .get_schema_responses_schema_response_id_schema_blocks_schema_response_block_id_response_attributes_block_type import (
        GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseAttributesBlockType,
    )
    from .get_schema_responses_schema_response_id_schema_blocks_schema_response_block_id_response_links import (
        GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseLinks,
    )
    from .get_schema_responses_schema_response_id_schema_blocks_schema_response_block_id_response_relationships import (
        GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseRelationships,
    )
    from .schema_response_blocks_read_response import SchemaResponseBlocksReadResponse
    from .schema_response_blocks_read_response_attributes import SchemaResponseBlocksReadResponseAttributes
    from .schema_response_blocks_read_response_attributes_block_type import (
        SchemaResponseBlocksReadResponseAttributesBlockType,
    )
    from .schema_response_blocks_read_response_links import SchemaResponseBlocksReadResponseLinks
    from .schema_response_blocks_read_response_relationships import SchemaResponseBlocksReadResponseRelationships
_dynamic_imports: typing.Dict[str, str] = {
    "GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponse": ".get_schema_responses_schema_response_id_schema_blocks_schema_response_block_id_response",
    "GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseAttributes": ".get_schema_responses_schema_response_id_schema_blocks_schema_response_block_id_response_attributes",
    "GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseAttributesBlockType": ".get_schema_responses_schema_response_id_schema_blocks_schema_response_block_id_response_attributes_block_type",
    "GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseLinks": ".get_schema_responses_schema_response_id_schema_blocks_schema_response_block_id_response_links",
    "GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseRelationships": ".get_schema_responses_schema_response_id_schema_blocks_schema_response_block_id_response_relationships",
    "SchemaResponseBlocksReadResponse": ".schema_response_blocks_read_response",
    "SchemaResponseBlocksReadResponseAttributes": ".schema_response_blocks_read_response_attributes",
    "SchemaResponseBlocksReadResponseAttributesBlockType": ".schema_response_blocks_read_response_attributes_block_type",
    "SchemaResponseBlocksReadResponseLinks": ".schema_response_blocks_read_response_links",
    "SchemaResponseBlocksReadResponseRelationships": ".schema_response_blocks_read_response_relationships",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponse",
    "GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseAttributes",
    "GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseAttributesBlockType",
    "GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseLinks",
    "GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponseRelationships",
    "SchemaResponseBlocksReadResponse",
    "SchemaResponseBlocksReadResponseAttributes",
    "SchemaResponseBlocksReadResponseAttributesBlockType",
    "SchemaResponseBlocksReadResponseLinks",
    "SchemaResponseBlocksReadResponseRelationships",
]
