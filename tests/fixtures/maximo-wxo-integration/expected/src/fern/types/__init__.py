



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .check_asset_for_work_orders_get_response import CheckAssetForWorkOrdersGetResponse
    from .check_multiple_assets_for_work_orders_get_response import CheckMultipleAssetsForWorkOrdersGetResponse
    from .create_work_order_get_response import CreateWorkOrderGetResponse
    from .get_unhealthy_assets_get_response import GetUnhealthyAssetsGetResponse
    from .login_token_post_response import LoginTokenPostResponse
    from .unprocessable_entity_error_body import UnprocessableEntityErrorBody
_dynamic_imports: typing.Dict[str, str] = {
    "CheckAssetForWorkOrdersGetResponse": ".check_asset_for_work_orders_get_response",
    "CheckMultipleAssetsForWorkOrdersGetResponse": ".check_multiple_assets_for_work_orders_get_response",
    "CreateWorkOrderGetResponse": ".create_work_order_get_response",
    "GetUnhealthyAssetsGetResponse": ".get_unhealthy_assets_get_response",
    "LoginTokenPostResponse": ".login_token_post_response",
    "UnprocessableEntityErrorBody": ".unprocessable_entity_error_body",
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
    "CheckAssetForWorkOrdersGetResponse",
    "CheckMultipleAssetsForWorkOrdersGetResponse",
    "CreateWorkOrderGetResponse",
    "GetUnhealthyAssetsGetResponse",
    "LoginTokenPostResponse",
    "UnprocessableEntityErrorBody",
]
