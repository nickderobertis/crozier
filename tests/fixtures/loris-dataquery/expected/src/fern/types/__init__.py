



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .all_queries import AllQueries
    from .bad_request_error_body import BadRequestErrorBody
    from .get_queries_query_id_count_response import GetQueriesQueryIdCountResponse
    from .post_queries_response import PostQueriesResponse
    from .query import Query
    from .query_criteria_group import QueryCriteriaGroup
    from .query_criteria_group_operator import QueryCriteriaGroupOperator
    from .query_field import QueryField
    from .query_group_field import QueryGroupField
    from .query_group_field_op import QueryGroupFieldOp
    from .query_object import QueryObject
    from .query_object_type import QueryObjectType
    from .query_results import QueryResults
    from .query_run import QueryRun
    from .query_run_list import QueryRunList
_dynamic_imports: typing.Dict[str, str] = {
    "AllQueries": ".all_queries",
    "BadRequestErrorBody": ".bad_request_error_body",
    "GetQueriesQueryIdCountResponse": ".get_queries_query_id_count_response",
    "PostQueriesResponse": ".post_queries_response",
    "Query": ".query",
    "QueryCriteriaGroup": ".query_criteria_group",
    "QueryCriteriaGroupOperator": ".query_criteria_group_operator",
    "QueryField": ".query_field",
    "QueryGroupField": ".query_group_field",
    "QueryGroupFieldOp": ".query_group_field_op",
    "QueryObject": ".query_object",
    "QueryObjectType": ".query_object_type",
    "QueryResults": ".query_results",
    "QueryRun": ".query_run",
    "QueryRunList": ".query_run_list",
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
    "AllQueries",
    "BadRequestErrorBody",
    "GetQueriesQueryIdCountResponse",
    "PostQueriesResponse",
    "Query",
    "QueryCriteriaGroup",
    "QueryCriteriaGroupOperator",
    "QueryField",
    "QueryGroupField",
    "QueryGroupFieldOp",
    "QueryObject",
    "QueryObjectType",
    "QueryResults",
    "QueryRun",
    "QueryRunList",
]
