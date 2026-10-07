



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .connect_v1alter_offset_request_info import ConnectV1AlterOffsetRequestInfo
    from .connect_v1alter_offset_request_info_offsets_item import ConnectV1AlterOffsetRequestInfoOffsetsItem
    from .connect_v1alter_offset_request_type import ConnectV1AlterOffsetRequestType
    from .connect_v1alter_offset_status import ConnectV1AlterOffsetStatus
    from .connect_v1alter_offset_status_previous_offsets_item import ConnectV1AlterOffsetStatusPreviousOffsetsItem
    from .connect_v1alter_offset_status_status import ConnectV1AlterOffsetStatusStatus
    from .connect_v1connector import ConnectV1Connector
    from .connect_v1connector_config import ConnectV1ConnectorConfig
    from .connect_v1connector_error import ConnectV1ConnectorError
    from .connect_v1connector_error_error import ConnectV1ConnectorErrorError
    from .connect_v1connector_expansion import ConnectV1ConnectorExpansion
    from .connect_v1connector_expansion_id import ConnectV1ConnectorExpansionId
    from .connect_v1connector_expansion_info import ConnectV1ConnectorExpansionInfo
    from .connect_v1connector_expansion_info_config import ConnectV1ConnectorExpansionInfoConfig
    from .connect_v1connector_expansion_map import ConnectV1ConnectorExpansionMap
    from .connect_v1connector_expansion_status import ConnectV1ConnectorExpansionStatus
    from .connect_v1connector_expansion_status_connector import ConnectV1ConnectorExpansionStatusConnector
    from .connect_v1connector_expansion_status_connector_state import ConnectV1ConnectorExpansionStatusConnectorState
    from .connect_v1connector_expansion_status_type import ConnectV1ConnectorExpansionStatusType
    from .connect_v1connector_offsets import ConnectV1ConnectorOffsets
    from .connect_v1connector_offsets_metadata import ConnectV1ConnectorOffsetsMetadata
    from .connect_v1connector_offsets_offsets_item import ConnectV1ConnectorOffsetsOffsetsItem
    from .connect_v1connector_tasks import ConnectV1ConnectorTasks
    from .connect_v1connector_type import ConnectV1ConnectorType
    from .connect_v1connector_with_offsets import ConnectV1ConnectorWithOffsets
    from .connect_v1connector_with_offsets_config import ConnectV1ConnectorWithOffsetsConfig
    from .connect_v1connector_with_offsets_offsets_item import ConnectV1ConnectorWithOffsetsOffsetsItem
    from .connect_v1connector_with_offsets_type import ConnectV1ConnectorWithOffsetsType
    from .connect_v1connectors import ConnectV1Connectors
    from .connect_v1connectors_item import ConnectV1ConnectorsItem
    from .connect_v1connectors_item_config import ConnectV1ConnectorsItemConfig
    from .connect_v1connectors_item_id import ConnectV1ConnectorsItemId
    from .connect_v1offsets import ConnectV1Offsets
    from .connect_v1offsets_item import ConnectV1OffsetsItem
    from .inline_response200 import InlineResponse200
    from .inline_response2001 import InlineResponse2001
    from .inline_response2001connector import InlineResponse2001Connector
    from .inline_response2001connector_state import InlineResponse2001ConnectorState
    from .inline_response2001tasks import InlineResponse2001Tasks
    from .inline_response2001type import InlineResponse2001Type
    from .inline_response2002 import InlineResponse2002
    from .inline_response2002type import InlineResponse2002Type
    from .inline_response2003 import InlineResponse2003
    from .inline_response2003configs import InlineResponse2003Configs
    from .inline_response2003definition import InlineResponse2003Definition
    from .inline_response2003definition_importance import InlineResponse2003DefinitionImportance
    from .inline_response2003definition_type import InlineResponse2003DefinitionType
    from .inline_response2003definition_width import InlineResponse2003DefinitionWidth
    from .inline_response2003value import InlineResponse2003Value
    from .inline_response400 import InlineResponse400
    from .inline_response500 import InlineResponse500
