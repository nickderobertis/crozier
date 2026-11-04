



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_schema_responses_schema_response_id_actions_schema_response_action_id_response import (
        GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponse,
    )
    from .get_schema_responses_schema_response_id_actions_schema_response_action_id_response_attributes import (
        GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributes,
    )
    from .get_schema_responses_schema_response_id_actions_schema_response_action_id_response_attributes_from_state import (
        GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesFromState,
    )
    from .get_schema_responses_schema_response_id_actions_schema_response_action_id_response_attributes_to_state import (
        GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesToState,
    )
    from .get_schema_responses_schema_response_id_actions_schema_response_action_id_response_attributes_trigger import (
        GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesTrigger,
    )
    from .get_schema_responses_schema_response_id_actions_schema_response_action_id_response_links import (
        GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseLinks,
    )
    from .get_schema_responses_schema_response_id_actions_schema_response_action_id_response_relationships import (
        GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseRelationships,
    )
    from .schema_response_action_read_response import SchemaResponseActionReadResponse
    from .schema_response_action_read_response_attributes import SchemaResponseActionReadResponseAttributes
    from .schema_response_action_read_response_attributes_from_state import (
        SchemaResponseActionReadResponseAttributesFromState,
    )
    from .schema_response_action_read_response_attributes_to_state import (
        SchemaResponseActionReadResponseAttributesToState,
    )
    from .schema_response_action_read_response_attributes_trigger import (
        SchemaResponseActionReadResponseAttributesTrigger,
    )
    from .schema_response_action_read_response_links import SchemaResponseActionReadResponseLinks
    from .schema_response_action_read_response_relationships import SchemaResponseActionReadResponseRelationships
_dynamic_imports: typing.Dict[str, str] = {
    "GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponse": ".get_schema_responses_schema_response_id_actions_schema_response_action_id_response",
    "GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributes": ".get_schema_responses_schema_response_id_actions_schema_response_action_id_response_attributes",
    "GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesFromState": ".get_schema_responses_schema_response_id_actions_schema_response_action_id_response_attributes_from_state",
    "GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesToState": ".get_schema_responses_schema_response_id_actions_schema_response_action_id_response_attributes_to_state",
    "GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesTrigger": ".get_schema_responses_schema_response_id_actions_schema_response_action_id_response_attributes_trigger",
    "GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseLinks": ".get_schema_responses_schema_response_id_actions_schema_response_action_id_response_links",
    "GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseRelationships": ".get_schema_responses_schema_response_id_actions_schema_response_action_id_response_relationships",
    "SchemaResponseActionReadResponse": ".schema_response_action_read_response",
    "SchemaResponseActionReadResponseAttributes": ".schema_response_action_read_response_attributes",
    "SchemaResponseActionReadResponseAttributesFromState": ".schema_response_action_read_response_attributes_from_state",
    "SchemaResponseActionReadResponseAttributesToState": ".schema_response_action_read_response_attributes_to_state",
    "SchemaResponseActionReadResponseAttributesTrigger": ".schema_response_action_read_response_attributes_trigger",
    "SchemaResponseActionReadResponseLinks": ".schema_response_action_read_response_links",
    "SchemaResponseActionReadResponseRelationships": ".schema_response_action_read_response_relationships",
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
    "GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponse",
    "GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributes",
    "GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesFromState",
    "GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesToState",
    "GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesTrigger",
    "GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseLinks",
    "GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseRelationships",
    "SchemaResponseActionReadResponse",
    "SchemaResponseActionReadResponseAttributes",
    "SchemaResponseActionReadResponseAttributesFromState",
    "SchemaResponseActionReadResponseAttributesToState",
    "SchemaResponseActionReadResponseAttributesTrigger",
    "SchemaResponseActionReadResponseLinks",
    "SchemaResponseActionReadResponseRelationships",
]
