



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .registration_schema_read_response import RegistrationSchemaReadResponse
    from .registration_schema_read_response_attributes import RegistrationSchemaReadResponseAttributes
    from .registration_schema_read_response_links import RegistrationSchemaReadResponseLinks
    from .registration_schema_read_response_relationships import RegistrationSchemaReadResponseRelationships
    from .registration_schemas_list_response import RegistrationSchemasListResponse
    from .registration_schemas_list_response_attributes import RegistrationSchemasListResponseAttributes
    from .registration_schemas_list_response_links import RegistrationSchemasListResponseLinks
    from .registration_schemas_list_response_relationships import RegistrationSchemasListResponseRelationships
_dynamic_imports: typing.Dict[str, str] = {
    "RegistrationSchemaReadResponse": ".registration_schema_read_response",
    "RegistrationSchemaReadResponseAttributes": ".registration_schema_read_response_attributes",
    "RegistrationSchemaReadResponseLinks": ".registration_schema_read_response_links",
    "RegistrationSchemaReadResponseRelationships": ".registration_schema_read_response_relationships",
    "RegistrationSchemasListResponse": ".registration_schemas_list_response",
    "RegistrationSchemasListResponseAttributes": ".registration_schemas_list_response_attributes",
    "RegistrationSchemasListResponseLinks": ".registration_schemas_list_response_links",
    "RegistrationSchemasListResponseRelationships": ".registration_schemas_list_response_relationships",
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
    "RegistrationSchemaReadResponse",
    "RegistrationSchemaReadResponseAttributes",
    "RegistrationSchemaReadResponseLinks",
    "RegistrationSchemaReadResponseRelationships",
    "RegistrationSchemasListResponse",
    "RegistrationSchemasListResponseAttributes",
    "RegistrationSchemasListResponseLinks",
    "RegistrationSchemasListResponseRelationships",
]
