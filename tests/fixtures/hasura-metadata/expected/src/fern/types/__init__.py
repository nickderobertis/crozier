



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .action_definition_mutation_graph_ql_type_input_webhook import ActionDefinitionMutationGraphQlTypeInputWebhook
    from .action_definition_mutation_graph_ql_type_input_webhook_headers_item import (
        ActionDefinitionMutationGraphQlTypeInputWebhookHeadersItem,
    )
    from .action_definition_mutation_graph_ql_type_input_webhook_kind import (
        ActionDefinitionMutationGraphQlTypeInputWebhookKind,
    )
    from .action_definition_mutation_graph_ql_type_input_webhook_request_transform import (
        ActionDefinitionMutationGraphQlTypeInputWebhookRequestTransform,
    )
    from .action_definition_mutation_graph_ql_type_input_webhook_response_transform import (
        ActionDefinitionMutationGraphQlTypeInputWebhookResponseTransform,
    )
    from .action_definition_query_graph_ql_type_input_webhook import ActionDefinitionQueryGraphQlTypeInputWebhook
    from .action_definition_query_graph_ql_type_input_webhook_headers_item import (
        ActionDefinitionQueryGraphQlTypeInputWebhookHeadersItem,
    )
    from .action_definition_query_graph_ql_type_input_webhook_request_transform import (
        ActionDefinitionQueryGraphQlTypeInputWebhookRequestTransform,
    )
    from .action_definition_query_graph_ql_type_input_webhook_response_transform import (
        ActionDefinitionQueryGraphQlTypeInputWebhookResponseTransform,
    )
    from .action_metadata import ActionMetadata
    from .action_metadata_definition import (
        ActionMetadataDefinition,
        ActionMetadataDefinition_Mutation,
        ActionMetadataDefinition_Query,
    )
    from .action_permission_metadata import ActionPermissionMetadata
    from .add_replace_or_remove_fields import AddReplaceOrRemoveFields
    from .allowlist_entry import AllowlistEntry
    from .allowlist_entry_scope import AllowlistEntryScope
    from .allowlist_scope_global import AllowlistScopeGlobal
    from .allowlist_scope_roles import AllowlistScopeRoles
    from .api_limit import ApiLimit
    from .apollo_federation_config import ApolloFederationConfig
    from .apollo_federation_config_enable import ApolloFederationConfigEnable
    from .argument_definition_graph_ql_type import ArgumentDefinitionGraphQlType
    from .auto_trigger_log_cleanup_config import AutoTriggerLogCleanupConfig
    from .backend_map_backend_config_wrapper import BackendMapBackendConfigWrapper
    from .big_query_computed_field_definition import BigQueryComputedFieldDefinition
    from .big_query_conn_source_config import BigQueryConnSourceConfig
    from .big_query_conn_source_config_datasets import BigQueryConnSourceConfigDatasets
    from .big_query_conn_source_config_global_select_limit import BigQueryConnSourceConfigGlobalSelectLimit
    from .big_query_conn_source_config_project_id import BigQueryConnSourceConfigProjectId
    from .big_query_conn_source_config_retry_base_delay import BigQueryConnSourceConfigRetryBaseDelay
    from .big_query_conn_source_config_retry_limit import BigQueryConnSourceConfigRetryLimit
    from .big_query_function_name import BigQueryFunctionName
    from .big_query_service_account import BigQueryServiceAccount
    from .big_query_table_name import BigQueryTableName
    from .bigquery_arr_rel_using_f_key_on_multiple_columns import BigqueryArrRelUsingFKeyOnMultipleColumns
    from .bigquery_arr_rel_using_f_key_on_single_column import BigqueryArrRelUsingFKeyOnSingleColumn
    from .bigquery_bool_exp import BigqueryBoolExp
    from .bigquery_computed_field_metadata import BigqueryComputedFieldMetadata
    from .bigquery_del_perm import BigqueryDelPerm
    from .bigquery_delete_perm_def import BigqueryDeletePermDef
    from .bigquery_function_metadata import BigqueryFunctionMetadata
    from .bigquery_ins_perm import BigqueryInsPerm
    from .bigquery_ins_perm_columns import BigqueryInsPermColumns
    from .bigquery_ins_perm_columns_zero import BigqueryInsPermColumnsZero
    from .bigquery_insert_perm_def import BigqueryInsertPermDef
    from .bigquery_logical_model_field import BigqueryLogicalModelField
    from .bigquery_logical_model_metadata import BigqueryLogicalModelMetadata
    from .bigquery_native_query_metadata import BigqueryNativeQueryMetadata
    from .bigquery_nullable_scalar_type import BigqueryNullableScalarType
    from .bigquery_obj_rel_remote_table_multiple_columns import BigqueryObjRelRemoteTableMultipleColumns
    from .bigquery_obj_rel_remote_table_single_column import BigqueryObjRelRemoteTableSingleColumn
    from .bigquery_rel_manual_native_query_config import BigqueryRelManualNativeQueryConfig
    from .bigquery_rel_manual_native_query_config_insertion_order import (
        BigqueryRelManualNativeQueryConfigInsertionOrder,
    )
    from .bigquery_rel_manual_table_config import BigqueryRelManualTableConfig
    from .bigquery_rel_manual_table_config_insertion_order import BigqueryRelManualTableConfigInsertionOrder
    from .bigquery_ru_manual import BigqueryRuManual
    from .bigquery_sel_perm import BigquerySelPerm
    from .bigquery_sel_perm_columns import BigquerySelPermColumns
    from .bigquery_sel_perm_columns_zero import BigquerySelPermColumnsZero
    from .bigquery_sel_perm_query_root_fields_item import BigquerySelPermQueryRootFieldsItem
    from .bigquery_sel_perm_subscription_root_fields_item import BigquerySelPermSubscriptionRootFieldsItem
    from .bigquery_select_perm_def import BigquerySelectPermDef
    from .bigquery_source_metadata import BigquerySourceMetadata
    from .bigquery_source_metadata_kind import BigquerySourceMetadataKind
    from .bigquery_stored_procedure_metadata import BigqueryStoredProcedureMetadata
    from .bigquery_table_config import BigqueryTableConfig
    from .bigquery_table_metadata import BigqueryTableMetadata
    from .bigquery_upd_perm import BigqueryUpdPerm
    from .bigquery_upd_perm_columns import BigqueryUpdPermColumns
    from .bigquery_upd_perm_columns_zero import BigqueryUpdPermColumnsZero
    from .bigquery_update_perm_def import BigqueryUpdatePermDef
    from .body_transform_fn_modify_as_form_url_encoded import BodyTransformFnModifyAsFormUrlEncoded
    from .body_transform_fn_modify_as_json import BodyTransformFnModifyAsJson
    from .body_transform_fn_remove import BodyTransformFnRemove
    from .cert_var import CertVar
    from .citus_arr_rel_using_f_key_on_multiple_columns import CitusArrRelUsingFKeyOnMultipleColumns
    from .citus_arr_rel_using_f_key_on_single_column import CitusArrRelUsingFKeyOnSingleColumn
    from .citus_bool_exp import CitusBoolExp
    from .citus_computed_field_metadata import CitusComputedFieldMetadata
    from .citus_del_perm import CitusDelPerm
    from .citus_delete_perm_def import CitusDeletePermDef
    from .citus_event_trigger_conf_event_trigger_conf import CitusEventTriggerConfEventTriggerConf
    from .citus_event_trigger_conf_event_trigger_conf_headers_item import (
        CitusEventTriggerConfEventTriggerConfHeadersItem,
    )
    from .citus_event_trigger_conf_event_trigger_conf_request_transform import (
        CitusEventTriggerConfEventTriggerConfRequestTransform,
    )
    from .citus_event_trigger_conf_event_trigger_conf_response_transform import (
        CitusEventTriggerConfEventTriggerConfResponseTransform,
    )
    from .citus_function_metadata import CitusFunctionMetadata
    from .citus_health_check_config import CitusHealthCheckConfig
    from .citus_ins_perm import CitusInsPerm
    from .citus_ins_perm_columns import CitusInsPermColumns
    from .citus_ins_perm_columns_zero import CitusInsPermColumnsZero
    from .citus_insert_perm_def import CitusInsertPermDef
    from .citus_logical_model_field import CitusLogicalModelField
    from .citus_logical_model_metadata import CitusLogicalModelMetadata
    from .citus_native_query_metadata import CitusNativeQueryMetadata
    from .citus_nullable_scalar_type import CitusNullableScalarType
    from .citus_obj_rel_remote_table_multiple_columns import CitusObjRelRemoteTableMultipleColumns
    from .citus_obj_rel_remote_table_single_column import CitusObjRelRemoteTableSingleColumn
    from .citus_rel_manual_native_query_config import CitusRelManualNativeQueryConfig
    from .citus_rel_manual_native_query_config_insertion_order import CitusRelManualNativeQueryConfigInsertionOrder
    from .citus_rel_manual_table_config import CitusRelManualTableConfig
    from .citus_rel_manual_table_config_insertion_order import CitusRelManualTableConfigInsertionOrder
    from .citus_ru_manual import CitusRuManual
    from .citus_sel_perm import CitusSelPerm
    from .citus_sel_perm_columns import CitusSelPermColumns
    from .citus_sel_perm_columns_zero import CitusSelPermColumnsZero
    from .citus_sel_perm_query_root_fields_item import CitusSelPermQueryRootFieldsItem
    from .citus_sel_perm_subscription_root_fields_item import CitusSelPermSubscriptionRootFieldsItem
    from .citus_select_perm_def import CitusSelectPermDef
    from .citus_source_metadata import CitusSourceMetadata
    from .citus_source_metadata_kind import CitusSourceMetadataKind
    from .citus_stored_procedure_metadata import CitusStoredProcedureMetadata
    from .citus_subscribe_op_spec import CitusSubscribeOpSpec
    from .citus_subscribe_op_spec_columns import CitusSubscribeOpSpecColumns
    from .citus_subscribe_op_spec_columns_zero import CitusSubscribeOpSpecColumnsZero
    from .citus_subscribe_op_spec_payload import CitusSubscribeOpSpecPayload
    from .citus_subscribe_op_spec_payload_zero import CitusSubscribeOpSpecPayloadZero
    from .citus_table_config import CitusTableConfig
    from .citus_table_metadata import CitusTableMetadata
    from .citus_trigger_ops_def import CitusTriggerOpsDef
    from .citus_upd_perm import CitusUpdPerm
    from .citus_upd_perm_columns import CitusUpdPermColumns
    from .citus_upd_perm_columns_zero import CitusUpdPermColumnsZero
    from .citus_update_perm_def import CitusUpdatePermDef
    from .cockroach_arr_rel_using_f_key_on_multiple_columns import CockroachArrRelUsingFKeyOnMultipleColumns
    from .cockroach_arr_rel_using_f_key_on_single_column import CockroachArrRelUsingFKeyOnSingleColumn
    from .cockroach_bool_exp import CockroachBoolExp
    from .cockroach_computed_field_metadata import CockroachComputedFieldMetadata
    from .cockroach_del_perm import CockroachDelPerm
    from .cockroach_delete_perm_def import CockroachDeletePermDef
    from .cockroach_event_trigger_conf_event_trigger_conf import CockroachEventTriggerConfEventTriggerConf
    from .cockroach_event_trigger_conf_event_trigger_conf_headers_item import (
        CockroachEventTriggerConfEventTriggerConfHeadersItem,
    )
    from .cockroach_event_trigger_conf_event_trigger_conf_request_transform import (
        CockroachEventTriggerConfEventTriggerConfRequestTransform,
    )
    from .cockroach_event_trigger_conf_event_trigger_conf_response_transform import (
        CockroachEventTriggerConfEventTriggerConfResponseTransform,
    )
    from .cockroach_function_metadata import CockroachFunctionMetadata
    from .cockroach_health_check_config import CockroachHealthCheckConfig
    from .cockroach_ins_perm import CockroachInsPerm
    from .cockroach_ins_perm_columns import CockroachInsPermColumns
    from .cockroach_ins_perm_columns_zero import CockroachInsPermColumnsZero
    from .cockroach_insert_perm_def import CockroachInsertPermDef
    from .cockroach_logical_model_field import CockroachLogicalModelField
    from .cockroach_logical_model_metadata import CockroachLogicalModelMetadata
    from .cockroach_native_query_metadata import CockroachNativeQueryMetadata
    from .cockroach_nullable_scalar_type import CockroachNullableScalarType
    from .cockroach_obj_rel_remote_table_multiple_columns import CockroachObjRelRemoteTableMultipleColumns
    from .cockroach_obj_rel_remote_table_single_column import CockroachObjRelRemoteTableSingleColumn
    from .cockroach_rel_manual_native_query_config import CockroachRelManualNativeQueryConfig
    from .cockroach_rel_manual_native_query_config_insertion_order import (
        CockroachRelManualNativeQueryConfigInsertionOrder,
    )
    from .cockroach_rel_manual_table_config import CockroachRelManualTableConfig
    from .cockroach_rel_manual_table_config_insertion_order import CockroachRelManualTableConfigInsertionOrder
    from .cockroach_ru_manual import CockroachRuManual
    from .cockroach_sel_perm import CockroachSelPerm
    from .cockroach_sel_perm_columns import CockroachSelPermColumns
    from .cockroach_sel_perm_columns_zero import CockroachSelPermColumnsZero
    from .cockroach_sel_perm_query_root_fields_item import CockroachSelPermQueryRootFieldsItem
    from .cockroach_sel_perm_subscription_root_fields_item import CockroachSelPermSubscriptionRootFieldsItem
    from .cockroach_select_perm_def import CockroachSelectPermDef
    from .cockroach_source_metadata import CockroachSourceMetadata
    from .cockroach_source_metadata_kind import CockroachSourceMetadataKind
    from .cockroach_stored_procedure_metadata import CockroachStoredProcedureMetadata
    from .cockroach_subscribe_op_spec import CockroachSubscribeOpSpec
    from .cockroach_subscribe_op_spec_columns import CockroachSubscribeOpSpecColumns
    from .cockroach_subscribe_op_spec_columns_zero import CockroachSubscribeOpSpecColumnsZero
    from .cockroach_subscribe_op_spec_payload import CockroachSubscribeOpSpecPayload
    from .cockroach_subscribe_op_spec_payload_zero import CockroachSubscribeOpSpecPayloadZero
    from .cockroach_table_config import CockroachTableConfig
    from .cockroach_table_metadata import CockroachTableMetadata
    from .cockroach_trigger_ops_def import CockroachTriggerOpsDef
    from .cockroach_upd_perm import CockroachUpdPerm
    from .cockroach_upd_perm_columns import CockroachUpdPermColumns
    from .cockroach_upd_perm_columns_zero import CockroachUpdPermColumnsZero
    from .cockroach_update_perm_def import CockroachUpdatePermDef
    from .collection_def import CollectionDef
    from .column_config import ColumnConfig
    from .config import Config
    from .connection_template import ConnectionTemplate
    from .create_collection import CreateCollection
    from .cron_schedule import CronSchedule
    from .cron_trigger_metadata import CronTriggerMetadata
    from .cron_trigger_metadata_headers_item import CronTriggerMetadataHeadersItem
    from .cron_trigger_metadata_request_transform import CronTriggerMetadataRequestTransform
    from .cron_trigger_metadata_response_transform import CronTriggerMetadataResponseTransform
    from .custom_root_field import CustomRootField
    from .custom_types import CustomTypes
    from .data_connector_conn_source_config import DataConnectorConnSourceConfig
    from .data_connector_conn_source_config_timeout import DataConnectorConnSourceConfigTimeout
    from .data_connector_options import DataConnectorOptions
    from .data_connector_options_uri import DataConnectorOptionsUri
    from .data_connector_source_timeout_microseconds import DataConnectorSourceTimeoutMicroseconds
    from .data_connector_source_timeout_milliseconds import DataConnectorSourceTimeoutMilliseconds
    from .data_connector_source_timeout_seconds import DataConnectorSourceTimeoutSeconds
    from .dataconnector_arr_rel_using_f_key_on_multiple_columns import DataconnectorArrRelUsingFKeyOnMultipleColumns
    from .dataconnector_arr_rel_using_f_key_on_multiple_columns_columns_item import (
        DataconnectorArrRelUsingFKeyOnMultipleColumnsColumnsItem,
    )
    from .dataconnector_arr_rel_using_f_key_on_single_column import DataconnectorArrRelUsingFKeyOnSingleColumn
    from .dataconnector_arr_rel_using_f_key_on_single_column_column import (
        DataconnectorArrRelUsingFKeyOnSingleColumnColumn,
    )
    from .dataconnector_bool_exp import DataconnectorBoolExp
    from .dataconnector_computed_field_metadata import DataconnectorComputedFieldMetadata
    from .dataconnector_del_perm import DataconnectorDelPerm
    from .dataconnector_delete_perm_def import DataconnectorDeletePermDef
    from .dataconnector_function_metadata import DataconnectorFunctionMetadata
    from .dataconnector_ins_perm import DataconnectorInsPerm
    from .dataconnector_ins_perm_columns import DataconnectorInsPermColumns
    from .dataconnector_ins_perm_columns_zero import DataconnectorInsPermColumnsZero
    from .dataconnector_insert_perm_def import DataconnectorInsertPermDef
    from .dataconnector_logical_model_field import DataconnectorLogicalModelField
    from .dataconnector_logical_model_metadata import DataconnectorLogicalModelMetadata
    from .dataconnector_native_query_metadata import DataconnectorNativeQueryMetadata
    from .dataconnector_nullable_scalar_type import DataconnectorNullableScalarType
    from .dataconnector_obj_rel_remote_table_multiple_columns import DataconnectorObjRelRemoteTableMultipleColumns
    from .dataconnector_obj_rel_remote_table_multiple_columns_columns_item import (
        DataconnectorObjRelRemoteTableMultipleColumnsColumnsItem,
    )
    from .dataconnector_obj_rel_remote_table_single_column import DataconnectorObjRelRemoteTableSingleColumn
    from .dataconnector_obj_rel_remote_table_single_column_column import (
        DataconnectorObjRelRemoteTableSingleColumnColumn,
    )
    from .dataconnector_rel_manual_native_query_config import DataconnectorRelManualNativeQueryConfig
    from .dataconnector_rel_manual_native_query_config_insertion_order import (
        DataconnectorRelManualNativeQueryConfigInsertionOrder,
    )
    from .dataconnector_rel_manual_table_config import DataconnectorRelManualTableConfig
    from .dataconnector_rel_manual_table_config_insertion_order import DataconnectorRelManualTableConfigInsertionOrder
    from .dataconnector_ru_manual import DataconnectorRuManual
    from .dataconnector_sel_perm import DataconnectorSelPerm
    from .dataconnector_sel_perm_columns import DataconnectorSelPermColumns
    from .dataconnector_sel_perm_columns_zero import DataconnectorSelPermColumnsZero
    from .dataconnector_sel_perm_query_root_fields_item import DataconnectorSelPermQueryRootFieldsItem
    from .dataconnector_sel_perm_subscription_root_fields_item import DataconnectorSelPermSubscriptionRootFieldsItem
    from .dataconnector_select_perm_def import DataconnectorSelectPermDef
    from .dataconnector_source_metadata import DataconnectorSourceMetadata
    from .dataconnector_stored_procedure_metadata import DataconnectorStoredProcedureMetadata
    from .dataconnector_table_config import DataconnectorTableConfig
    from .dataconnector_table_metadata import DataconnectorTableMetadata
    from .dataconnector_upd_perm import DataconnectorUpdPerm
    from .dataconnector_upd_perm_columns import DataconnectorUpdPermColumns
    from .dataconnector_upd_perm_columns_zero import DataconnectorUpdPermColumnsZero
    from .dataconnector_update_perm_def import DataconnectorUpdatePermDef
    from .endpoint_def_query_reference import EndpointDefQueryReference
    from .endpoint_metadata_query_reference import EndpointMetadataQueryReference
    from .endpoint_metadata_query_reference_methods_item import EndpointMetadataQueryReferenceMethodsItem
    from .enum_type_definition import EnumTypeDefinition
    from .enum_value_definition import EnumValueDefinition
    from .extensions_schema import ExtensionsSchema
    from .field_call import FieldCall
    from .from_env import FromEnv
    from .function_config import FunctionConfig
    from .function_config_exposed_as import FunctionConfigExposedAs
    from .function_custom_root_fields import FunctionCustomRootFields
    from .function_permission_info import FunctionPermissionInfo
    from .function_return_type import FunctionReturnType
    from .graph_ql_name import GraphQlName
    from .graph_ql_schema import GraphQlSchema
    from .graph_ql_value_name import GraphQlValueName
    from .header_conf_from_env import HeaderConfFromEnv
    from .header_conf_value import HeaderConfValue
    from .health_check_test_sql import HealthCheckTestSql
    from .inferred_function_response import InferredFunctionResponse
    from .inferred_function_response_type import InferredFunctionResponseType
    from .input_object_field_definition import InputObjectFieldDefinition
    from .input_object_type_definition import InputObjectTypeDefinition
    from .limit_max_batch_size import LimitMaxBatchSize
    from .limit_max_depth import LimitMaxDepth
    from .limit_max_nodes import LimitMaxNodes
    from .limit_max_time import LimitMaxTime
    from .limit_rate_limit_config import LimitRateLimitConfig
    from .listed_query import ListedQuery
    from .metadata import Metadata
    from .metadata_v1 import MetadataV1
    from .metadata_v2 import MetadataV2
    from .metadata_v3 import MetadataV3
    from .metrics_config import MetricsConfig
    from .mssql_arr_rel_using_f_key_on_multiple_columns import MssqlArrRelUsingFKeyOnMultipleColumns
    from .mssql_arr_rel_using_f_key_on_single_column import MssqlArrRelUsingFKeyOnSingleColumn
    from .mssql_bool_exp import MssqlBoolExp
    from .mssql_computed_field_metadata import MssqlComputedFieldMetadata
    from .mssql_conn_configuration import MssqlConnConfiguration
    from .mssql_connection_info import MssqlConnectionInfo
    from .mssql_connection_info_connection_string import MssqlConnectionInfoConnectionString
    from .mssql_del_perm import MssqlDelPerm
    from .mssql_delete_perm_def import MssqlDeletePermDef
    from .mssql_event_trigger_conf_event_trigger_conf import MssqlEventTriggerConfEventTriggerConf
    from .mssql_event_trigger_conf_event_trigger_conf_headers_item import (
        MssqlEventTriggerConfEventTriggerConfHeadersItem,
    )
    from .mssql_event_trigger_conf_event_trigger_conf_request_transform import (
        MssqlEventTriggerConfEventTriggerConfRequestTransform,
    )
    from .mssql_event_trigger_conf_event_trigger_conf_response_transform import (
        MssqlEventTriggerConfEventTriggerConfResponseTransform,
    )
    from .mssql_function_metadata import MssqlFunctionMetadata
    from .mssql_function_name import MssqlFunctionName
    from .mssql_health_check_config import MssqlHealthCheckConfig
    from .mssql_ins_perm import MssqlInsPerm
    from .mssql_ins_perm_columns import MssqlInsPermColumns
    from .mssql_ins_perm_columns_zero import MssqlInsPermColumnsZero
    from .mssql_insert_perm_def import MssqlInsertPermDef
    from .mssql_logical_model_field import MssqlLogicalModelField
    from .mssql_logical_model_metadata import MssqlLogicalModelMetadata
    from .mssql_native_query_metadata import MssqlNativeQueryMetadata
    from .mssql_nullable_scalar_type import MssqlNullableScalarType
    from .mssql_obj_rel_remote_table_multiple_columns import MssqlObjRelRemoteTableMultipleColumns
    from .mssql_obj_rel_remote_table_single_column import MssqlObjRelRemoteTableSingleColumn
    from .mssql_pool_settings import MssqlPoolSettings
    from .mssql_rel_manual_native_query_config import MssqlRelManualNativeQueryConfig
    from .mssql_rel_manual_native_query_config_insertion_order import MssqlRelManualNativeQueryConfigInsertionOrder
    from .mssql_rel_manual_table_config import MssqlRelManualTableConfig
    from .mssql_rel_manual_table_config_insertion_order import MssqlRelManualTableConfigInsertionOrder
    from .mssql_ru_manual import MssqlRuManual
    from .mssql_sel_perm import MssqlSelPerm
    from .mssql_sel_perm_columns import MssqlSelPermColumns
    from .mssql_sel_perm_columns_zero import MssqlSelPermColumnsZero
    from .mssql_sel_perm_query_root_fields_item import MssqlSelPermQueryRootFieldsItem
    from .mssql_sel_perm_subscription_root_fields_item import MssqlSelPermSubscriptionRootFieldsItem
    from .mssql_select_perm_def import MssqlSelectPermDef
    from .mssql_source_metadata import MssqlSourceMetadata
    from .mssql_source_metadata_kind import MssqlSourceMetadataKind
    from .mssql_stored_procedure_metadata import MssqlStoredProcedureMetadata
    from .mssql_subscribe_op_spec import MssqlSubscribeOpSpec
    from .mssql_subscribe_op_spec_columns import MssqlSubscribeOpSpecColumns
    from .mssql_subscribe_op_spec_columns_zero import MssqlSubscribeOpSpecColumnsZero
    from .mssql_subscribe_op_spec_payload import MssqlSubscribeOpSpecPayload
    from .mssql_subscribe_op_spec_payload_zero import MssqlSubscribeOpSpecPayloadZero
    from .mssql_table_config import MssqlTableConfig
    from .mssql_table_metadata import MssqlTableMetadata
    from .mssql_table_name import MssqlTableName
    from .mssql_trigger_ops_def import MssqlTriggerOpsDef
    from .mssql_upd_perm import MssqlUpdPerm
    from .mssql_upd_perm_columns import MssqlUpdPermColumns
    from .mssql_upd_perm_columns_zero import MssqlUpdPermColumnsZero
    from .mssql_update_perm_def import MssqlUpdatePermDef
    from .naming_case import NamingCase
    from .network import Network
    from .object_field_definition_graph_ql_type import ObjectFieldDefinitionGraphQlType
    from .object_type_definition import ObjectTypeDefinition
    from .open_telemetry_config import OpenTelemetryConfig
    from .open_telemetry_config_data_types_item import OpenTelemetryConfigDataTypesItem
    from .otel_batch_span_processor_config import OtelBatchSpanProcessorConfig
    from .otel_exporter_config import OtelExporterConfig
    from .otel_exporter_config_headers_item import OtelExporterConfigHeadersItem
    from .otel_exporter_config_protocol import OtelExporterConfigProtocol
    from .otel_exporter_config_traces_propagators_item import OtelExporterConfigTracesPropagatorsItem
    from .otel_name_value import OtelNameValue
    from .pg_client_certs import PgClientCerts
    from .pg_connection_params import PgConnectionParams
    from .postgres_arr_rel_using_f_key_on_multiple_columns import PostgresArrRelUsingFKeyOnMultipleColumns
    from .postgres_arr_rel_using_f_key_on_single_column import PostgresArrRelUsingFKeyOnSingleColumn
    from .postgres_bool_exp import PostgresBoolExp
    from .postgres_computed_field_definition import PostgresComputedFieldDefinition
    from .postgres_computed_field_metadata import PostgresComputedFieldMetadata
    from .postgres_conn_configuration import PostgresConnConfiguration
    from .postgres_del_perm import PostgresDelPerm
    from .postgres_delete_perm_def import PostgresDeletePermDef
    from .postgres_event_trigger_conf_event_trigger_conf import PostgresEventTriggerConfEventTriggerConf
    from .postgres_event_trigger_conf_event_trigger_conf_headers_item import (
        PostgresEventTriggerConfEventTriggerConfHeadersItem,
    )
    from .postgres_event_trigger_conf_event_trigger_conf_request_transform import (
        PostgresEventTriggerConfEventTriggerConfRequestTransform,
    )
    from .postgres_event_trigger_conf_event_trigger_conf_response_transform import (
        PostgresEventTriggerConfEventTriggerConfResponseTransform,
    )
    from .postgres_function_metadata import PostgresFunctionMetadata
    from .postgres_health_check_config import PostgresHealthCheckConfig
    from .postgres_ins_perm import PostgresInsPerm
    from .postgres_ins_perm_columns import PostgresInsPermColumns
    from .postgres_ins_perm_columns_zero import PostgresInsPermColumnsZero
    from .postgres_insert_perm_def import PostgresInsertPermDef
    from .postgres_logical_model_field import PostgresLogicalModelField
    from .postgres_logical_model_metadata import PostgresLogicalModelMetadata
    from .postgres_native_query_metadata import PostgresNativeQueryMetadata
    from .postgres_nullable_scalar_type import PostgresNullableScalarType
    from .postgres_obj_rel_remote_table_multiple_columns import PostgresObjRelRemoteTableMultipleColumns
    from .postgres_obj_rel_remote_table_single_column import PostgresObjRelRemoteTableSingleColumn
    from .postgres_pool_settings import PostgresPoolSettings
    from .postgres_qualified_function_name import PostgresQualifiedFunctionName
    from .postgres_qualified_table_name import PostgresQualifiedTableName
    from .postgres_rel_manual_native_query_config import PostgresRelManualNativeQueryConfig
    from .postgres_rel_manual_native_query_config_insertion_order import (
        PostgresRelManualNativeQueryConfigInsertionOrder,
    )
    from .postgres_rel_manual_table_config import PostgresRelManualTableConfig
    from .postgres_rel_manual_table_config_insertion_order import PostgresRelManualTableConfigInsertionOrder
    from .postgres_ru_manual import PostgresRuManual
    from .postgres_sel_perm import PostgresSelPerm
    from .postgres_sel_perm_columns import PostgresSelPermColumns
    from .postgres_sel_perm_columns_zero import PostgresSelPermColumnsZero
    from .postgres_sel_perm_query_root_fields_item import PostgresSelPermQueryRootFieldsItem
    from .postgres_sel_perm_subscription_root_fields_item import PostgresSelPermSubscriptionRootFieldsItem
    from .postgres_select_perm_def import PostgresSelectPermDef
    from .postgres_source_conn_info import PostgresSourceConnInfo
    from .postgres_source_conn_info_database_url import PostgresSourceConnInfoDatabaseUrl
    from .postgres_source_metadata import PostgresSourceMetadata
    from .postgres_source_metadata_kind import PostgresSourceMetadataKind
    from .postgres_stored_procedure_metadata import PostgresStoredProcedureMetadata
    from .postgres_subscribe_op_spec import PostgresSubscribeOpSpec
    from .postgres_subscribe_op_spec_columns import PostgresSubscribeOpSpecColumns
    from .postgres_subscribe_op_spec_columns_zero import PostgresSubscribeOpSpecColumnsZero
    from .postgres_subscribe_op_spec_payload import PostgresSubscribeOpSpecPayload
    from .postgres_subscribe_op_spec_payload_zero import PostgresSubscribeOpSpecPayloadZero
    from .postgres_table_config import PostgresTableConfig
    from .postgres_table_metadata import PostgresTableMetadata
    from .postgres_trigger_ops_def import PostgresTriggerOpsDef
    from .postgres_upd_perm import PostgresUpdPerm
    from .postgres_upd_perm_columns import PostgresUpdPermColumns
    from .postgres_upd_perm_columns_zero import PostgresUpdPermColumnsZero
    from .postgres_update_perm_def import PostgresUpdatePermDef
    from .query_reference import QueryReference
    from .query_tags_config import QueryTagsConfig
    from .query_tags_format import QueryTagsFormat
    from .rate_limit_config import RateLimitConfig
    from .rate_limit_config_unique_params import RateLimitConfigUniqueParams
    from .rate_limit_config_unique_params_zero import RateLimitConfigUniqueParamsZero
    from .rel_def_rel_manual_config_big_query import RelDefRelManualConfigBigQuery
    from .rel_def_rel_manual_config_data_connector import RelDefRelManualConfigDataConnector
    from .rel_def_rel_manual_config_mssql import RelDefRelManualConfigMssql
    from .rel_def_rel_manual_config_postgres_citus import RelDefRelManualConfigPostgresCitus
    from .rel_def_rel_manual_config_postgres_cockroach import RelDefRelManualConfigPostgresCockroach
    from .rel_def_rel_manual_config_postgres_vanilla import RelDefRelManualConfigPostgresVanilla
    from .rel_def_rel_using_big_query_arr_rel_using_f_key_on_big_query import (
        RelDefRelUsingBigQueryArrRelUsingFKeyOnBigQuery,
    )
    from .rel_def_rel_using_big_query_arr_rel_using_f_key_on_big_query_using import (
        RelDefRelUsingBigQueryArrRelUsingFKeyOnBigQueryUsing,
    )
    from .rel_def_rel_using_big_query_obj_rel_using_choice_big_query import (
        RelDefRelUsingBigQueryObjRelUsingChoiceBigQuery,
    )
    from .rel_def_rel_using_big_query_obj_rel_using_choice_big_query_using import (
        RelDefRelUsingBigQueryObjRelUsingChoiceBigQueryUsing,
    )
    from .rel_def_rel_using_data_connector_arr_rel_using_f_key_on_data_connector import (
        RelDefRelUsingDataConnectorArrRelUsingFKeyOnDataConnector,
    )
    from .rel_def_rel_using_data_connector_arr_rel_using_f_key_on_data_connector_using import (
        RelDefRelUsingDataConnectorArrRelUsingFKeyOnDataConnectorUsing,
    )
    from .rel_def_rel_using_data_connector_obj_rel_using_choice_data_connector import (
        RelDefRelUsingDataConnectorObjRelUsingChoiceDataConnector,
    )
    from .rel_def_rel_using_data_connector_obj_rel_using_choice_data_connector_using import (
        RelDefRelUsingDataConnectorObjRelUsingChoiceDataConnectorUsing,
    )
    from .rel_def_rel_using_mssql_arr_rel_using_f_key_on_mssql import RelDefRelUsingMssqlArrRelUsingFKeyOnMssql
    from .rel_def_rel_using_mssql_arr_rel_using_f_key_on_mssql_using import (
        RelDefRelUsingMssqlArrRelUsingFKeyOnMssqlUsing,
    )
    from .rel_def_rel_using_mssql_obj_rel_using_choice_mssql import RelDefRelUsingMssqlObjRelUsingChoiceMssql
    from .rel_def_rel_using_mssql_obj_rel_using_choice_mssql_using import RelDefRelUsingMssqlObjRelUsingChoiceMssqlUsing
    from .rel_def_rel_using_postgres_citus_arr_rel_using_f_key_on_postgres_citus import (
        RelDefRelUsingPostgresCitusArrRelUsingFKeyOnPostgresCitus,
    )
    from .rel_def_rel_using_postgres_citus_arr_rel_using_f_key_on_postgres_citus_using import (
        RelDefRelUsingPostgresCitusArrRelUsingFKeyOnPostgresCitusUsing,
    )
    from .rel_def_rel_using_postgres_citus_obj_rel_using_choice_postgres_citus import (
        RelDefRelUsingPostgresCitusObjRelUsingChoicePostgresCitus,
    )
    from .rel_def_rel_using_postgres_citus_obj_rel_using_choice_postgres_citus_using import (
        RelDefRelUsingPostgresCitusObjRelUsingChoicePostgresCitusUsing,
    )
    from .rel_def_rel_using_postgres_cockroach_arr_rel_using_f_key_on_postgres_cockroach import (
        RelDefRelUsingPostgresCockroachArrRelUsingFKeyOnPostgresCockroach,
    )
    from .rel_def_rel_using_postgres_cockroach_arr_rel_using_f_key_on_postgres_cockroach_using import (
        RelDefRelUsingPostgresCockroachArrRelUsingFKeyOnPostgresCockroachUsing,
    )
    from .rel_def_rel_using_postgres_cockroach_obj_rel_using_choice_postgres_cockroach import (
        RelDefRelUsingPostgresCockroachObjRelUsingChoicePostgresCockroach,
    )
    from .rel_def_rel_using_postgres_cockroach_obj_rel_using_choice_postgres_cockroach_using import (
        RelDefRelUsingPostgresCockroachObjRelUsingChoicePostgresCockroachUsing,
    )
    from .rel_def_rel_using_postgres_vanilla_arr_rel_using_f_key_on_postgres_vanilla import (
        RelDefRelUsingPostgresVanillaArrRelUsingFKeyOnPostgresVanilla,
    )
    from .rel_def_rel_using_postgres_vanilla_arr_rel_using_f_key_on_postgres_vanilla_using import (
        RelDefRelUsingPostgresVanillaArrRelUsingFKeyOnPostgresVanillaUsing,
    )
    from .rel_def_rel_using_postgres_vanilla_obj_rel_using_choice_postgres_vanilla import (
        RelDefRelUsingPostgresVanillaObjRelUsingChoicePostgresVanilla,
    )
    from .rel_def_rel_using_postgres_vanilla_obj_rel_using_choice_postgres_vanilla_using import (
        RelDefRelUsingPostgresVanillaObjRelUsingChoicePostgresVanillaUsing,
    )
    from .relationship_to_schema import RelationshipToSchema
    from .relationship_to_source import RelationshipToSource
    from .remote_arguments import RemoteArguments
    from .remote_field_customization import RemoteFieldCustomization
    from .remote_fields import RemoteFields
    from .remote_relationship_remote_relationship_definition import RemoteRelationshipRemoteRelationshipDefinition
    from .remote_relationship_remote_relationship_definition_definition import (
        RemoteRelationshipRemoteRelationshipDefinitionDefinition,
    )
    from .remote_schema_customization import RemoteSchemaCustomization
    from .remote_schema_def import RemoteSchemaDef
    from .remote_schema_def_headers_item import RemoteSchemaDefHeadersItem
    from .remote_schema_def_introspection_headers_item import RemoteSchemaDefIntrospectionHeadersItem
    from .remote_schema_metadata_remote_relationship_definition import RemoteSchemaMetadataRemoteRelationshipDefinition
    from .remote_schema_permission_definition import RemoteSchemaPermissionDefinition
    from .remote_schema_permission_metadata import RemoteSchemaPermissionMetadata
    from .remote_type_customization import RemoteTypeCustomization
    from .request_transform_v1 import RequestTransformV1
    from .request_transform_v1query_params import RequestTransformV1QueryParams
    from .request_transform_v1template_engine import RequestTransformV1TemplateEngine
    from .request_transform_v2 import RequestTransformV2
    from .request_transform_v2body import (
        RequestTransformV2Body,
        RequestTransformV2Body_Remove,
        RequestTransformV2Body_Transform,
        RequestTransformV2Body_XWwwFormUrlencoded,
    )
    from .request_transform_v2query_params import RequestTransformV2QueryParams
    from .request_transform_v2template_engine import RequestTransformV2TemplateEngine
    from .response_transform_v1 import ResponseTransformV1
    from .response_transform_v1template_engine import ResponseTransformV1TemplateEngine
    from .response_transform_v2 import ResponseTransformV2
    from .response_transform_v2body import (
        ResponseTransformV2Body,
        ResponseTransformV2Body_Remove,
        ResponseTransformV2Body_Transform,
        ResponseTransformV2Body_XWwwFormUrlencoded,
    )
    from .response_transform_v2template_engine import ResponseTransformV2TemplateEngine
    from .retry_conf import RetryConf
    from .role import Role
    from .root_fields_customization import RootFieldsCustomization
    from .ruf_key_on_arr_rel_using_f_key_on_big_query import RufKeyOnArrRelUsingFKeyOnBigQuery
    from .ruf_key_on_arr_rel_using_f_key_on_big_query_foreign_key_constraint_on import (
        RufKeyOnArrRelUsingFKeyOnBigQueryForeignKeyConstraintOn,
    )
    from .ruf_key_on_arr_rel_using_f_key_on_data_connector import RufKeyOnArrRelUsingFKeyOnDataConnector
    from .ruf_key_on_arr_rel_using_f_key_on_data_connector_foreign_key_constraint_on import (
        RufKeyOnArrRelUsingFKeyOnDataConnectorForeignKeyConstraintOn,
    )
    from .ruf_key_on_arr_rel_using_f_key_on_mssql import RufKeyOnArrRelUsingFKeyOnMssql
    from .ruf_key_on_arr_rel_using_f_key_on_mssql_foreign_key_constraint_on import (
        RufKeyOnArrRelUsingFKeyOnMssqlForeignKeyConstraintOn,
    )
    from .ruf_key_on_arr_rel_using_f_key_on_postgres_citus import RufKeyOnArrRelUsingFKeyOnPostgresCitus
    from .ruf_key_on_arr_rel_using_f_key_on_postgres_citus_foreign_key_constraint_on import (
        RufKeyOnArrRelUsingFKeyOnPostgresCitusForeignKeyConstraintOn,
    )
    from .ruf_key_on_arr_rel_using_f_key_on_postgres_cockroach import RufKeyOnArrRelUsingFKeyOnPostgresCockroach
    from .ruf_key_on_arr_rel_using_f_key_on_postgres_cockroach_foreign_key_constraint_on import (
        RufKeyOnArrRelUsingFKeyOnPostgresCockroachForeignKeyConstraintOn,
    )
    from .ruf_key_on_arr_rel_using_f_key_on_postgres_vanilla import RufKeyOnArrRelUsingFKeyOnPostgresVanilla
    from .ruf_key_on_arr_rel_using_f_key_on_postgres_vanilla_foreign_key_constraint_on import (
        RufKeyOnArrRelUsingFKeyOnPostgresVanillaForeignKeyConstraintOn,
    )
    from .ruf_key_on_obj_rel_using_choice_big_query import RufKeyOnObjRelUsingChoiceBigQuery
    from .ruf_key_on_obj_rel_using_choice_big_query_foreign_key_constraint_on import (
        RufKeyOnObjRelUsingChoiceBigQueryForeignKeyConstraintOn,
    )
    from .ruf_key_on_obj_rel_using_choice_data_connector import RufKeyOnObjRelUsingChoiceDataConnector
    from .ruf_key_on_obj_rel_using_choice_data_connector_foreign_key_constraint_on import (
        RufKeyOnObjRelUsingChoiceDataConnectorForeignKeyConstraintOn,
    )
    from .ruf_key_on_obj_rel_using_choice_data_connector_foreign_key_constraint_on_two_item import (
        RufKeyOnObjRelUsingChoiceDataConnectorForeignKeyConstraintOnTwoItem,
    )
    from .ruf_key_on_obj_rel_using_choice_mssql import RufKeyOnObjRelUsingChoiceMssql
    from .ruf_key_on_obj_rel_using_choice_mssql_foreign_key_constraint_on import (
        RufKeyOnObjRelUsingChoiceMssqlForeignKeyConstraintOn,
    )
    from .ruf_key_on_obj_rel_using_choice_postgres_citus import RufKeyOnObjRelUsingChoicePostgresCitus
    from .ruf_key_on_obj_rel_using_choice_postgres_citus_foreign_key_constraint_on import (
        RufKeyOnObjRelUsingChoicePostgresCitusForeignKeyConstraintOn,
    )
    from .ruf_key_on_obj_rel_using_choice_postgres_cockroach import RufKeyOnObjRelUsingChoicePostgresCockroach
    from .ruf_key_on_obj_rel_using_choice_postgres_cockroach_foreign_key_constraint_on import (
        RufKeyOnObjRelUsingChoicePostgresCockroachForeignKeyConstraintOn,
    )
    from .ruf_key_on_obj_rel_using_choice_postgres_vanilla import RufKeyOnObjRelUsingChoicePostgresVanilla
    from .ruf_key_on_obj_rel_using_choice_postgres_vanilla_foreign_key_constraint_on import (
        RufKeyOnObjRelUsingChoicePostgresVanillaForeignKeyConstraintOn,
    )
    from .scalar_type import ScalarType
    from .scalar_type_definition import ScalarTypeDefinition
    from .source_customization import SourceCustomization
    from .source_metadata import SourceMetadata
    from .source_type_customization import SourceTypeCustomization
    from .ssl_mode import SslMode
    from .st_retry_conf import StRetryConf
    from .stored_procedure_config import StoredProcedureConfig
    from .stored_procedure_config_exposed_as import StoredProcedureConfigExposedAs
    from .table_custom_root_fields import TableCustomRootFields
    from .table_custom_root_fields_delete import TableCustomRootFieldsDelete
    from .table_custom_root_fields_delete_by_pk import TableCustomRootFieldsDeleteByPk
    from .table_custom_root_fields_insert import TableCustomRootFieldsInsert
    from .table_custom_root_fields_insert_one import TableCustomRootFieldsInsertOne
    from .table_custom_root_fields_select import TableCustomRootFieldsSelect
    from .table_custom_root_fields_select_aggregate import TableCustomRootFieldsSelectAggregate
    from .table_custom_root_fields_select_by_pk import TableCustomRootFieldsSelectByPk
    from .table_custom_root_fields_select_stream import TableCustomRootFieldsSelectStream
    from .table_custom_root_fields_update import TableCustomRootFieldsUpdate
    from .table_custom_root_fields_update_by_pk import TableCustomRootFieldsUpdateByPk
    from .table_custom_root_fields_update_many import TableCustomRootFieldsUpdateMany
    from .table_function_response import TableFunctionResponse
    from .table_function_response_type import TableFunctionResponseType
    from .template_variable_dynamic_from_file import TemplateVariableDynamicFromFile
    from .template_variable_dynamic_from_file_type import TemplateVariableDynamicFromFileType
    from .template_variable_source import TemplateVariableSource
    from .tls_allow import TlsAllow
    from .tls_allow_permissions_item import TlsAllowPermissionsItem
    from .to_schema_relationship_def import ToSchemaRelationshipDef
    from .to_schema_relationship_def_legacy_format import ToSchemaRelationshipDefLegacyFormat
    from .to_source_relationship_def import ToSourceRelationshipDef
    from .to_source_relationship_def_relationship_type import ToSourceRelationshipDefRelationshipType
    from .tx_isolation import TxIsolation
    from .type_relationship_definition import TypeRelationshipDefinition
    from .type_relationship_definition_type import TypeRelationshipDefinitionType
    from .url_conf_from_params import UrlConfFromParams
    from .url_conf_from_params_connection_parameters import UrlConfFromParamsConnectionParameters
    from .url_conf_from_params_connection_parameters_left import UrlConfFromParamsConnectionParametersLeft
    from .url_conf_from_params_connection_parameters_right import UrlConfFromParamsConnectionParametersRight
    from .validate_input_http_definition import ValidateInputHttpDefinition
    from .validate_input_http_definition_headers_item import ValidateInputHttpDefinitionHeadersItem
    from .validate_input_input_webhook import ValidateInputInputWebhook
    from .validate_input_input_webhook_type import ValidateInputInputWebhookType
