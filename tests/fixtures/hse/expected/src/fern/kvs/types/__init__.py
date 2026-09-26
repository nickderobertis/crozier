



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .kvs_cn_tree_get_response import KvsCnTreeGetResponse
    from .kvs_cn_tree_get_response_nodes_item import KvsCnTreeGetResponseNodesItem
    from .kvs_cn_tree_get_response_nodes_item_kvsets import KvsCnTreeGetResponseNodesItemKvsets
    from .kvs_cn_tree_get_response_nodes_item_kvsets_one_item import KvsCnTreeGetResponseNodesItemKvsetsOneItem
    from .kvs_cn_tree_get_response_nodes_item_kvsets_one_item_job import KvsCnTreeGetResponseNodesItemKvsetsOneItemJob
    from .kvs_param_get_response import KvsParamGetResponse
    from .kvs_param_set_request_body import KvsParamSetRequestBody
    from .kvs_params_get_response import KvsParamsGetResponse
_dynamic_imports: typing.Dict[str, str] = {
    "KvsCnTreeGetResponse": ".kvs_cn_tree_get_response",
    "KvsCnTreeGetResponseNodesItem": ".kvs_cn_tree_get_response_nodes_item",
    "KvsCnTreeGetResponseNodesItemKvsets": ".kvs_cn_tree_get_response_nodes_item_kvsets",
    "KvsCnTreeGetResponseNodesItemKvsetsOneItem": ".kvs_cn_tree_get_response_nodes_item_kvsets_one_item",
    "KvsCnTreeGetResponseNodesItemKvsetsOneItemJob": ".kvs_cn_tree_get_response_nodes_item_kvsets_one_item_job",
    "KvsParamGetResponse": ".kvs_param_get_response",
    "KvsParamSetRequestBody": ".kvs_param_set_request_body",
    "KvsParamsGetResponse": ".kvs_params_get_response",
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
    "KvsCnTreeGetResponse",
    "KvsCnTreeGetResponseNodesItem",
    "KvsCnTreeGetResponseNodesItemKvsets",
    "KvsCnTreeGetResponseNodesItemKvsetsOneItem",
    "KvsCnTreeGetResponseNodesItemKvsetsOneItemJob",
    "KvsParamGetResponse",
    "KvsParamSetRequestBody",
    "KvsParamsGetResponse",
]