_dynamic_imports: typing.Dict[str, str] = {
    "ConnectV1AlterOffsetRequestInfo": ".connect_v1alter_offset_request_info",
    "ConnectV1AlterOffsetRequestInfoOffsetsItem": ".connect_v1alter_offset_request_info_offsets_item",
    "ConnectV1AlterOffsetRequestType": ".connect_v1alter_offset_request_type",
    "ConnectV1AlterOffsetStatus": ".connect_v1alter_offset_status",
    "ConnectV1AlterOffsetStatusPreviousOffsetsItem": ".connect_v1alter_offset_status_previous_offsets_item",
    "ConnectV1AlterOffsetStatusStatus": ".connect_v1alter_offset_status_status",
    "ConnectV1Connector": ".connect_v1connector",
    "ConnectV1ConnectorConfig": ".connect_v1connector_config",
    "ConnectV1ConnectorError": ".connect_v1connector_error",
    "ConnectV1ConnectorErrorError": ".connect_v1connector_error_error",
    "ConnectV1ConnectorExpansion": ".connect_v1connector_expansion",
    "ConnectV1ConnectorExpansionId": ".connect_v1connector_expansion_id",
    "ConnectV1ConnectorExpansionInfo": ".connect_v1connector_expansion_info",
    "ConnectV1ConnectorExpansionInfoConfig": ".connect_v1connector_expansion_info_config",
    "ConnectV1ConnectorExpansionMap": ".connect_v1connector_expansion_map",
    "ConnectV1ConnectorExpansionStatus": ".connect_v1connector_expansion_status",
    "ConnectV1ConnectorExpansionStatusConnector": ".connect_v1connector_expansion_status_connector",
    "ConnectV1ConnectorExpansionStatusConnectorState": ".connect_v1connector_expansion_status_connector_state",
    "ConnectV1ConnectorExpansionStatusType": ".connect_v1connector_expansion_status_type",
    "ConnectV1ConnectorOffsets": ".connect_v1connector_offsets",
    "ConnectV1ConnectorOffsetsMetadata": ".connect_v1connector_offsets_metadata",
    "ConnectV1ConnectorOffsetsOffsetsItem": ".connect_v1connector_offsets_offsets_item",
    "ConnectV1ConnectorTasks": ".connect_v1connector_tasks",
    "ConnectV1ConnectorType": ".connect_v1connector_type",
    "ConnectV1ConnectorWithOffsets": ".connect_v1connector_with_offsets",
    "ConnectV1ConnectorWithOffsetsConfig": ".connect_v1connector_with_offsets_config",
    "ConnectV1ConnectorWithOffsetsOffsetsItem": ".connect_v1connector_with_offsets_offsets_item",
    "ConnectV1ConnectorWithOffsetsType": ".connect_v1connector_with_offsets_type",
    "ConnectV1Connectors": ".connect_v1connectors",
    "ConnectV1ConnectorsItem": ".connect_v1connectors_item",
    "ConnectV1ConnectorsItemConfig": ".connect_v1connectors_item_config",
    "ConnectV1ConnectorsItemId": ".connect_v1connectors_item_id",
    "ConnectV1Offsets": ".connect_v1offsets",
    "ConnectV1OffsetsItem": ".connect_v1offsets_item",
    "InlineResponse200": ".inline_response200",
    "InlineResponse2001": ".inline_response2001",
    "InlineResponse2001Connector": ".inline_response2001connector",
    "InlineResponse2001ConnectorState": ".inline_response2001connector_state",
    "InlineResponse2001Tasks": ".inline_response2001tasks",
    "InlineResponse2001Type": ".inline_response2001type",
    "InlineResponse2002": ".inline_response2002",
    "InlineResponse2002Type": ".inline_response2002type",
    "InlineResponse2003": ".inline_response2003",
    "InlineResponse2003Configs": ".inline_response2003configs",
    "InlineResponse2003Definition": ".inline_response2003definition",
    "InlineResponse2003DefinitionImportance": ".inline_response2003definition_importance",
    "InlineResponse2003DefinitionType": ".inline_response2003definition_type",
    "InlineResponse2003DefinitionWidth": ".inline_response2003definition_width",
    "InlineResponse2003Value": ".inline_response2003value",
    "InlineResponse400": ".inline_response400",
    "InlineResponse500": ".inline_response500",
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
    "ConnectV1AlterOffsetRequestInfo",
    "ConnectV1AlterOffsetRequestInfoOffsetsItem",
    "ConnectV1AlterOffsetRequestType",
    "ConnectV1AlterOffsetStatus",
    "ConnectV1AlterOffsetStatusPreviousOffsetsItem",
    "ConnectV1AlterOffsetStatusStatus",
    "ConnectV1Connector",
    "ConnectV1ConnectorConfig",
    "ConnectV1ConnectorError",
    "ConnectV1ConnectorErrorError",
    "ConnectV1ConnectorExpansion",
    "ConnectV1ConnectorExpansionId",
    "ConnectV1ConnectorExpansionInfo",
    "ConnectV1ConnectorExpansionInfoConfig",
    "ConnectV1ConnectorExpansionMap",
    "ConnectV1ConnectorExpansionStatus",
    "ConnectV1ConnectorExpansionStatusConnector",
    "ConnectV1ConnectorExpansionStatusConnectorState",
    "ConnectV1ConnectorExpansionStatusType",
    "ConnectV1ConnectorOffsets",
    "ConnectV1ConnectorOffsetsMetadata",
    "ConnectV1ConnectorOffsetsOffsetsItem",
    "ConnectV1ConnectorTasks",
    "ConnectV1ConnectorType",
    "ConnectV1ConnectorWithOffsets",
    "ConnectV1ConnectorWithOffsetsConfig",
    "ConnectV1ConnectorWithOffsetsOffsetsItem",
    "ConnectV1ConnectorWithOffsetsType",
    "ConnectV1Connectors",
    "ConnectV1ConnectorsItem",
    "ConnectV1ConnectorsItemConfig",
    "ConnectV1ConnectorsItemId",
    "ConnectV1Offsets",
    "ConnectV1OffsetsItem",
    "InlineResponse200",
    "InlineResponse2001",
    "InlineResponse2001Connector",
    "InlineResponse2001ConnectorState",
    "InlineResponse2001Tasks",
    "InlineResponse2001Type",
    "InlineResponse2002",
    "InlineResponse2002Type",
    "InlineResponse2003",
    "InlineResponse2003Configs",
    "InlineResponse2003Definition",
    "InlineResponse2003DefinitionImportance",
    "InlineResponse2003DefinitionType",
    "InlineResponse2003DefinitionWidth",
    "InlineResponse2003Value",
    "InlineResponse400",
    "InlineResponse500",
]