_dynamic_imports: typing.Dict[str, str] = {
    "ActionDefinitionMutationGraphQlTypeInputWebhook": ".action_definition_mutation_graph_ql_type_input_webhook",
    "ActionDefinitionMutationGraphQlTypeInputWebhookHeadersItem": ".action_definition_mutation_graph_ql_type_input_webhook_headers_item",
    "ActionDefinitionMutationGraphQlTypeInputWebhookKind": ".action_definition_mutation_graph_ql_type_input_webhook_kind",
    "ActionDefinitionMutationGraphQlTypeInputWebhookRequestTransform": ".action_definition_mutation_graph_ql_type_input_webhook_request_transform",
    "ActionDefinitionMutationGraphQlTypeInputWebhookResponseTransform": ".action_definition_mutation_graph_ql_type_input_webhook_response_transform",
    "ActionDefinitionQueryGraphQlTypeInputWebhook": ".action_definition_query_graph_ql_type_input_webhook",
    "ActionDefinitionQueryGraphQlTypeInputWebhookHeadersItem": ".action_definition_query_graph_ql_type_input_webhook_headers_item",
    "ActionDefinitionQueryGraphQlTypeInputWebhookRequestTransform": ".action_definition_query_graph_ql_type_input_webhook_request_transform",
    "ActionDefinitionQueryGraphQlTypeInputWebhookResponseTransform": ".action_definition_query_graph_ql_type_input_webhook_response_transform",
    "ActionMetadata": ".action_metadata",
    "ActionMetadataDefinition": ".action_metadata_definition",
    "ActionMetadataDefinition_Mutation": ".action_metadata_definition",
    "ActionMetadataDefinition_Query": ".action_metadata_definition",
    "ActionPermissionMetadata": ".action_permission_metadata",
    "AddReplaceOrRemoveFields": ".add_replace_or_remove_fields",
    "AllowlistEntry": ".allowlist_entry",
    "AllowlistEntryScope": ".allowlist_entry_scope",
    "AllowlistScopeGlobal": ".allowlist_scope_global",
    "AllowlistScopeRoles": ".allowlist_scope_roles",
    "ApiLimit": ".api_limit",
    "ApolloFederationConfig": ".apollo_federation_config",
    "ApolloFederationConfigEnable": ".apollo_federation_config_enable",
    "ArgumentDefinitionGraphQlType": ".argument_definition_graph_ql_type",
    "AutoTriggerLogCleanupConfig": ".auto_trigger_log_cleanup_config",
    "BackendMapBackendConfigWrapper": ".backend_map_backend_config_wrapper",
    "BigQueryComputedFieldDefinition": ".big_query_computed_field_definition",
    "BigQueryConnSourceConfig": ".big_query_conn_source_config",
    "BigQueryConnSourceConfigDatasets": ".big_query_conn_source_config_datasets",
    "BigQueryConnSourceConfigGlobalSelectLimit": ".big_query_conn_source_config_global_select_limit",
    "BigQueryConnSourceConfigProjectId": ".big_query_conn_source_config_project_id",
    "BigQueryConnSourceConfigRetryBaseDelay": ".big_query_conn_source_config_retry_base_delay",
    "BigQueryConnSourceConfigRetryLimit": ".big_query_conn_source_config_retry_limit",
    "BigQueryFunctionName": ".big_query_function_name",
    "BigQueryServiceAccount": ".big_query_service_account",
    "BigQueryTableName": ".big_query_table_name",
    "BigqueryArrRelUsingFKeyOnMultipleColumns": ".bigquery_arr_rel_using_f_key_on_multiple_columns",
    "BigqueryArrRelUsingFKeyOnSingleColumn": ".bigquery_arr_rel_using_f_key_on_single_column",
    "BigqueryBoolExp": ".bigquery_bool_exp",
    "BigqueryComputedFieldMetadata": ".bigquery_computed_field_metadata",
    "BigqueryDelPerm": ".bigquery_del_perm",
    "BigqueryDeletePermDef": ".bigquery_delete_perm_def",
    "BigqueryFunctionMetadata": ".bigquery_function_metadata",
    "BigqueryInsPerm": ".bigquery_ins_perm",
    "BigqueryInsPermColumns": ".bigquery_ins_perm_columns",
    "BigqueryInsPermColumnsZero": ".bigquery_ins_perm_columns_zero",
    "BigqueryInsertPermDef": ".bigquery_insert_perm_def",
    "BigqueryLogicalModelField": ".bigquery_logical_model_field",
    "BigqueryLogicalModelMetadata": ".bigquery_logical_model_metadata",
    "BigqueryNativeQueryMetadata": ".bigquery_native_query_metadata",
    "BigqueryNullableScalarType": ".bigquery_nullable_scalar_type",
    "BigqueryObjRelRemoteTableMultipleColumns": ".bigquery_obj_rel_remote_table_multiple_columns",
    "BigqueryObjRelRemoteTableSingleColumn": ".bigquery_obj_rel_remote_table_single_column",
    "BigqueryRelManualNativeQueryConfig": ".bigquery_rel_manual_native_query_config",
    "BigqueryRelManualNativeQueryConfigInsertionOrder": ".bigquery_rel_manual_native_query_config_insertion_order",
    "BigqueryRelManualTableConfig": ".bigquery_rel_manual_table_config",
    "BigqueryRelManualTableConfigInsertionOrder": ".bigquery_rel_manual_table_config_insertion_order",
    "BigqueryRuManual": ".bigquery_ru_manual",
    "BigquerySelPerm": ".bigquery_sel_perm",
    "BigquerySelPermColumns": ".bigquery_sel_perm_columns",
    "BigquerySelPermColumnsZero": ".bigquery_sel_perm_columns_zero",
    "BigquerySelPermQueryRootFieldsItem": ".bigquery_sel_perm_query_root_fields_item",
    "BigquerySelPermSubscriptionRootFieldsItem": ".bigquery_sel_perm_subscription_root_fields_item",
    "BigquerySelectPermDef": ".bigquery_select_perm_def",
    "BigquerySourceMetadata": ".bigquery_source_metadata",
    "BigquerySourceMetadataKind": ".bigquery_source_metadata_kind",
    "BigqueryStoredProcedureMetadata": ".bigquery_stored_procedure_metadata",
    "BigqueryTableConfig": ".bigquery_table_config",
    "BigqueryTableMetadata": ".bigquery_table_metadata",
    "BigqueryUpdPerm": ".bigquery_upd_perm",
    "BigqueryUpdPermColumns": ".bigquery_upd_perm_columns",
    "BigqueryUpdPermColumnsZero": ".bigquery_upd_perm_columns_zero",
    "BigqueryUpdatePermDef": ".bigquery_update_perm_def",
    "BodyTransformFnModifyAsFormUrlEncoded": ".body_transform_fn_modify_as_form_url_encoded",
    "BodyTransformFnModifyAsJson": ".body_transform_fn_modify_as_json",
    "BodyTransformFnRemove": ".body_transform_fn_remove",
    "CertVar": ".cert_var",
    "CitusArrRelUsingFKeyOnMultipleColumns": ".citus_arr_rel_using_f_key_on_multiple_columns",
    "CitusArrRelUsingFKeyOnSingleColumn": ".citus_arr_rel_using_f_key_on_single_column",
    "CitusBoolExp": ".citus_bool_exp",
    "CitusComputedFieldMetadata": ".citus_computed_field_metadata",
    "CitusDelPerm": ".citus_del_perm",
    "CitusDeletePermDef": ".citus_delete_perm_def",
    "CitusEventTriggerConfEventTriggerConf": ".citus_event_trigger_conf_event_trigger_conf",
    "CitusEventTriggerConfEventTriggerConfHeadersItem": ".citus_event_trigger_conf_event_trigger_conf_headers_item",
    "CitusEventTriggerConfEventTriggerConfRequestTransform": ".citus_event_trigger_conf_event_trigger_conf_request_transform",
    "CitusEventTriggerConfEventTriggerConfResponseTransform": ".citus_event_trigger_conf_event_trigger_conf_response_transform",
    "CitusFunctionMetadata": ".citus_function_metadata",
    "CitusHealthCheckConfig": ".citus_health_check_config",
    "CitusInsPerm": ".citus_ins_perm",
    "CitusInsPermColumns": ".citus_ins_perm_columns",
    "CitusInsPermColumnsZero": ".citus_ins_perm_columns_zero",
    "CitusInsertPermDef": ".citus_insert_perm_def",
    "CitusLogicalModelField": ".citus_logical_model_field",
    "CitusLogicalModelMetadata": ".citus_logical_model_metadata",
    "CitusNativeQueryMetadata": ".citus_native_query_metadata",
    "CitusNullableScalarType": ".citus_nullable_scalar_type",
    "CitusObjRelRemoteTableMultipleColumns": ".citus_obj_rel_remote_table_multiple_columns",
    "CitusObjRelRemoteTableSingleColumn": ".citus_obj_rel_remote_table_single_column",
    "CitusRelManualNativeQueryConfig": ".citus_rel_manual_native_query_config",
    "CitusRelManualNativeQueryConfigInsertionOrder": ".citus_rel_manual_native_query_config_insertion_order",
    "CitusRelManualTableConfig": ".citus_rel_manual_table_config",
    "CitusRelManualTableConfigInsertionOrder": ".citus_rel_manual_table_config_insertion_order",
    "CitusRuManual": ".citus_ru_manual",
    "CitusSelPerm": ".citus_sel_perm",
    "CitusSelPermColumns": ".citus_sel_perm_columns",
    "CitusSelPermColumnsZero": ".citus_sel_perm_columns_zero",
    "CitusSelPermQueryRootFieldsItem": ".citus_sel_perm_query_root_fields_item",
    "CitusSelPermSubscriptionRootFieldsItem": ".citus_sel_perm_subscription_root_fields_item",
    "CitusSelectPermDef": ".citus_select_perm_def",
    "CitusSourceMetadata": ".citus_source_metadata",
    "CitusSourceMetadataKind": ".citus_source_metadata_kind",
    "CitusStoredProcedureMetadata": ".citus_stored_procedure_metadata",
    "CitusSubscribeOpSpec": ".citus_subscribe_op_spec",
    "CitusSubscribeOpSpecColumns": ".citus_subscribe_op_spec_columns",
    "CitusSubscribeOpSpecColumnsZero": ".citus_subscribe_op_spec_columns_zero",
    "CitusSubscribeOpSpecPayload": ".citus_subscribe_op_spec_payload",
    "CitusSubscribeOpSpecPayloadZero": ".citus_subscribe_op_spec_payload_zero",
    "CitusTableConfig": ".citus_table_config",
    "CitusTableMetadata": ".citus_table_metadata",
    "CitusTriggerOpsDef": ".citus_trigger_ops_def",
    "CitusUpdPerm": ".citus_upd_perm",
    "CitusUpdPermColumns": ".citus_upd_perm_columns",
    "CitusUpdPermColumnsZero": ".citus_upd_perm_columns_zero",
    "CitusUpdatePermDef": ".citus_update_perm_def",
    "CockroachArrRelUsingFKeyOnMultipleColumns": ".cockroach_arr_rel_using_f_key_on_multiple_columns",
    "CockroachArrRelUsingFKeyOnSingleColumn": ".cockroach_arr_rel_using_f_key_on_single_column",
    "CockroachBoolExp": ".cockroach_bool_exp",
    "CockroachComputedFieldMetadata": ".cockroach_computed_field_metadata",
    "CockroachDelPerm": ".cockroach_del_perm",
    "CockroachDeletePermDef": ".cockroach_delete_perm_def",
    "CockroachEventTriggerConfEventTriggerConf": ".cockroach_event_trigger_conf_event_trigger_conf",
    "CockroachEventTriggerConfEventTriggerConfHeadersItem": ".cockroach_event_trigger_conf_event_trigger_conf_headers_item",
    "CockroachEventTriggerConfEventTriggerConfRequestTransform": ".cockroach_event_trigger_conf_event_trigger_conf_request_transform",
    "CockroachEventTriggerConfEventTriggerConfResponseTransform": ".cockroach_event_trigger_conf_event_trigger_conf_response_transform",
    "CockroachFunctionMetadata": ".cockroach_function_metadata",
    "CockroachHealthCheckConfig": ".cockroach_health_check_config",
    "CockroachInsPerm": ".cockroach_ins_perm",
    "CockroachInsPermColumns": ".cockroach_ins_perm_columns",
    "CockroachInsPermColumnsZero": ".cockroach_ins_perm_columns_zero",
    "CockroachInsertPermDef": ".cockroach_insert_perm_def",
    "CockroachLogicalModelField": ".cockroach_logical_model_field",
    "CockroachLogicalModelMetadata": ".cockroach_logical_model_metadata",
    "CockroachNativeQueryMetadata": ".cockroach_native_query_metadata",
    "CockroachNullableScalarType": ".cockroach_nullable_scalar_type",
    "CockroachObjRelRemoteTableMultipleColumns": ".cockroach_obj_rel_remote_table_multiple_columns",
    "CockroachObjRelRemoteTableSingleColumn": ".cockroach_obj_rel_remote_table_single_column",
    "CockroachRelManualNativeQueryConfig": ".cockroach_rel_manual_native_query_config",
    "CockroachRelManualNativeQueryConfigInsertionOrder": ".cockroach_rel_manual_native_query_config_insertion_order",
    "CockroachRelManualTableConfig": ".cockroach_rel_manual_table_config",
    "CockroachRelManualTableConfigInsertionOrder": ".cockroach_rel_manual_table_config_insertion_order",
    "CockroachRuManual": ".cockroach_ru_manual",
    "CockroachSelPerm": ".cockroach_sel_perm",
    "CockroachSelPermColumns": ".cockroach_sel_perm_columns",
    "CockroachSelPermColumnsZero": ".cockroach_sel_perm_columns_zero",
    "CockroachSelPermQueryRootFieldsItem": ".cockroach_sel_perm_query_root_fields_item",
    "CockroachSelPermSubscriptionRootFieldsItem": ".cockroach_sel_perm_subscription_root_fields_item",
    "CockroachSelectPermDef": ".cockroach_select_perm_def",
    "CockroachSourceMetadata": ".cockroach_source_metadata",
    "CockroachSourceMetadataKind": ".cockroach_source_metadata_kind",
    "CockroachStoredProcedureMetadata": ".cockroach_stored_procedure_metadata",
    "CockroachSubscribeOpSpec": ".cockroach_subscribe_op_spec",
    "CockroachSubscribeOpSpecColumns": ".cockroach_subscribe_op_spec_columns",
    "CockroachSubscribeOpSpecColumnsZero": ".cockroach_subscribe_op_spec_columns_zero",
    "CockroachSubscribeOpSpecPayload": ".cockroach_subscribe_op_spec_payload",
    "CockroachSubscribeOpSpecPayloadZero": ".cockroach_subscribe_op_spec_payload_zero",
    "CockroachTableConfig": ".cockroach_table_config",
    "CockroachTableMetadata": ".cockroach_table_metadata",
    "CockroachTriggerOpsDef": ".cockroach_trigger_ops_def",
    "CockroachUpdPerm": ".cockroach_upd_perm",
    "CockroachUpdPermColumns": ".cockroach_upd_perm_columns",
    "CockroachUpdPermColumnsZero": ".cockroach_upd_perm_columns_zero",
    "CockroachUpdatePermDef": ".cockroach_update_perm_def",
    "CollectionDef": ".collection_def",
    "ColumnConfig": ".column_config",
    "Config": ".config",
    "ConnectionTemplate": ".connection_template",
    "CreateCollection": ".create_collection",
    "CronSchedule": ".cron_schedule",
    "CronTriggerMetadata": ".cron_trigger_metadata",
    "CronTriggerMetadataHeadersItem": ".cron_trigger_metadata_headers_item",
    "CronTriggerMetadataRequestTransform": ".cron_trigger_metadata_request_transform",
    "CronTriggerMetadataResponseTransform": ".cron_trigger_metadata_response_transform",
    "CustomRootField": ".custom_root_field",
    "CustomTypes": ".custom_types",
    "DataConnectorConnSourceConfig": ".data_connector_conn_source_config",
    "DataConnectorConnSourceConfigTimeout": ".data_connector_conn_source_config_timeout",
    "DataConnectorOptions": ".data_connector_options",
    "DataConnectorOptionsUri": ".data_connector_options_uri",
    "DataConnectorSourceTimeoutMicroseconds": ".data_connector_source_timeout_microseconds",
    "DataConnectorSourceTimeoutMilliseconds": ".data_connector_source_timeout_milliseconds",
    "DataConnectorSourceTimeoutSeconds": ".data_connector_source_timeout_seconds",
    "DataconnectorArrRelUsingFKeyOnMultipleColumns": ".dataconnector_arr_rel_using_f_key_on_multiple_columns",
    "DataconnectorArrRelUsingFKeyOnMultipleColumnsColumnsItem": ".dataconnector_arr_rel_using_f_key_on_multiple_columns_columns_item",
    "DataconnectorArrRelUsingFKeyOnSingleColumn": ".dataconnector_arr_rel_using_f_key_on_single_column",
    "DataconnectorArrRelUsingFKeyOnSingleColumnColumn": ".dataconnector_arr_rel_using_f_key_on_single_column_column",
    "DataconnectorBoolExp": ".dataconnector_bool_exp",
    "DataconnectorComputedFieldMetadata": ".dataconnector_computed_field_metadata",
    "DataconnectorDelPerm": ".dataconnector_del_perm",
    "DataconnectorDeletePermDef": ".dataconnector_delete_perm_def",
    "DataconnectorFunctionMetadata": ".dataconnector_function_metadata",
    "DataconnectorInsPerm": ".dataconnector_ins_perm",
    "DataconnectorInsPermColumns": ".dataconnector_ins_perm_columns",
    "DataconnectorInsPermColumnsZero": ".dataconnector_ins_perm_columns_zero",
    "DataconnectorInsertPermDef": ".dataconnector_insert_perm_def",
    "DataconnectorLogicalModelField": ".dataconnector_logical_model_field",
    "DataconnectorLogicalModelMetadata": ".dataconnector_logical_model_metadata",
    "DataconnectorNativeQueryMetadata": ".dataconnector_native_query_metadata",
    "DataconnectorNullableScalarType": ".dataconnector_nullable_scalar_type",
    "DataconnectorObjRelRemoteTableMultipleColumns": ".dataconnector_obj_rel_remote_table_multiple_columns",
    "DataconnectorObjRelRemoteTableMultipleColumnsColumnsItem": ".dataconnector_obj_rel_remote_table_multiple_columns_columns_item",
    "DataconnectorObjRelRemoteTableSingleColumn": ".dataconnector_obj_rel_remote_table_single_column",
    "DataconnectorObjRelRemoteTableSingleColumnColumn": ".dataconnector_obj_rel_remote_table_single_column_column",
    "DataconnectorRelManualNativeQueryConfig": ".dataconnector_rel_manual_native_query_config",
    "DataconnectorRelManualNativeQueryConfigInsertionOrder": ".dataconnector_rel_manual_native_query_config_insertion_order",
    "DataconnectorRelManualTableConfig": ".dataconnector_rel_manual_table_config",
    "DataconnectorRelManualTableConfigInsertionOrder": ".dataconnector_rel_manual_table_config_insertion_order",
    "DataconnectorRuManual": ".dataconnector_ru_manual",
    "DataconnectorSelPerm": ".dataconnector_sel_perm",
    "DataconnectorSelPermColumns": ".dataconnector_sel_perm_columns",
    "DataconnectorSelPermColumnsZero": ".dataconnector_sel_perm_columns_zero",
    "DataconnectorSelPermQueryRootFieldsItem": ".dataconnector_sel_perm_query_root_fields_item",
    "DataconnectorSelPermSubscriptionRootFieldsItem": ".dataconnector_sel_perm_subscription_root_fields_item",
    "DataconnectorSelectPermDef": ".dataconnector_select_perm_def",
    "DataconnectorSourceMetadata": ".dataconnector_source_metadata",
    "DataconnectorStoredProcedureMetadata": ".dataconnector_stored_procedure_metadata",
    "DataconnectorTableConfig": ".dataconnector_table_config",
    "DataconnectorTableMetadata": ".dataconnector_table_metadata",
    "DataconnectorUpdPerm": ".dataconnector_upd_perm",
    "DataconnectorUpdPermColumns": ".dataconnector_upd_perm_columns",
    "DataconnectorUpdPermColumnsZero": ".dataconnector_upd_perm_columns_zero",
    "DataconnectorUpdatePermDef": ".dataconnector_update_perm_def",
    "EndpointDefQueryReference": ".endpoint_def_query_reference",
    "EndpointMetadataQueryReference": ".endpoint_metadata_query_reference",
    "EndpointMetadataQueryReferenceMethodsItem": ".endpoint_metadata_query_reference_methods_item",
    "EnumTypeDefinition": ".enum_type_definition",
    "EnumValueDefinition": ".enum_value_definition",
    "ExtensionsSchema": ".extensions_schema",
    "FieldCall": ".field_call",
    "FromEnv": ".from_env",
    "FunctionConfig": ".function_config",
    "FunctionConfigExposedAs": ".function_config_exposed_as",
    "FunctionCustomRootFields": ".function_custom_root_fields",
    "FunctionPermissionInfo": ".function_permission_info",
    "FunctionReturnType": ".function_return_type",
    "GraphQlName": ".graph_ql_name",
    "GraphQlSchema": ".graph_ql_schema",
    "GraphQlValueName": ".graph_ql_value_name",
    "HeaderConfFromEnv": ".header_conf_from_env",
    "HeaderConfValue": ".header_conf_value",
    "HealthCheckTestSql": ".health_check_test_sql",
    "InferredFunctionResponse": ".inferred_function_response",
    "InferredFunctionResponseType": ".inferred_function_response_type",
    "InputObjectFieldDefinition": ".input_object_field_definition",
    "InputObjectTypeDefinition": ".input_object_type_definition",
    "LimitMaxBatchSize": ".limit_max_batch_size",
    "LimitMaxDepth": ".limit_max_depth",
    "LimitMaxNodes": ".limit_max_nodes",
    "LimitMaxTime": ".limit_max_time",
    "LimitRateLimitConfig": ".limit_rate_limit_config",
    "ListedQuery": ".listed_query",
    "Metadata": ".metadata",
    "MetadataV1": ".metadata_v1",
    "MetadataV2": ".metadata_v2",
    "MetadataV3": ".metadata_v3",
    "MetricsConfig": ".metrics_config",
    "MssqlArrRelUsingFKeyOnMultipleColumns": ".mssql_arr_rel_using_f_key_on_multiple_columns",
    "MssqlArrRelUsingFKeyOnSingleColumn": ".mssql_arr_rel_using_f_key_on_single_column",
    "MssqlBoolExp": ".mssql_bool_exp",
    "MssqlComputedFieldMetadata": ".mssql_computed_field_metadata",
    "MssqlConnConfiguration": ".mssql_conn_configuration",
    "MssqlConnectionInfo": ".mssql_connection_info",
    "MssqlConnectionInfoConnectionString": ".mssql_connection_info_connection_string",
    "MssqlDelPerm": ".mssql_del_perm",
    "MssqlDeletePermDef": ".mssql_delete_perm_def",
    "MssqlEventTriggerConfEventTriggerConf": ".mssql_event_trigger_conf_event_trigger_conf",
    "MssqlEventTriggerConfEventTriggerConfHeadersItem": ".mssql_event_trigger_conf_event_trigger_conf_headers_item",
    "MssqlEventTriggerConfEventTriggerConfRequestTransform": ".mssql_event_trigger_conf_event_trigger_conf_request_transform",
    "MssqlEventTriggerConfEventTriggerConfResponseTransform": ".mssql_event_trigger_conf_event_trigger_conf_response_transform",
    "MssqlFunctionMetadata": ".mssql_function_metadata",
    "MssqlFunctionName": ".mssql_function_name",
    "MssqlHealthCheckConfig": ".mssql_health_check_config",
    "MssqlInsPerm": ".mssql_ins_perm",
    "MssqlInsPermColumns": ".mssql_ins_perm_columns",
    "MssqlInsPermColumnsZero": ".mssql_ins_perm_columns_zero",
    "MssqlInsertPermDef": ".mssql_insert_perm_def",
    "MssqlLogicalModelField": ".mssql_logical_model_field",
    "MssqlLogicalModelMetadata": ".mssql_logical_model_metadata",
    "MssqlNativeQueryMetadata": ".mssql_native_query_metadata",
    "MssqlNullableScalarType": ".mssql_nullable_scalar_type",
    "MssqlObjRelRemoteTableMultipleColumns": ".mssql_obj_rel_remote_table_multiple_columns",
    "MssqlObjRelRemoteTableSingleColumn": ".mssql_obj_rel_remote_table_single_column",
    "MssqlPoolSettings": ".mssql_pool_settings",
    "MssqlRelManualNativeQueryConfig": ".mssql_rel_manual_native_query_config",
    "MssqlRelManualNativeQueryConfigInsertionOrder": ".mssql_rel_manual_native_query_config_insertion_order",
    "MssqlRelManualTableConfig": ".mssql_rel_manual_table_config",
    "MssqlRelManualTableConfigInsertionOrder": ".mssql_rel_manual_table_config_insertion_order",
    "MssqlRuManual": ".mssql_ru_manual",
    "MssqlSelPerm": ".mssql_sel_perm",
    "MssqlSelPermColumns": ".mssql_sel_perm_columns",
    "MssqlSelPermColumnsZero": ".mssql_sel_perm_columns_zero",
    "MssqlSelPermQueryRootFieldsItem": ".mssql_sel_perm_query_root_fields_item",
    "MssqlSelPermSubscriptionRootFieldsItem": ".mssql_sel_perm_subscription_root_fields_item",
    "MssqlSelectPermDef": ".mssql_select_perm_def",
    "MssqlSourceMetadata": ".mssql_source_metadata",
    "MssqlSourceMetadataKind": ".mssql_source_metadata_kind",
    "MssqlStoredProcedureMetadata": ".mssql_stored_procedure_metadata",
    "MssqlSubscribeOpSpec": ".mssql_subscribe_op_spec",
    "MssqlSubscribeOpSpecColumns": ".mssql_subscribe_op_spec_columns",
    "MssqlSubscribeOpSpecColumnsZero": ".mssql_subscribe_op_spec_columns_zero",
    "MssqlSubscribeOpSpecPayload": ".mssql_subscribe_op_spec_payload",
    "MssqlSubscribeOpSpecPayloadZero": ".mssql_subscribe_op_spec_payload_zero",
    "MssqlTableConfig": ".mssql_table_config",
    "MssqlTableMetadata": ".mssql_table_metadata",
    "MssqlTableName": ".mssql_table_name",
    "MssqlTriggerOpsDef": ".mssql_trigger_ops_def",
    "MssqlUpdPerm": ".mssql_upd_perm",
    "MssqlUpdPermColumns": ".mssql_upd_perm_columns",
    "MssqlUpdPermColumnsZero": ".mssql_upd_perm_columns_zero",
    "MssqlUpdatePermDef": ".mssql_update_perm_def",
    "NamingCase": ".naming_case",
    "Network": ".network",
    "ObjectFieldDefinitionGraphQlType": ".object_field_definition_graph_ql_type",
    "ObjectTypeDefinition": ".object_type_definition",
    "OpenTelemetryConfig": ".open_telemetry_config",
    "OpenTelemetryConfigDataTypesItem": ".open_telemetry_config_data_types_item",
    "OtelBatchSpanProcessorConfig": ".otel_batch_span_processor_config",
    "OtelExporterConfig": ".otel_exporter_config",
    "OtelExporterConfigHeadersItem": ".otel_exporter_config_headers_item",
    "OtelExporterConfigProtocol": ".otel_exporter_config_protocol",
    "OtelExporterConfigTracesPropagatorsItem": ".otel_exporter_config_traces_propagators_item",
    "OtelNameValue": ".otel_name_value",
    "PgClientCerts": ".pg_client_certs",
    "PgConnectionParams": ".pg_connection_params",
    "PostgresArrRelUsingFKeyOnMultipleColumns": ".postgres_arr_rel_using_f_key_on_multiple_columns",
    "PostgresArrRelUsingFKeyOnSingleColumn": ".postgres_arr_rel_using_f_key_on_single_column",
    "PostgresBoolExp": ".postgres_bool_exp",
    "PostgresComputedFieldDefinition": ".postgres_computed_field_definition",
    "PostgresComputedFieldMetadata": ".postgres_computed_field_metadata",
    "PostgresConnConfiguration": ".postgres_conn_configuration",
    "PostgresDelPerm": ".postgres_del_perm",
    "PostgresDeletePermDef": ".postgres_delete_perm_def",
    "PostgresEventTriggerConfEventTriggerConf": ".postgres_event_trigger_conf_event_trigger_conf",
    "PostgresEventTriggerConfEventTriggerConfHeadersItem": ".postgres_event_trigger_conf_event_trigger_conf_headers_item",
    "PostgresEventTriggerConfEventTriggerConfRequestTransform": ".postgres_event_trigger_conf_event_trigger_conf_request_transform",
    "PostgresEventTriggerConfEventTriggerConfResponseTransform": ".postgres_event_trigger_conf_event_trigger_conf_response_transform",
    "PostgresFunctionMetadata": ".postgres_function_metadata",
    "PostgresHealthCheckConfig": ".postgres_health_check_config",
    "PostgresInsPerm": ".postgres_ins_perm",
    "PostgresInsPermColumns": ".postgres_ins_perm_columns",
    "PostgresInsPermColumnsZero": ".postgres_ins_perm_columns_zero",
    "PostgresInsertPermDef": ".postgres_insert_perm_def",
    "PostgresLogicalModelField": ".postgres_logical_model_field",
    "PostgresLogicalModelMetadata": ".postgres_logical_model_metadata",
    "PostgresNativeQueryMetadata": ".postgres_native_query_metadata",
    "PostgresNullableScalarType": ".postgres_nullable_scalar_type",
    "PostgresObjRelRemoteTableMultipleColumns": ".postgres_obj_rel_remote_table_multiple_columns",
    "PostgresObjRelRemoteTableSingleColumn": ".postgres_obj_rel_remote_table_single_column",
    "PostgresPoolSettings": ".postgres_pool_settings",
    "PostgresQualifiedFunctionName": ".postgres_qualified_function_name",
    "PostgresQualifiedTableName": ".postgres_qualified_table_name",
    "PostgresRelManualNativeQueryConfig": ".postgres_rel_manual_native_query_config",
    "PostgresRelManualNativeQueryConfigInsertionOrder": ".postgres_rel_manual_native_query_config_insertion_order",
    "PostgresRelManualTableConfig": ".postgres_rel_manual_table_config",
    "PostgresRelManualTableConfigInsertionOrder": ".postgres_rel_manual_table_config_insertion_order",
    "PostgresRuManual": ".postgres_ru_manual",
    "PostgresSelPerm": ".postgres_sel_perm",
    "PostgresSelPermColumns": ".postgres_sel_perm_columns",
    "PostgresSelPermColumnsZero": ".postgres_sel_perm_columns_zero",
    "PostgresSelPermQueryRootFieldsItem": ".postgres_sel_perm_query_root_fields_item",
    "PostgresSelPermSubscriptionRootFieldsItem": ".postgres_sel_perm_subscription_root_fields_item",
    "PostgresSelectPermDef": ".postgres_select_perm_def",
    "PostgresSourceConnInfo": ".postgres_source_conn_info",
    "PostgresSourceConnInfoDatabaseUrl": ".postgres_source_conn_info_database_url",
    "PostgresSourceMetadata": ".postgres_source_metadata",
    "PostgresSourceMetadataKind": ".postgres_source_metadata_kind",
    "PostgresStoredProcedureMetadata": ".postgres_stored_procedure_metadata",
    "PostgresSubscribeOpSpec": ".postgres_subscribe_op_spec",
    "PostgresSubscribeOpSpecColumns": ".postgres_subscribe_op_spec_columns",
    "PostgresSubscribeOpSpecColumnsZero": ".postgres_subscribe_op_spec_columns_zero",
    "PostgresSubscribeOpSpecPayload": ".postgres_subscribe_op_spec_payload",
    "PostgresSubscribeOpSpecPayloadZero": ".postgres_subscribe_op_spec_payload_zero",
    "PostgresTableConfig": ".postgres_table_config",
    "PostgresTableMetadata": ".postgres_table_metadata",
    "PostgresTriggerOpsDef": ".postgres_trigger_ops_def",
    "PostgresUpdPerm": ".postgres_upd_perm",
    "PostgresUpdPermColumns": ".postgres_upd_perm_columns",
    "PostgresUpdPermColumnsZero": ".postgres_upd_perm_columns_zero",
    "PostgresUpdatePermDef": ".postgres_update_perm_def",
    "QueryReference": ".query_reference",
    "QueryTagsConfig": ".query_tags_config",
    "QueryTagsFormat": ".query_tags_format",
    "RateLimitConfig": ".rate_limit_config",
    "RateLimitConfigUniqueParams": ".rate_limit_config_unique_params",
    "RateLimitConfigUniqueParamsZero": ".rate_limit_config_unique_params_zero",
    "RelDefRelManualConfigBigQuery": ".rel_def_rel_manual_config_big_query",
    "RelDefRelManualConfigDataConnector": ".rel_def_rel_manual_config_data_connector",
    "RelDefRelManualConfigMssql": ".rel_def_rel_manual_config_mssql",
    "RelDefRelManualConfigPostgresCitus": ".rel_def_rel_manual_config_postgres_citus",
    "RelDefRelManualConfigPostgresCockroach": ".rel_def_rel_manual_config_postgres_cockroach",
    "RelDefRelManualConfigPostgresVanilla": ".rel_def_rel_manual_config_postgres_vanilla",
    "RelDefRelUsingBigQueryArrRelUsingFKeyOnBigQuery": ".rel_def_rel_using_big_query_arr_rel_using_f_key_on_big_query",
    "RelDefRelUsingBigQueryArrRelUsingFKeyOnBigQueryUsing": ".rel_def_rel_using_big_query_arr_rel_using_f_key_on_big_query_using",
    "RelDefRelUsingBigQueryObjRelUsingChoiceBigQuery": ".rel_def_rel_using_big_query_obj_rel_using_choice_big_query",
    "RelDefRelUsingBigQueryObjRelUsingChoiceBigQueryUsing": ".rel_def_rel_using_big_query_obj_rel_using_choice_big_query_using",
    "RelDefRelUsingDataConnectorArrRelUsingFKeyOnDataConnector": ".rel_def_rel_using_data_connector_arr_rel_using_f_key_on_data_connector",
    "RelDefRelUsingDataConnectorArrRelUsingFKeyOnDataConnectorUsing": ".rel_def_rel_using_data_connector_arr_rel_using_f_key_on_data_connector_using",
    "RelDefRelUsingDataConnectorObjRelUsingChoiceDataConnector": ".rel_def_rel_using_data_connector_obj_rel_using_choice_data_connector",
    "RelDefRelUsingDataConnectorObjRelUsingChoiceDataConnectorUsing": ".rel_def_rel_using_data_connector_obj_rel_using_choice_data_connector_using",
    "RelDefRelUsingMssqlArrRelUsingFKeyOnMssql": ".rel_def_rel_using_mssql_arr_rel_using_f_key_on_mssql",
    "RelDefRelUsingMssqlArrRelUsingFKeyOnMssqlUsing": ".rel_def_rel_using_mssql_arr_rel_using_f_key_on_mssql_using",
    "RelDefRelUsingMssqlObjRelUsingChoiceMssql": ".rel_def_rel_using_mssql_obj_rel_using_choice_mssql",
    "RelDefRelUsingMssqlObjRelUsingChoiceMssqlUsing": ".rel_def_rel_using_mssql_obj_rel_using_choice_mssql_using",
    "RelDefRelUsingPostgresCitusArrRelUsingFKeyOnPostgresCitus": ".rel_def_rel_using_postgres_citus_arr_rel_using_f_key_on_postgres_citus",
    "RelDefRelUsingPostgresCitusArrRelUsingFKeyOnPostgresCitusUsing": ".rel_def_rel_using_postgres_citus_arr_rel_using_f_key_on_postgres_citus_using",
    "RelDefRelUsingPostgresCitusObjRelUsingChoicePostgresCitus": ".rel_def_rel_using_postgres_citus_obj_rel_using_choice_postgres_citus",
    "RelDefRelUsingPostgresCitusObjRelUsingChoicePostgresCitusUsing": ".rel_def_rel_using_postgres_citus_obj_rel_using_choice_postgres_citus_using",
    "RelDefRelUsingPostgresCockroachArrRelUsingFKeyOnPostgresCockroach": ".rel_def_rel_using_postgres_cockroach_arr_rel_using_f_key_on_postgres_cockroach",
    "RelDefRelUsingPostgresCockroachArrRelUsingFKeyOnPostgresCockroachUsing": ".rel_def_rel_using_postgres_cockroach_arr_rel_using_f_key_on_postgres_cockroach_using",
    "RelDefRelUsingPostgresCockroachObjRelUsingChoicePostgresCockroach": ".rel_def_rel_using_postgres_cockroach_obj_rel_using_choice_postgres_cockroach",
    "RelDefRelUsingPostgresCockroachObjRelUsingChoicePostgresCockroachUsing": ".rel_def_rel_using_postgres_cockroach_obj_rel_using_choice_postgres_cockroach_using",
    "RelDefRelUsingPostgresVanillaArrRelUsingFKeyOnPostgresVanilla": ".rel_def_rel_using_postgres_vanilla_arr_rel_using_f_key_on_postgres_vanilla",
    "RelDefRelUsingPostgresVanillaArrRelUsingFKeyOnPostgresVanillaUsing": ".rel_def_rel_using_postgres_vanilla_arr_rel_using_f_key_on_postgres_vanilla_using",
    "RelDefRelUsingPostgresVanillaObjRelUsingChoicePostgresVanilla": ".rel_def_rel_using_postgres_vanilla_obj_rel_using_choice_postgres_vanilla",
    "RelDefRelUsingPostgresVanillaObjRelUsingChoicePostgresVanillaUsing": ".rel_def_rel_using_postgres_vanilla_obj_rel_using_choice_postgres_vanilla_using",
    "RelationshipToSchema": ".relationship_to_schema",
    "RelationshipToSource": ".relationship_to_source",
    "RemoteArguments": ".remote_arguments",
    "RemoteFieldCustomization": ".remote_field_customization",
    "RemoteFields": ".remote_fields",
    "RemoteRelationshipRemoteRelationshipDefinition": ".remote_relationship_remote_relationship_definition",
    "RemoteRelationshipRemoteRelationshipDefinitionDefinition": ".remote_relationship_remote_relationship_definition_definition",
    "RemoteSchemaCustomization": ".remote_schema_customization",
    "RemoteSchemaDef": ".remote_schema_def",
    "RemoteSchemaDefHeadersItem": ".remote_schema_def_headers_item",
    "RemoteSchemaDefIntrospectionHeadersItem": ".remote_schema_def_introspection_headers_item",
    "RemoteSchemaMetadataRemoteRelationshipDefinition": ".remote_schema_metadata_remote_relationship_definition",
    "RemoteSchemaPermissionDefinition": ".remote_schema_permission_definition",
    "RemoteSchemaPermissionMetadata": ".remote_schema_permission_metadata",
    "RemoteTypeCustomization": ".remote_type_customization",
    "RequestTransformV1": ".request_transform_v1",
    "RequestTransformV1QueryParams": ".request_transform_v1query_params",
    "RequestTransformV1TemplateEngine": ".request_transform_v1template_engine",
    "RequestTransformV2": ".request_transform_v2",
    "RequestTransformV2Body": ".request_transform_v2body",
    "RequestTransformV2Body_Remove": ".request_transform_v2body",
    "RequestTransformV2Body_Transform": ".request_transform_v2body",
    "RequestTransformV2Body_XWwwFormUrlencoded": ".request_transform_v2body",
    "RequestTransformV2QueryParams": ".request_transform_v2query_params",
    "RequestTransformV2TemplateEngine": ".request_transform_v2template_engine",
    "ResponseTransformV1": ".response_transform_v1",
    "ResponseTransformV1TemplateEngine": ".response_transform_v1template_engine",
    "ResponseTransformV2": ".response_transform_v2",
    "ResponseTransformV2Body": ".response_transform_v2body",
    "ResponseTransformV2Body_Remove": ".response_transform_v2body",
    "ResponseTransformV2Body_Transform": ".response_transform_v2body",
    "ResponseTransformV2Body_XWwwFormUrlencoded": ".response_transform_v2body",
    "ResponseTransformV2TemplateEngine": ".response_transform_v2template_engine",
    "RetryConf": ".retry_conf",
    "Role": ".role",
    "RootFieldsCustomization": ".root_fields_customization",
    "RufKeyOnArrRelUsingFKeyOnBigQuery": ".ruf_key_on_arr_rel_using_f_key_on_big_query",
    "RufKeyOnArrRelUsingFKeyOnBigQueryForeignKeyConstraintOn": ".ruf_key_on_arr_rel_using_f_key_on_big_query_foreign_key_constraint_on",
    "RufKeyOnArrRelUsingFKeyOnDataConnector": ".ruf_key_on_arr_rel_using_f_key_on_data_connector",
    "RufKeyOnArrRelUsingFKeyOnDataConnectorForeignKeyConstraintOn": ".ruf_key_on_arr_rel_using_f_key_on_data_connector_foreign_key_constraint_on",
    "RufKeyOnArrRelUsingFKeyOnMssql": ".ruf_key_on_arr_rel_using_f_key_on_mssql",
    "RufKeyOnArrRelUsingFKeyOnMssqlForeignKeyConstraintOn": ".ruf_key_on_arr_rel_using_f_key_on_mssql_foreign_key_constraint_on",
    "RufKeyOnArrRelUsingFKeyOnPostgresCitus": ".ruf_key_on_arr_rel_using_f_key_on_postgres_citus",
    "RufKeyOnArrRelUsingFKeyOnPostgresCitusForeignKeyConstraintOn": ".ruf_key_on_arr_rel_using_f_key_on_postgres_citus_foreign_key_constraint_on",
    "RufKeyOnArrRelUsingFKeyOnPostgresCockroach": ".ruf_key_on_arr_rel_using_f_key_on_postgres_cockroach",
    "RufKeyOnArrRelUsingFKeyOnPostgresCockroachForeignKeyConstraintOn": ".ruf_key_on_arr_rel_using_f_key_on_postgres_cockroach_foreign_key_constraint_on",
    "RufKeyOnArrRelUsingFKeyOnPostgresVanilla": ".ruf_key_on_arr_rel_using_f_key_on_postgres_vanilla",
    "RufKeyOnArrRelUsingFKeyOnPostgresVanillaForeignKeyConstraintOn": ".ruf_key_on_arr_rel_using_f_key_on_postgres_vanilla_foreign_key_constraint_on",
    "RufKeyOnObjRelUsingChoiceBigQuery": ".ruf_key_on_obj_rel_using_choice_big_query",
    "RufKeyOnObjRelUsingChoiceBigQueryForeignKeyConstraintOn": ".ruf_key_on_obj_rel_using_choice_big_query_foreign_key_constraint_on",
    "RufKeyOnObjRelUsingChoiceDataConnector": ".ruf_key_on_obj_rel_using_choice_data_connector",
    "RufKeyOnObjRelUsingChoiceDataConnectorForeignKeyConstraintOn": ".ruf_key_on_obj_rel_using_choice_data_connector_foreign_key_constraint_on",
    "RufKeyOnObjRelUsingChoiceDataConnectorForeignKeyConstraintOnTwoItem": ".ruf_key_on_obj_rel_using_choice_data_connector_foreign_key_constraint_on_two_item",
    "RufKeyOnObjRelUsingChoiceMssql": ".ruf_key_on_obj_rel_using_choice_mssql",
    "RufKeyOnObjRelUsingChoiceMssqlForeignKeyConstraintOn": ".ruf_key_on_obj_rel_using_choice_mssql_foreign_key_constraint_on",
    "RufKeyOnObjRelUsingChoicePostgresCitus": ".ruf_key_on_obj_rel_using_choice_postgres_citus",
    "RufKeyOnObjRelUsingChoicePostgresCitusForeignKeyConstraintOn": ".ruf_key_on_obj_rel_using_choice_postgres_citus_foreign_key_constraint_on",
    "RufKeyOnObjRelUsingChoicePostgresCockroach": ".ruf_key_on_obj_rel_using_choice_postgres_cockroach",
    "RufKeyOnObjRelUsingChoicePostgresCockroachForeignKeyConstraintOn": ".ruf_key_on_obj_rel_using_choice_postgres_cockroach_foreign_key_constraint_on",
    "RufKeyOnObjRelUsingChoicePostgresVanilla": ".ruf_key_on_obj_rel_using_choice_postgres_vanilla",
    "RufKeyOnObjRelUsingChoicePostgresVanillaForeignKeyConstraintOn": ".ruf_key_on_obj_rel_using_choice_postgres_vanilla_foreign_key_constraint_on",
    "ScalarType": ".scalar_type",
    "ScalarTypeDefinition": ".scalar_type_definition",
    "SourceCustomization": ".source_customization",
    "SourceMetadata": ".source_metadata",
    "SourceTypeCustomization": ".source_type_customization",
    "SslMode": ".ssl_mode",
    "StRetryConf": ".st_retry_conf",
    "StoredProcedureConfig": ".stored_procedure_config",
    "StoredProcedureConfigExposedAs": ".stored_procedure_config_exposed_as",
    "TableCustomRootFields": ".table_custom_root_fields",
    "TableCustomRootFieldsDelete": ".table_custom_root_fields_delete",
    "TableCustomRootFieldsDeleteByPk": ".table_custom_root_fields_delete_by_pk",
    "TableCustomRootFieldsInsert": ".table_custom_root_fields_insert",
    "TableCustomRootFieldsInsertOne": ".table_custom_root_fields_insert_one",
    "TableCustomRootFieldsSelect": ".table_custom_root_fields_select",
    "TableCustomRootFieldsSelectAggregate": ".table_custom_root_fields_select_aggregate",
    "TableCustomRootFieldsSelectByPk": ".table_custom_root_fields_select_by_pk",
    "TableCustomRootFieldsSelectStream": ".table_custom_root_fields_select_stream",
    "TableCustomRootFieldsUpdate": ".table_custom_root_fields_update",
    "TableCustomRootFieldsUpdateByPk": ".table_custom_root_fields_update_by_pk",
    "TableCustomRootFieldsUpdateMany": ".table_custom_root_fields_update_many",
    "TableFunctionResponse": ".table_function_response",
    "TableFunctionResponseType": ".table_function_response_type",
    "TemplateVariableDynamicFromFile": ".template_variable_dynamic_from_file",
    "TemplateVariableDynamicFromFileType": ".template_variable_dynamic_from_file_type",
    "TemplateVariableSource": ".template_variable_source",
    "TlsAllow": ".tls_allow",
    "TlsAllowPermissionsItem": ".tls_allow_permissions_item",
    "ToSchemaRelationshipDef": ".to_schema_relationship_def",
    "ToSchemaRelationshipDefLegacyFormat": ".to_schema_relationship_def_legacy_format",
    "ToSourceRelationshipDef": ".to_source_relationship_def",
    "ToSourceRelationshipDefRelationshipType": ".to_source_relationship_def_relationship_type",
    "TxIsolation": ".tx_isolation",
    "TypeRelationshipDefinition": ".type_relationship_definition",
    "TypeRelationshipDefinitionType": ".type_relationship_definition_type",
    "UrlConfFromParams": ".url_conf_from_params",
    "UrlConfFromParamsConnectionParameters": ".url_conf_from_params_connection_parameters",
    "UrlConfFromParamsConnectionParametersLeft": ".url_conf_from_params_connection_parameters_left",
    "UrlConfFromParamsConnectionParametersRight": ".url_conf_from_params_connection_parameters_right",
    "ValidateInputHttpDefinition": ".validate_input_http_definition",
    "ValidateInputHttpDefinitionHeadersItem": ".validate_input_http_definition_headers_item",
    "ValidateInputInputWebhook": ".validate_input_input_webhook",
    "ValidateInputInputWebhookType": ".validate_input_input_webhook_type",
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
    "ActionDefinitionMutationGraphQlTypeInputWebhook",
    "ActionDefinitionMutationGraphQlTypeInputWebhookHeadersItem",
    "ActionDefinitionMutationGraphQlTypeInputWebhookKind",
    "ActionDefinitionMutationGraphQlTypeInputWebhookRequestTransform",
    "ActionDefinitionMutationGraphQlTypeInputWebhookResponseTransform",
    "ActionDefinitionQueryGraphQlTypeInputWebhook",
    "ActionDefinitionQueryGraphQlTypeInputWebhookHeadersItem",
    "ActionDefinitionQueryGraphQlTypeInputWebhookRequestTransform",
    "ActionDefinitionQueryGraphQlTypeInputWebhookResponseTransform",
    "ActionMetadata",
    "ActionMetadataDefinition",
    "ActionMetadataDefinition_Mutation",
    "ActionMetadataDefinition_Query",
    "ActionPermissionMetadata",
    "AddReplaceOrRemoveFields",
    "AllowlistEntry",
    "AllowlistEntryScope",
    "AllowlistScopeGlobal",
    "AllowlistScopeRoles",
    "ApiLimit",
    "ApolloFederationConfig",
    "ApolloFederationConfigEnable",
    "ArgumentDefinitionGraphQlType",
    "AutoTriggerLogCleanupConfig",
    "BackendMapBackendConfigWrapper",
    "BigQueryComputedFieldDefinition",
    "BigQueryConnSourceConfig",
    "BigQueryConnSourceConfigDatasets",
    "BigQueryConnSourceConfigGlobalSelectLimit",
    "BigQueryConnSourceConfigProjectId",
    "BigQueryConnSourceConfigRetryBaseDelay",
    "BigQueryConnSourceConfigRetryLimit",
    "BigQueryFunctionName",
    "BigQueryServiceAccount",
    "BigQueryTableName",
    "BigqueryArrRelUsingFKeyOnMultipleColumns",
    "BigqueryArrRelUsingFKeyOnSingleColumn",
    "BigqueryBoolExp",
    "BigqueryComputedFieldMetadata",
    "BigqueryDelPerm",
    "BigqueryDeletePermDef",
    "BigqueryFunctionMetadata",
    "BigqueryInsPerm",
    "BigqueryInsPermColumns",
    "BigqueryInsPermColumnsZero",
    "BigqueryInsertPermDef",
    "BigqueryLogicalModelField",
    "BigqueryLogicalModelMetadata",
    "BigqueryNativeQueryMetadata",
    "BigqueryNullableScalarType",
    "BigqueryObjRelRemoteTableMultipleColumns",
    "BigqueryObjRelRemoteTableSingleColumn",
    "BigqueryRelManualNativeQueryConfig",
    "BigqueryRelManualNativeQueryConfigInsertionOrder",
    "BigqueryRelManualTableConfig",
    "BigqueryRelManualTableConfigInsertionOrder",
    "BigqueryRuManual",
    "BigquerySelPerm",
    "BigquerySelPermColumns",
    "BigquerySelPermColumnsZero",
    "BigquerySelPermQueryRootFieldsItem",
    "BigquerySelPermSubscriptionRootFieldsItem",
    "BigquerySelectPermDef",
    "BigquerySourceMetadata",
    "BigquerySourceMetadataKind",
    "BigqueryStoredProcedureMetadata",
    "BigqueryTableConfig",
    "BigqueryTableMetadata",
    "BigqueryUpdPerm",
    "BigqueryUpdPermColumns",
    "BigqueryUpdPermColumnsZero",
    "BigqueryUpdatePermDef",
    "BodyTransformFnModifyAsFormUrlEncoded",
    "BodyTransformFnModifyAsJson",
    "BodyTransformFnRemove",
    "CertVar",
    "CitusArrRelUsingFKeyOnMultipleColumns",
    "CitusArrRelUsingFKeyOnSingleColumn",
    "CitusBoolExp",
    "CitusComputedFieldMetadata",
    "CitusDelPerm",
    "CitusDeletePermDef",
    "CitusEventTriggerConfEventTriggerConf",
    "CitusEventTriggerConfEventTriggerConfHeadersItem",
    "CitusEventTriggerConfEventTriggerConfRequestTransform",
    "CitusEventTriggerConfEventTriggerConfResponseTransform",
    "CitusFunctionMetadata",
    "CitusHealthCheckConfig",
    "CitusInsPerm",
    "CitusInsPermColumns",
    "CitusInsPermColumnsZero",
    "CitusInsertPermDef",
    "CitusLogicalModelField",
    "CitusLogicalModelMetadata",
    "CitusNativeQueryMetadata",
    "CitusNullableScalarType",
    "CitusObjRelRemoteTableMultipleColumns",
    "CitusObjRelRemoteTableSingleColumn",
    "CitusRelManualNativeQueryConfig",
    "CitusRelManualNativeQueryConfigInsertionOrder",
    "CitusRelManualTableConfig",
    "CitusRelManualTableConfigInsertionOrder",
    "CitusRuManual",
    "CitusSelPerm",
    "CitusSelPermColumns",
    "CitusSelPermColumnsZero",
    "CitusSelPermQueryRootFieldsItem",
    "CitusSelPermSubscriptionRootFieldsItem",
    "CitusSelectPermDef",
    "CitusSourceMetadata",
    "CitusSourceMetadataKind",
    "CitusStoredProcedureMetadata",
    "CitusSubscribeOpSpec",
    "CitusSubscribeOpSpecColumns",
    "CitusSubscribeOpSpecColumnsZero",
    "CitusSubscribeOpSpecPayload",
    "CitusSubscribeOpSpecPayloadZero",
    "CitusTableConfig",
    "CitusTableMetadata",
    "CitusTriggerOpsDef",
    "CitusUpdPerm",
    "CitusUpdPermColumns",
    "CitusUpdPermColumnsZero",
    "CitusUpdatePermDef",
    "CockroachArrRelUsingFKeyOnMultipleColumns",
    "CockroachArrRelUsingFKeyOnSingleColumn",
    "CockroachBoolExp",
    "CockroachComputedFieldMetadata",
    "CockroachDelPerm",
    "CockroachDeletePermDef",
    "CockroachEventTriggerConfEventTriggerConf",
    "CockroachEventTriggerConfEventTriggerConfHeadersItem",
    "CockroachEventTriggerConfEventTriggerConfRequestTransform",
    "CockroachEventTriggerConfEventTriggerConfResponseTransform",
    "CockroachFunctionMetadata",
    "CockroachHealthCheckConfig",
    "CockroachInsPerm",
    "CockroachInsPermColumns",
    "CockroachInsPermColumnsZero",
    "CockroachInsertPermDef",
    "CockroachLogicalModelField",
    "CockroachLogicalModelMetadata",
    "CockroachNativeQueryMetadata",
    "CockroachNullableScalarType",
    "CockroachObjRelRemoteTableMultipleColumns",
    "CockroachObjRelRemoteTableSingleColumn",
    "CockroachRelManualNativeQueryConfig",
    "CockroachRelManualNativeQueryConfigInsertionOrder",
    "CockroachRelManualTableConfig",
    "CockroachRelManualTableConfigInsertionOrder",
    "CockroachRuManual",
    "CockroachSelPerm",
    "CockroachSelPermColumns",
    "CockroachSelPermColumnsZero",
    "CockroachSelPermQueryRootFieldsItem",
    "CockroachSelPermSubscriptionRootFieldsItem",
    "CockroachSelectPermDef",
    "CockroachSourceMetadata",
    "CockroachSourceMetadataKind",
    "CockroachStoredProcedureMetadata",
    "CockroachSubscribeOpSpec",
    "CockroachSubscribeOpSpecColumns",
    "CockroachSubscribeOpSpecColumnsZero",
    "CockroachSubscribeOpSpecPayload",
    "CockroachSubscribeOpSpecPayloadZero",
    "CockroachTableConfig",
    "CockroachTableMetadata",
    "CockroachTriggerOpsDef",
    "CockroachUpdPerm",
    "CockroachUpdPermColumns",
    "CockroachUpdPermColumnsZero",
    "CockroachUpdatePermDef",
    "CollectionDef",
    "ColumnConfig",
    "Config",
    "ConnectionTemplate",
    "CreateCollection",
    "CronSchedule",
    "CronTriggerMetadata",
    "CronTriggerMetadataHeadersItem",
    "CronTriggerMetadataRequestTransform",
    "CronTriggerMetadataResponseTransform",
    "CustomRootField",
    "CustomTypes",
    "DataConnectorConnSourceConfig",
    "DataConnectorConnSourceConfigTimeout",
    "DataConnectorOptions",
    "DataConnectorOptionsUri",
    "DataConnectorSourceTimeoutMicroseconds",
    "DataConnectorSourceTimeoutMilliseconds",
    "DataConnectorSourceTimeoutSeconds",
    "DataconnectorArrRelUsingFKeyOnMultipleColumns",
    "DataconnectorArrRelUsingFKeyOnMultipleColumnsColumnsItem",
    "DataconnectorArrRelUsingFKeyOnSingleColumn",
    "DataconnectorArrRelUsingFKeyOnSingleColumnColumn",
    "DataconnectorBoolExp",
    "DataconnectorComputedFieldMetadata",
    "DataconnectorDelPerm",
    "DataconnectorDeletePermDef",
    "DataconnectorFunctionMetadata",
    "DataconnectorInsPerm",
    "DataconnectorInsPermColumns",
    "DataconnectorInsPermColumnsZero",
    "DataconnectorInsertPermDef",
    "DataconnectorLogicalModelField",
    "DataconnectorLogicalModelMetadata",
    "DataconnectorNativeQueryMetadata",
    "DataconnectorNullableScalarType",
    "DataconnectorObjRelRemoteTableMultipleColumns",
    "DataconnectorObjRelRemoteTableMultipleColumnsColumnsItem",
    "DataconnectorObjRelRemoteTableSingleColumn",
    "DataconnectorObjRelRemoteTableSingleColumnColumn",
    "DataconnectorRelManualNativeQueryConfig",
    "DataconnectorRelManualNativeQueryConfigInsertionOrder",
    "DataconnectorRelManualTableConfig",
    "DataconnectorRelManualTableConfigInsertionOrder",
    "DataconnectorRuManual",
    "DataconnectorSelPerm",
    "DataconnectorSelPermColumns",
    "DataconnectorSelPermColumnsZero",
    "DataconnectorSelPermQueryRootFieldsItem",
    "DataconnectorSelPermSubscriptionRootFieldsItem",
    "DataconnectorSelectPermDef",
    "DataconnectorSourceMetadata",
    "DataconnectorStoredProcedureMetadata",
    "DataconnectorTableConfig",
    "DataconnectorTableMetadata",
    "DataconnectorUpdPerm",
    "DataconnectorUpdPermColumns",
    "DataconnectorUpdPermColumnsZero",
    "DataconnectorUpdatePermDef",
    "EndpointDefQueryReference",
    "EndpointMetadataQueryReference",
    "EndpointMetadataQueryReferenceMethodsItem",
    "EnumTypeDefinition",
    "EnumValueDefinition",
    "ExtensionsSchema",
    "FieldCall",
    "FromEnv",
    "FunctionConfig",
    "FunctionConfigExposedAs",
    "FunctionCustomRootFields",
    "FunctionPermissionInfo",
    "FunctionReturnType",
    "GraphQlName",
    "GraphQlSchema",
    "GraphQlValueName",
    "HeaderConfFromEnv",
    "HeaderConfValue",
    "HealthCheckTestSql",
    "InferredFunctionResponse",
    "InferredFunctionResponseType",
    "InputObjectFieldDefinition",
    "InputObjectTypeDefinition",
    "LimitMaxBatchSize",
    "LimitMaxDepth",
    "LimitMaxNodes",
    "LimitMaxTime",
    "LimitRateLimitConfig",
    "ListedQuery",
    "Metadata",
    "MetadataV1",
    "MetadataV2",
    "MetadataV3",
    "MetricsConfig",
    "MssqlArrRelUsingFKeyOnMultipleColumns",
    "MssqlArrRelUsingFKeyOnSingleColumn",
    "MssqlBoolExp",
    "MssqlComputedFieldMetadata",
    "MssqlConnConfiguration",
    "MssqlConnectionInfo",
    "MssqlConnectionInfoConnectionString",
    "MssqlDelPerm",
    "MssqlDeletePermDef",
    "MssqlEventTriggerConfEventTriggerConf",
    "MssqlEventTriggerConfEventTriggerConfHeadersItem",
    "MssqlEventTriggerConfEventTriggerConfRequestTransform",
    "MssqlEventTriggerConfEventTriggerConfResponseTransform",
    "MssqlFunctionMetadata",
    "MssqlFunctionName",
    "MssqlHealthCheckConfig",
    "MssqlInsPerm",
    "MssqlInsPermColumns",
    "MssqlInsPermColumnsZero",
    "MssqlInsertPermDef",
    "MssqlLogicalModelField",
    "MssqlLogicalModelMetadata",
    "MssqlNativeQueryMetadata",
    "MssqlNullableScalarType",
    "MssqlObjRelRemoteTableMultipleColumns",
    "MssqlObjRelRemoteTableSingleColumn",
    "MssqlPoolSettings",
    "MssqlRelManualNativeQueryConfig",
    "MssqlRelManualNativeQueryConfigInsertionOrder",
    "MssqlRelManualTableConfig",
    "MssqlRelManualTableConfigInsertionOrder",
    "MssqlRuManual",
    "MssqlSelPerm",
    "MssqlSelPermColumns",
    "MssqlSelPermColumnsZero",
    "MssqlSelPermQueryRootFieldsItem",
    "MssqlSelPermSubscriptionRootFieldsItem",
    "MssqlSelectPermDef",
    "MssqlSourceMetadata",
    "MssqlSourceMetadataKind",
    "MssqlStoredProcedureMetadata",
    "MssqlSubscribeOpSpec",
    "MssqlSubscribeOpSpecColumns",
    "MssqlSubscribeOpSpecColumnsZero",
    "MssqlSubscribeOpSpecPayload",
    "MssqlSubscribeOpSpecPayloadZero",
    "MssqlTableConfig",
    "MssqlTableMetadata",
    "MssqlTableName",
    "MssqlTriggerOpsDef",
    "MssqlUpdPerm",
    "MssqlUpdPermColumns",
    "MssqlUpdPermColumnsZero",
    "MssqlUpdatePermDef",
    "NamingCase",
    "Network",
    "ObjectFieldDefinitionGraphQlType",
    "ObjectTypeDefinition",
    "OpenTelemetryConfig",
    "OpenTelemetryConfigDataTypesItem",
    "OtelBatchSpanProcessorConfig",
    "OtelExporterConfig",
    "OtelExporterConfigHeadersItem",
    "OtelExporterConfigProtocol",
    "OtelExporterConfigTracesPropagatorsItem",
    "OtelNameValue",
    "PgClientCerts",
    "PgConnectionParams",
    "PostgresArrRelUsingFKeyOnMultipleColumns",
    "PostgresArrRelUsingFKeyOnSingleColumn",
    "PostgresBoolExp",
    "PostgresComputedFieldDefinition",
    "PostgresComputedFieldMetadata",
    "PostgresConnConfiguration",
    "PostgresDelPerm",
    "PostgresDeletePermDef",
    "PostgresEventTriggerConfEventTriggerConf",
    "PostgresEventTriggerConfEventTriggerConfHeadersItem",
    "PostgresEventTriggerConfEventTriggerConfRequestTransform",
    "PostgresEventTriggerConfEventTriggerConfResponseTransform",
    "PostgresFunctionMetadata",
    "PostgresHealthCheckConfig",
    "PostgresInsPerm",
    "PostgresInsPermColumns",
    "PostgresInsPermColumnsZero",
    "PostgresInsertPermDef",
    "PostgresLogicalModelField",
    "PostgresLogicalModelMetadata",
    "PostgresNativeQueryMetadata",
    "PostgresNullableScalarType",
    "PostgresObjRelRemoteTableMultipleColumns",
    "PostgresObjRelRemoteTableSingleColumn",
    "PostgresPoolSettings",
    "PostgresQualifiedFunctionName",
    "PostgresQualifiedTableName",
    "PostgresRelManualNativeQueryConfig",
    "PostgresRelManualNativeQueryConfigInsertionOrder",
    "PostgresRelManualTableConfig",
    "PostgresRelManualTableConfigInsertionOrder",
    "PostgresRuManual",
    "PostgresSelPerm",
    "PostgresSelPermColumns",
    "PostgresSelPermColumnsZero",
    "PostgresSelPermQueryRootFieldsItem",
    "PostgresSelPermSubscriptionRootFieldsItem",
    "PostgresSelectPermDef",
    "PostgresSourceConnInfo",
    "PostgresSourceConnInfoDatabaseUrl",
    "PostgresSourceMetadata",
    "PostgresSourceMetadataKind",
    "PostgresStoredProcedureMetadata",
    "PostgresSubscribeOpSpec",
    "PostgresSubscribeOpSpecColumns",
    "PostgresSubscribeOpSpecColumnsZero",
    "PostgresSubscribeOpSpecPayload",
    "PostgresSubscribeOpSpecPayloadZero",
    "PostgresTableConfig",
    "PostgresTableMetadata",
    "PostgresTriggerOpsDef",
    "PostgresUpdPerm",
    "PostgresUpdPermColumns",
    "PostgresUpdPermColumnsZero",
    "PostgresUpdatePermDef",
    "QueryReference",
    "QueryTagsConfig",
    "QueryTagsFormat",
    "RateLimitConfig",
    "RateLimitConfigUniqueParams",
    "RateLimitConfigUniqueParamsZero",
    "RelDefRelManualConfigBigQuery",
    "RelDefRelManualConfigDataConnector",
    "RelDefRelManualConfigMssql",
    "RelDefRelManualConfigPostgresCitus",
    "RelDefRelManualConfigPostgresCockroach",
    "RelDefRelManualConfigPostgresVanilla",
    "RelDefRelUsingBigQueryArrRelUsingFKeyOnBigQuery",
    "RelDefRelUsingBigQueryArrRelUsingFKeyOnBigQueryUsing",
    "RelDefRelUsingBigQueryObjRelUsingChoiceBigQuery",
    "RelDefRelUsingBigQueryObjRelUsingChoiceBigQueryUsing",
    "RelDefRelUsingDataConnectorArrRelUsingFKeyOnDataConnector",
    "RelDefRelUsingDataConnectorArrRelUsingFKeyOnDataConnectorUsing",
    "RelDefRelUsingDataConnectorObjRelUsingChoiceDataConnector",
    "RelDefRelUsingDataConnectorObjRelUsingChoiceDataConnectorUsing",
    "RelDefRelUsingMssqlArrRelUsingFKeyOnMssql",
    "RelDefRelUsingMssqlArrRelUsingFKeyOnMssqlUsing",
    "RelDefRelUsingMssqlObjRelUsingChoiceMssql",
    "RelDefRelUsingMssqlObjRelUsingChoiceMssqlUsing",
    "RelDefRelUsingPostgresCitusArrRelUsingFKeyOnPostgresCitus",
    "RelDefRelUsingPostgresCitusArrRelUsingFKeyOnPostgresCitusUsing",
    "RelDefRelUsingPostgresCitusObjRelUsingChoicePostgresCitus",
    "RelDefRelUsingPostgresCitusObjRelUsingChoicePostgresCitusUsing",
    "RelDefRelUsingPostgresCockroachArrRelUsingFKeyOnPostgresCockroach",
    "RelDefRelUsingPostgresCockroachArrRelUsingFKeyOnPostgresCockroachUsing",
    "RelDefRelUsingPostgresCockroachObjRelUsingChoicePostgresCockroach",
    "RelDefRelUsingPostgresCockroachObjRelUsingChoicePostgresCockroachUsing",
    "RelDefRelUsingPostgresVanillaArrRelUsingFKeyOnPostgresVanilla",
    "RelDefRelUsingPostgresVanillaArrRelUsingFKeyOnPostgresVanillaUsing",
    "RelDefRelUsingPostgresVanillaObjRelUsingChoicePostgresVanilla",
    "RelDefRelUsingPostgresVanillaObjRelUsingChoicePostgresVanillaUsing",
    "RelationshipToSchema",
    "RelationshipToSource",
    "RemoteArguments",
    "RemoteFieldCustomization",
    "RemoteFields",
    "RemoteRelationshipRemoteRelationshipDefinition",
    "RemoteRelationshipRemoteRelationshipDefinitionDefinition",
    "RemoteSchemaCustomization",
    "RemoteSchemaDef",
    "RemoteSchemaDefHeadersItem",
    "RemoteSchemaDefIntrospectionHeadersItem",
    "RemoteSchemaMetadataRemoteRelationshipDefinition",
    "RemoteSchemaPermissionDefinition",
    "RemoteSchemaPermissionMetadata",
    "RemoteTypeCustomization",
    "RequestTransformV1",
    "RequestTransformV1QueryParams",
    "RequestTransformV1TemplateEngine",
    "RequestTransformV2",
    "RequestTransformV2Body",
    "RequestTransformV2Body_Remove",
    "RequestTransformV2Body_Transform",
    "RequestTransformV2Body_XWwwFormUrlencoded",
    "RequestTransformV2QueryParams",
    "RequestTransformV2TemplateEngine",
    "ResponseTransformV1",
    "ResponseTransformV1TemplateEngine",
    "ResponseTransformV2",
    "ResponseTransformV2Body",
    "ResponseTransformV2Body_Remove",
    "ResponseTransformV2Body_Transform",
    "ResponseTransformV2Body_XWwwFormUrlencoded",
    "ResponseTransformV2TemplateEngine",
    "RetryConf",
    "Role",
    "RootFieldsCustomization",
    "RufKeyOnArrRelUsingFKeyOnBigQuery",
    "RufKeyOnArrRelUsingFKeyOnBigQueryForeignKeyConstraintOn",
    "RufKeyOnArrRelUsingFKeyOnDataConnector",
    "RufKeyOnArrRelUsingFKeyOnDataConnectorForeignKeyConstraintOn",
    "RufKeyOnArrRelUsingFKeyOnMssql",
    "RufKeyOnArrRelUsingFKeyOnMssqlForeignKeyConstraintOn",
    "RufKeyOnArrRelUsingFKeyOnPostgresCitus",
    "RufKeyOnArrRelUsingFKeyOnPostgresCitusForeignKeyConstraintOn",
    "RufKeyOnArrRelUsingFKeyOnPostgresCockroach",
    "RufKeyOnArrRelUsingFKeyOnPostgresCockroachForeignKeyConstraintOn",
    "RufKeyOnArrRelUsingFKeyOnPostgresVanilla",
    "RufKeyOnArrRelUsingFKeyOnPostgresVanillaForeignKeyConstraintOn",
    "RufKeyOnObjRelUsingChoiceBigQuery",
    "RufKeyOnObjRelUsingChoiceBigQueryForeignKeyConstraintOn",
    "RufKeyOnObjRelUsingChoiceDataConnector",
    "RufKeyOnObjRelUsingChoiceDataConnectorForeignKeyConstraintOn",
    "RufKeyOnObjRelUsingChoiceDataConnectorForeignKeyConstraintOnTwoItem",
    "RufKeyOnObjRelUsingChoiceMssql",
    "RufKeyOnObjRelUsingChoiceMssqlForeignKeyConstraintOn",
    "RufKeyOnObjRelUsingChoicePostgresCitus",
    "RufKeyOnObjRelUsingChoicePostgresCitusForeignKeyConstraintOn",
    "RufKeyOnObjRelUsingChoicePostgresCockroach",
    "RufKeyOnObjRelUsingChoicePostgresCockroachForeignKeyConstraintOn",
    "RufKeyOnObjRelUsingChoicePostgresVanilla",
    "RufKeyOnObjRelUsingChoicePostgresVanillaForeignKeyConstraintOn",
    "ScalarType",
    "ScalarTypeDefinition",
    "SourceCustomization",
    "SourceMetadata",
    "SourceTypeCustomization",
    "SslMode",
    "StRetryConf",
    "StoredProcedureConfig",
    "StoredProcedureConfigExposedAs",
    "TableCustomRootFields",
    "TableCustomRootFieldsDelete",
    "TableCustomRootFieldsDeleteByPk",
    "TableCustomRootFieldsInsert",
    "TableCustomRootFieldsInsertOne",
    "TableCustomRootFieldsSelect",
    "TableCustomRootFieldsSelectAggregate",
    "TableCustomRootFieldsSelectByPk",
    "TableCustomRootFieldsSelectStream",
    "TableCustomRootFieldsUpdate",
    "TableCustomRootFieldsUpdateByPk",
    "TableCustomRootFieldsUpdateMany",
    "TableFunctionResponse",
    "TableFunctionResponseType",
    "TemplateVariableDynamicFromFile",
    "TemplateVariableDynamicFromFileType",
    "TemplateVariableSource",
    "TlsAllow",
    "TlsAllowPermissionsItem",
    "ToSchemaRelationshipDef",
    "ToSchemaRelationshipDefLegacyFormat",
    "ToSourceRelationshipDef",
    "ToSourceRelationshipDefRelationshipType",
    "TxIsolation",
    "TypeRelationshipDefinition",
    "TypeRelationshipDefinitionType",
    "UrlConfFromParams",
    "UrlConfFromParamsConnectionParameters",
    "UrlConfFromParamsConnectionParametersLeft",
    "UrlConfFromParamsConnectionParametersRight",
    "ValidateInputHttpDefinition",
    "ValidateInputHttpDefinitionHeadersItem",
    "ValidateInputInputWebhook",
    "ValidateInputInputWebhookType",
]
