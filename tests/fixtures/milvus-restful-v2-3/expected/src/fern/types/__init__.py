



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .alias_collection import AliasCollection
    from .alias_detail import AliasDetail
    from .code_ok import CodeOk
    from .code_ok_data import CodeOkData
    from .collection_name import CollectionName
    from .collection_params import CollectionParams
    from .collection_schema import CollectionSchema
    from .customer_create_index_resp import CustomerCreateIndexResp
    from .customer_delete_resp import CustomerDeleteResp
    from .customer_drop_collection_resp import CustomerDropCollectionResp
    from .customer_insert_resp import CustomerInsertResp
    from .db_name import DbName
    from .field_schema import FieldSchema
    from .field_schema_element_type_params import FieldSchemaElementTypeParams
    from .has import Has
    from .has_data import HasData
    from .http_return_code import HttpReturnCode
    from .httpapi_generic_resp_customer_create_index_resp import HttpapiGenericRespCustomerCreateIndexResp
    from .httpapi_generic_resp_customer_delete_resp import HttpapiGenericRespCustomerDeleteResp
    from .httpapi_generic_resp_customer_drop_collection_resp import HttpapiGenericRespCustomerDropCollectionResp
    from .httpapi_generic_resp_customer_insert_resp import HttpapiGenericRespCustomerInsertResp
    from .httpapi_generic_resp_customer_upsert_resp import HttpapiGenericRespCustomerUpsertResp
    from .httpapi_generic_resp_customer_upsert_resp_data import HttpapiGenericRespCustomerUpsertRespData
    from .index_config import IndexConfig
    from .index_detail import IndexDetail
    from .index_param import IndexParam
    from .index_state import IndexState
    from .load_state_collection_partition import LoadStateCollectionPartition
    from .load_state_collection_partition_data import LoadStateCollectionPartitionData
    from .message import Message
    from .names_collection_partition_user_role_index_alias import NamesCollectionPartitionUserRoleIndexAlias
    from .partition_name import PartitionName
    from .partition_names import PartitionNames
    from .privilege_entity import PrivilegeEntity
    from .privileges import Privileges
    from .role_name import RoleName
    from .role_user import RoleUser
    from .row_count_collection_partition import RowCountCollectionPartition
    from .row_count_collection_partition_data import RowCountCollectionPartitionData
    from .search_params import SearchParams
    from .timeout import Timeout
    from .vector import Vector
    from .vector_item import VectorItem
_dynamic_imports: typing.Dict[str, str] = {
    "AliasCollection": ".alias_collection",
    "AliasDetail": ".alias_detail",
    "CodeOk": ".code_ok",
    "CodeOkData": ".code_ok_data",
    "CollectionName": ".collection_name",
    "CollectionParams": ".collection_params",
    "CollectionSchema": ".collection_schema",
    "CustomerCreateIndexResp": ".customer_create_index_resp",
    "CustomerDeleteResp": ".customer_delete_resp",
    "CustomerDropCollectionResp": ".customer_drop_collection_resp",
    "CustomerInsertResp": ".customer_insert_resp",
    "DbName": ".db_name",
    "FieldSchema": ".field_schema",
    "FieldSchemaElementTypeParams": ".field_schema_element_type_params",
    "Has": ".has",
    "HasData": ".has_data",
    "HttpReturnCode": ".http_return_code",
    "HttpapiGenericRespCustomerCreateIndexResp": ".httpapi_generic_resp_customer_create_index_resp",
    "HttpapiGenericRespCustomerDeleteResp": ".httpapi_generic_resp_customer_delete_resp",
    "HttpapiGenericRespCustomerDropCollectionResp": ".httpapi_generic_resp_customer_drop_collection_resp",
    "HttpapiGenericRespCustomerInsertResp": ".httpapi_generic_resp_customer_insert_resp",
    "HttpapiGenericRespCustomerUpsertResp": ".httpapi_generic_resp_customer_upsert_resp",
    "HttpapiGenericRespCustomerUpsertRespData": ".httpapi_generic_resp_customer_upsert_resp_data",
    "IndexConfig": ".index_config",
    "IndexDetail": ".index_detail",
    "IndexParam": ".index_param",
    "IndexState": ".index_state",
    "LoadStateCollectionPartition": ".load_state_collection_partition",
    "LoadStateCollectionPartitionData": ".load_state_collection_partition_data",
    "Message": ".message",
    "NamesCollectionPartitionUserRoleIndexAlias": ".names_collection_partition_user_role_index_alias",
    "PartitionName": ".partition_name",
    "PartitionNames": ".partition_names",
    "PrivilegeEntity": ".privilege_entity",
    "Privileges": ".privileges",
    "RoleName": ".role_name",
    "RoleUser": ".role_user",
    "RowCountCollectionPartition": ".row_count_collection_partition",
    "RowCountCollectionPartitionData": ".row_count_collection_partition_data",
    "SearchParams": ".search_params",
    "Timeout": ".timeout",
    "Vector": ".vector",
    "VectorItem": ".vector_item",
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
    "AliasCollection",
    "AliasDetail",
    "CodeOk",
    "CodeOkData",
    "CollectionName",
    "CollectionParams",
    "CollectionSchema",
    "CustomerCreateIndexResp",
    "CustomerDeleteResp",
    "CustomerDropCollectionResp",
    "CustomerInsertResp",
    "DbName",
    "FieldSchema",
    "FieldSchemaElementTypeParams",
    "Has",
    "HasData",
    "HttpReturnCode",
    "HttpapiGenericRespCustomerCreateIndexResp",
    "HttpapiGenericRespCustomerDeleteResp",
    "HttpapiGenericRespCustomerDropCollectionResp",
    "HttpapiGenericRespCustomerInsertResp",
    "HttpapiGenericRespCustomerUpsertResp",
    "HttpapiGenericRespCustomerUpsertRespData",
    "IndexConfig",
    "IndexDetail",
    "IndexParam",
    "IndexState",
    "LoadStateCollectionPartition",
    "LoadStateCollectionPartitionData",
    "Message",
    "NamesCollectionPartitionUserRoleIndexAlias",
    "PartitionName",
    "PartitionNames",
    "PrivilegeEntity",
    "Privileges",
    "RoleName",
    "RoleUser",
    "RowCountCollectionPartition",
    "RowCountCollectionPartitionData",
    "SearchParams",
    "Timeout",
    "Vector",
    "VectorItem",
]
