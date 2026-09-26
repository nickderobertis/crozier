



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .list_schemes_api_templates_schemes_get_request_locale import ListSchemesApiTemplatesSchemesGetRequestLocale
    from .preview_request_locale import PreviewRequestLocale
    from .scheme_payload_locale import SchemePayloadLocale
    from .template_payload_category import TemplatePayloadCategory
    from .template_payload_locale import TemplatePayloadLocale
    from .template_update_category import TemplateUpdateCategory
_dynamic_imports: typing.Dict[str, str] = {
    "ListSchemesApiTemplatesSchemesGetRequestLocale": ".list_schemes_api_templates_schemes_get_request_locale",
    "PreviewRequestLocale": ".preview_request_locale",
    "SchemePayloadLocale": ".scheme_payload_locale",
    "TemplatePayloadCategory": ".template_payload_category",
    "TemplatePayloadLocale": ".template_payload_locale",
    "TemplateUpdateCategory": ".template_update_category",
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
    "ListSchemesApiTemplatesSchemesGetRequestLocale",
    "PreviewRequestLocale",
    "SchemePayloadLocale",
    "TemplatePayloadCategory",
    "TemplatePayloadLocale",
    "TemplateUpdateCategory",
]
