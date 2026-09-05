



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .batch import Batch
    from .batch_condition import BatchCondition
    from .batch_condition_var_empty import BatchConditionVarEmpty
    from .batch_condition_var_min_size import BatchConditionVarMinSize
    from .batch_condition_var_not_empty import BatchConditionVarNotEmpty
    from .batch_condition_zero import BatchConditionZero
    from .batch_entry import BatchEntry
    from .batch_entry_for_each import BatchEntryForEach
    from .batch_entry_for_each_for_each import BatchEntryForEachForEach
    from .batch_entry_query import BatchEntryQuery
    from .health_response import HealthResponse
    from .named_query import NamedQuery
    from .operation_tree import OperationTree
    from .query_error import QueryError
    from .query_parameter_type import QueryParameterType
    from .query_parameter_type_array import QueryParameterTypeArray
    from .query_parameter_type_zero import QueryParameterTypeZero
    from .query_parameter_types import QueryParameterTypes
    from .query_parameter_value import QueryParameterValue
    from .query_parameters import QueryParameters
    from .query_request import QueryRequest, QueryRequest_Read, QueryRequest_Write
    from .query_response import QueryResponse
    from .read_batch_query import ReadBatchQuery
    from .read_query_request import ReadQueryRequest
    from .write_batch_query import WriteBatchQuery
    from .write_query_request import WriteQueryRequest
_dynamic_imports: typing.Dict[str, str] = {
    "Batch": ".batch",
    "BatchCondition": ".batch_condition",
    "BatchConditionVarEmpty": ".batch_condition_var_empty",
    "BatchConditionVarMinSize": ".batch_condition_var_min_size",
    "BatchConditionVarNotEmpty": ".batch_condition_var_not_empty",
    "BatchConditionZero": ".batch_condition_zero",
    "BatchEntry": ".batch_entry",
    "BatchEntryForEach": ".batch_entry_for_each",
    "BatchEntryForEachForEach": ".batch_entry_for_each_for_each",
    "BatchEntryQuery": ".batch_entry_query",
    "HealthResponse": ".health_response",
    "NamedQuery": ".named_query",
    "OperationTree": ".operation_tree",
    "QueryError": ".query_error",
    "QueryParameterType": ".query_parameter_type",
    "QueryParameterTypeArray": ".query_parameter_type_array",
    "QueryParameterTypeZero": ".query_parameter_type_zero",
    "QueryParameterTypes": ".query_parameter_types",
    "QueryParameterValue": ".query_parameter_value",
    "QueryParameters": ".query_parameters",
    "QueryRequest": ".query_request",
    "QueryRequest_Read": ".query_request",
    "QueryRequest_Write": ".query_request",
    "QueryResponse": ".query_response",
    "ReadBatchQuery": ".read_batch_query",
    "ReadQueryRequest": ".read_query_request",
    "WriteBatchQuery": ".write_batch_query",
    "WriteQueryRequest": ".write_query_request",
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
    "Batch",
    "BatchCondition",
    "BatchConditionVarEmpty",
    "BatchConditionVarMinSize",
    "BatchConditionVarNotEmpty",
    "BatchConditionZero",
    "BatchEntry",
    "BatchEntryForEach",
    "BatchEntryForEachForEach",
    "BatchEntryQuery",
    "HealthResponse",
    "NamedQuery",
    "OperationTree",
    "QueryError",
    "QueryParameterType",
    "QueryParameterTypeArray",
    "QueryParameterTypeZero",
    "QueryParameterTypes",
    "QueryParameterValue",
    "QueryParameters",
    "QueryRequest",
    "QueryRequest_Read",
    "QueryRequest_Write",
    "QueryResponse",
    "ReadBatchQuery",
    "ReadQueryRequest",
    "WriteBatchQuery",
    "WriteQueryRequest",
]
