



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .channel_permission_override_delete_request_contact_type import (
        ChannelPermissionOverrideDeleteRequestContactType,
    )
    from .channel_permission_override_delete_request_selector import (
        ChannelPermissionOverrideDeleteRequestSelector,
        ChannelPermissionOverrideDeleteRequestSelector_Adapter,
        ChannelPermissionOverrideDeleteRequestSelector_Channel,
        ChannelPermissionOverrideDeleteRequestSelector_ChannelType,
        ChannelPermissionOverrideDeleteRequestSelector_Workspace,
    )
    from .channel_permission_override_delete_request_selector_adapter import (
        ChannelPermissionOverrideDeleteRequestSelectorAdapter,
    )
    from .channel_permission_override_delete_request_selector_channel import (
        ChannelPermissionOverrideDeleteRequestSelectorChannel,
    )
    from .channel_permission_override_delete_request_selector_channel_type import (
        ChannelPermissionOverrideDeleteRequestSelectorChannelType,
    )
    from .channel_permission_override_delete_request_selector_channel_type_channel_type import (
        ChannelPermissionOverrideDeleteRequestSelectorChannelTypeChannelType,
    )
    from .channel_permission_override_delete_request_selector_workspace import (
        ChannelPermissionOverrideDeleteRequestSelectorWorkspace,
    )
    from .channel_permission_override_delete_response import ChannelPermissionOverrideDeleteResponse
    from .channel_permission_override_set_request_contact_type import ChannelPermissionOverrideSetRequestContactType
    from .channel_permission_override_set_request_selector import (
        ChannelPermissionOverrideSetRequestSelector,
        ChannelPermissionOverrideSetRequestSelector_Adapter,
        ChannelPermissionOverrideSetRequestSelector_Channel,
        ChannelPermissionOverrideSetRequestSelector_ChannelType,
        ChannelPermissionOverrideSetRequestSelector_Workspace,
    )
    from .channel_permission_override_set_request_selector_adapter import (
        ChannelPermissionOverrideSetRequestSelectorAdapter,
    )
    from .channel_permission_override_set_request_selector_channel import (
        ChannelPermissionOverrideSetRequestSelectorChannel,
    )
    from .channel_permission_override_set_request_selector_channel_type import (
        ChannelPermissionOverrideSetRequestSelectorChannelType,
    )
    from .channel_permission_override_set_request_selector_channel_type_channel_type import (
        ChannelPermissionOverrideSetRequestSelectorChannelTypeChannelType,
    )
    from .channel_permission_override_set_request_selector_workspace import (
        ChannelPermissionOverrideSetRequestSelectorWorkspace,
    )
    from .channel_permission_override_set_request_threshold import ChannelPermissionOverrideSetRequestThreshold
    from .channel_permission_override_set_response import ChannelPermissionOverrideSetResponse
    from .channel_permission_override_set_response_cell import ChannelPermissionOverrideSetResponseCell
    from .channel_permission_override_set_response_cell_contact_type import (
        ChannelPermissionOverrideSetResponseCellContactType,
    )
    from .channel_permission_override_set_response_cell_selector import (
        ChannelPermissionOverrideSetResponseCellSelector,
        ChannelPermissionOverrideSetResponseCellSelector_Adapter,
        ChannelPermissionOverrideSetResponseCellSelector_Channel,
        ChannelPermissionOverrideSetResponseCellSelector_ChannelType,
        ChannelPermissionOverrideSetResponseCellSelector_Workspace,
    )
    from .channel_permission_override_set_response_cell_selector_adapter import (
        ChannelPermissionOverrideSetResponseCellSelectorAdapter,
    )
    from .channel_permission_override_set_response_cell_selector_channel import (
        ChannelPermissionOverrideSetResponseCellSelectorChannel,
    )
    from .channel_permission_override_set_response_cell_selector_channel_type import (
        ChannelPermissionOverrideSetResponseCellSelectorChannelType,
    )
    from .channel_permission_override_set_response_cell_selector_channel_type_channel_type import (
        ChannelPermissionOverrideSetResponseCellSelectorChannelTypeChannelType,
    )
    from .channel_permission_override_set_response_cell_selector_workspace import (
        ChannelPermissionOverrideSetResponseCellSelectorWorkspace,
    )
    from .channel_permission_override_set_response_cell_threshold import (
        ChannelPermissionOverrideSetResponseCellThreshold,
    )
    from .channel_permission_overrides_list_response import ChannelPermissionOverridesListResponse
    from .channel_permission_overrides_list_response_cells_item import ChannelPermissionOverridesListResponseCellsItem
    from .channel_permission_overrides_list_response_cells_item_contact_type import (
        ChannelPermissionOverridesListResponseCellsItemContactType,
    )
    from .channel_permission_overrides_list_response_cells_item_selector import (
        ChannelPermissionOverridesListResponseCellsItemSelector,
        ChannelPermissionOverridesListResponseCellsItemSelector_Adapter,
        ChannelPermissionOverridesListResponseCellsItemSelector_Channel,
        ChannelPermissionOverridesListResponseCellsItemSelector_ChannelType,
        ChannelPermissionOverridesListResponseCellsItemSelector_Workspace,
    )
    from .channel_permission_overrides_list_response_cells_item_selector_adapter import (
        ChannelPermissionOverridesListResponseCellsItemSelectorAdapter,
    )
    from .channel_permission_overrides_list_response_cells_item_selector_channel import (
        ChannelPermissionOverridesListResponseCellsItemSelectorChannel,
    )
    from .channel_permission_overrides_list_response_cells_item_selector_channel_type import (
        ChannelPermissionOverridesListResponseCellsItemSelectorChannelType,
    )
    from .channel_permission_overrides_list_response_cells_item_selector_channel_type_channel_type import (
        ChannelPermissionOverridesListResponseCellsItemSelectorChannelTypeChannelType,
    )
    from .channel_permission_overrides_list_response_cells_item_selector_workspace import (
        ChannelPermissionOverridesListResponseCellsItemSelectorWorkspace,
    )
    from .channel_permission_overrides_list_response_cells_item_threshold import (
        ChannelPermissionOverridesListResponseCellsItemThreshold,
    )
    from .channel_permission_resolve_request_channel_type import ChannelPermissionResolveRequestChannelType
    from .channel_permission_resolve_request_contact_type import ChannelPermissionResolveRequestContactType
    from .channel_permission_resolve_response import ChannelPermissionResolveResponse
    from .channel_permission_resolve_response_resolved import ChannelPermissionResolveResponseResolved
    from .channel_permission_resolve_response_resolved_scope import ChannelPermissionResolveResponseResolvedScope
    from .channel_permission_resolve_response_resolved_threshold import (
        ChannelPermissionResolveResponseResolvedThreshold,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "ChannelPermissionOverrideDeleteRequestContactType": ".channel_permission_override_delete_request_contact_type",
    "ChannelPermissionOverrideDeleteRequestSelector": ".channel_permission_override_delete_request_selector",
    "ChannelPermissionOverrideDeleteRequestSelectorAdapter": ".channel_permission_override_delete_request_selector_adapter",
    "ChannelPermissionOverrideDeleteRequestSelectorChannel": ".channel_permission_override_delete_request_selector_channel",
    "ChannelPermissionOverrideDeleteRequestSelectorChannelType": ".channel_permission_override_delete_request_selector_channel_type",
    "ChannelPermissionOverrideDeleteRequestSelectorChannelTypeChannelType": ".channel_permission_override_delete_request_selector_channel_type_channel_type",
    "ChannelPermissionOverrideDeleteRequestSelectorWorkspace": ".channel_permission_override_delete_request_selector_workspace",
    "ChannelPermissionOverrideDeleteRequestSelector_Adapter": ".channel_permission_override_delete_request_selector",
    "ChannelPermissionOverrideDeleteRequestSelector_Channel": ".channel_permission_override_delete_request_selector",
    "ChannelPermissionOverrideDeleteRequestSelector_ChannelType": ".channel_permission_override_delete_request_selector",
    "ChannelPermissionOverrideDeleteRequestSelector_Workspace": ".channel_permission_override_delete_request_selector",
    "ChannelPermissionOverrideDeleteResponse": ".channel_permission_override_delete_response",
    "ChannelPermissionOverrideSetRequestContactType": ".channel_permission_override_set_request_contact_type",
    "ChannelPermissionOverrideSetRequestSelector": ".channel_permission_override_set_request_selector",
    "ChannelPermissionOverrideSetRequestSelectorAdapter": ".channel_permission_override_set_request_selector_adapter",
    "ChannelPermissionOverrideSetRequestSelectorChannel": ".channel_permission_override_set_request_selector_channel",
    "ChannelPermissionOverrideSetRequestSelectorChannelType": ".channel_permission_override_set_request_selector_channel_type",
    "ChannelPermissionOverrideSetRequestSelectorChannelTypeChannelType": ".channel_permission_override_set_request_selector_channel_type_channel_type",
    "ChannelPermissionOverrideSetRequestSelectorWorkspace": ".channel_permission_override_set_request_selector_workspace",
    "ChannelPermissionOverrideSetRequestSelector_Adapter": ".channel_permission_override_set_request_selector",
    "ChannelPermissionOverrideSetRequestSelector_Channel": ".channel_permission_override_set_request_selector",
    "ChannelPermissionOverrideSetRequestSelector_ChannelType": ".channel_permission_override_set_request_selector",
    "ChannelPermissionOverrideSetRequestSelector_Workspace": ".channel_permission_override_set_request_selector",
    "ChannelPermissionOverrideSetRequestThreshold": ".channel_permission_override_set_request_threshold",
    "ChannelPermissionOverrideSetResponse": ".channel_permission_override_set_response",
    "ChannelPermissionOverrideSetResponseCell": ".channel_permission_override_set_response_cell",
    "ChannelPermissionOverrideSetResponseCellContactType": ".channel_permission_override_set_response_cell_contact_type",
    "ChannelPermissionOverrideSetResponseCellSelector": ".channel_permission_override_set_response_cell_selector",
    "ChannelPermissionOverrideSetResponseCellSelectorAdapter": ".channel_permission_override_set_response_cell_selector_adapter",
    "ChannelPermissionOverrideSetResponseCellSelectorChannel": ".channel_permission_override_set_response_cell_selector_channel",
    "ChannelPermissionOverrideSetResponseCellSelectorChannelType": ".channel_permission_override_set_response_cell_selector_channel_type",
    "ChannelPermissionOverrideSetResponseCellSelectorChannelTypeChannelType": ".channel_permission_override_set_response_cell_selector_channel_type_channel_type",
    "ChannelPermissionOverrideSetResponseCellSelectorWorkspace": ".channel_permission_override_set_response_cell_selector_workspace",
    "ChannelPermissionOverrideSetResponseCellSelector_Adapter": ".channel_permission_override_set_response_cell_selector",
    "ChannelPermissionOverrideSetResponseCellSelector_Channel": ".channel_permission_override_set_response_cell_selector",
    "ChannelPermissionOverrideSetResponseCellSelector_ChannelType": ".channel_permission_override_set_response_cell_selector",
    "ChannelPermissionOverrideSetResponseCellSelector_Workspace": ".channel_permission_override_set_response_cell_selector",
    "ChannelPermissionOverrideSetResponseCellThreshold": ".channel_permission_override_set_response_cell_threshold",
    "ChannelPermissionOverridesListResponse": ".channel_permission_overrides_list_response",
    "ChannelPermissionOverridesListResponseCellsItem": ".channel_permission_overrides_list_response_cells_item",
    "ChannelPermissionOverridesListResponseCellsItemContactType": ".channel_permission_overrides_list_response_cells_item_contact_type",
    "ChannelPermissionOverridesListResponseCellsItemSelector": ".channel_permission_overrides_list_response_cells_item_selector",
    "ChannelPermissionOverridesListResponseCellsItemSelectorAdapter": ".channel_permission_overrides_list_response_cells_item_selector_adapter",
    "ChannelPermissionOverridesListResponseCellsItemSelectorChannel": ".channel_permission_overrides_list_response_cells_item_selector_channel",
    "ChannelPermissionOverridesListResponseCellsItemSelectorChannelType": ".channel_permission_overrides_list_response_cells_item_selector_channel_type",
    "ChannelPermissionOverridesListResponseCellsItemSelectorChannelTypeChannelType": ".channel_permission_overrides_list_response_cells_item_selector_channel_type_channel_type",
    "ChannelPermissionOverridesListResponseCellsItemSelectorWorkspace": ".channel_permission_overrides_list_response_cells_item_selector_workspace",
    "ChannelPermissionOverridesListResponseCellsItemSelector_Adapter": ".channel_permission_overrides_list_response_cells_item_selector",
    "ChannelPermissionOverridesListResponseCellsItemSelector_Channel": ".channel_permission_overrides_list_response_cells_item_selector",
    "ChannelPermissionOverridesListResponseCellsItemSelector_ChannelType": ".channel_permission_overrides_list_response_cells_item_selector",
    "ChannelPermissionOverridesListResponseCellsItemSelector_Workspace": ".channel_permission_overrides_list_response_cells_item_selector",
    "ChannelPermissionOverridesListResponseCellsItemThreshold": ".channel_permission_overrides_list_response_cells_item_threshold",
    "ChannelPermissionResolveRequestChannelType": ".channel_permission_resolve_request_channel_type",
    "ChannelPermissionResolveRequestContactType": ".channel_permission_resolve_request_contact_type",
    "ChannelPermissionResolveResponse": ".channel_permission_resolve_response",
    "ChannelPermissionResolveResponseResolved": ".channel_permission_resolve_response_resolved",
    "ChannelPermissionResolveResponseResolvedScope": ".channel_permission_resolve_response_resolved_scope",
    "ChannelPermissionResolveResponseResolvedThreshold": ".channel_permission_resolve_response_resolved_threshold",
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
    "ChannelPermissionOverrideDeleteRequestContactType",
    "ChannelPermissionOverrideDeleteRequestSelector",
    "ChannelPermissionOverrideDeleteRequestSelectorAdapter",
    "ChannelPermissionOverrideDeleteRequestSelectorChannel",
    "ChannelPermissionOverrideDeleteRequestSelectorChannelType",
    "ChannelPermissionOverrideDeleteRequestSelectorChannelTypeChannelType",
    "ChannelPermissionOverrideDeleteRequestSelectorWorkspace",
    "ChannelPermissionOverrideDeleteRequestSelector_Adapter",
    "ChannelPermissionOverrideDeleteRequestSelector_Channel",
    "ChannelPermissionOverrideDeleteRequestSelector_ChannelType",
    "ChannelPermissionOverrideDeleteRequestSelector_Workspace",
    "ChannelPermissionOverrideDeleteResponse",
    "ChannelPermissionOverrideSetRequestContactType",
    "ChannelPermissionOverrideSetRequestSelector",
    "ChannelPermissionOverrideSetRequestSelectorAdapter",
    "ChannelPermissionOverrideSetRequestSelectorChannel",
    "ChannelPermissionOverrideSetRequestSelectorChannelType",
    "ChannelPermissionOverrideSetRequestSelectorChannelTypeChannelType",
    "ChannelPermissionOverrideSetRequestSelectorWorkspace",
    "ChannelPermissionOverrideSetRequestSelector_Adapter",
    "ChannelPermissionOverrideSetRequestSelector_Channel",
    "ChannelPermissionOverrideSetRequestSelector_ChannelType",
    "ChannelPermissionOverrideSetRequestSelector_Workspace",
    "ChannelPermissionOverrideSetRequestThreshold",
    "ChannelPermissionOverrideSetResponse",
    "ChannelPermissionOverrideSetResponseCell",
    "ChannelPermissionOverrideSetResponseCellContactType",
    "ChannelPermissionOverrideSetResponseCellSelector",
    "ChannelPermissionOverrideSetResponseCellSelectorAdapter",
    "ChannelPermissionOverrideSetResponseCellSelectorChannel",
    "ChannelPermissionOverrideSetResponseCellSelectorChannelType",
    "ChannelPermissionOverrideSetResponseCellSelectorChannelTypeChannelType",
    "ChannelPermissionOverrideSetResponseCellSelectorWorkspace",
    "ChannelPermissionOverrideSetResponseCellSelector_Adapter",
    "ChannelPermissionOverrideSetResponseCellSelector_Channel",
    "ChannelPermissionOverrideSetResponseCellSelector_ChannelType",
    "ChannelPermissionOverrideSetResponseCellSelector_Workspace",
    "ChannelPermissionOverrideSetResponseCellThreshold",
    "ChannelPermissionOverridesListResponse",
    "ChannelPermissionOverridesListResponseCellsItem",
    "ChannelPermissionOverridesListResponseCellsItemContactType",
    "ChannelPermissionOverridesListResponseCellsItemSelector",
    "ChannelPermissionOverridesListResponseCellsItemSelectorAdapter",
    "ChannelPermissionOverridesListResponseCellsItemSelectorChannel",
    "ChannelPermissionOverridesListResponseCellsItemSelectorChannelType",
    "ChannelPermissionOverridesListResponseCellsItemSelectorChannelTypeChannelType",
    "ChannelPermissionOverridesListResponseCellsItemSelectorWorkspace",
    "ChannelPermissionOverridesListResponseCellsItemSelector_Adapter",
    "ChannelPermissionOverridesListResponseCellsItemSelector_Channel",
    "ChannelPermissionOverridesListResponseCellsItemSelector_ChannelType",
    "ChannelPermissionOverridesListResponseCellsItemSelector_Workspace",
    "ChannelPermissionOverridesListResponseCellsItemThreshold",
    "ChannelPermissionResolveRequestChannelType",
    "ChannelPermissionResolveRequestContactType",
    "ChannelPermissionResolveResponse",
    "ChannelPermissionResolveResponseResolved",
    "ChannelPermissionResolveResponseResolvedScope",
    "ChannelPermissionResolveResponseResolvedThreshold",
]
