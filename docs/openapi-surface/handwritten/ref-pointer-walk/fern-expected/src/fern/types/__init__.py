



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .choice import Choice
    from .choice_code import ChoiceCode
    from .components_schemas_route_properties_from_one_of0 import ComponentsSchemasRoutePropertiesFromOneOf0
    from .composite import Composite
    from .create_route_request_properties import CreateRouteRequestProperties
    from .either import Either
    from .either_flag import EitherFlag
    from .holder import Holder
    from .named import Named
    from .route import Route
    from .route_from import RouteFrom, RouteFrom_App, RouteFrom_Phone
    from .route_from_app import RouteFromApp
    from .route_from_phone import RouteFromPhone
    from .route_properties import RouteProperties
    from .route_to import RouteTo, RouteTo_App, RouteTo_Phone
    from .route_to_phone import RouteToPhone
    from .tag_list import TagList
    from .tag_list_item import TagListItem
    from .tag_list_item_tag import TagListItemTag
_dynamic_imports: typing.Dict[str, str] = {
    "Choice": ".choice",
    "ChoiceCode": ".choice_code",
    "ComponentsSchemasRoutePropertiesFromOneOf0": ".components_schemas_route_properties_from_one_of0",
    "Composite": ".composite",
    "CreateRouteRequestProperties": ".create_route_request_properties",
    "Either": ".either",
    "EitherFlag": ".either_flag",
    "Holder": ".holder",
    "Named": ".named",
    "Route": ".route",
    "RouteFrom": ".route_from",
    "RouteFromApp": ".route_from_app",
    "RouteFromPhone": ".route_from_phone",
    "RouteFrom_App": ".route_from",
    "RouteFrom_Phone": ".route_from",
    "RouteProperties": ".route_properties",
    "RouteTo": ".route_to",
    "RouteToPhone": ".route_to_phone",
    "RouteTo_App": ".route_to",
    "RouteTo_Phone": ".route_to",
    "TagList": ".tag_list",
    "TagListItem": ".tag_list_item",
    "TagListItemTag": ".tag_list_item_tag",
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
    "Choice",
    "ChoiceCode",
    "ComponentsSchemasRoutePropertiesFromOneOf0",
    "Composite",
    "CreateRouteRequestProperties",
    "Either",
    "EitherFlag",
    "Holder",
    "Named",
    "Route",
    "RouteFrom",
    "RouteFromApp",
    "RouteFromPhone",
    "RouteFrom_App",
    "RouteFrom_Phone",
    "RouteProperties",
    "RouteTo",
    "RouteToPhone",
    "RouteTo_App",
    "RouteTo_Phone",
    "TagList",
    "TagListItem",
    "TagListItemTag",
]
