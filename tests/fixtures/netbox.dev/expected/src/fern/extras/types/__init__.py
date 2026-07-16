



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .extras_config_contexts_list_response import ExtrasConfigContextsListResponse
    from .extras_content_types_list_response import ExtrasContentTypesListResponse
    from .extras_custom_fields_list_response import ExtrasCustomFieldsListResponse
    from .extras_custom_links_list_response import ExtrasCustomLinksListResponse
    from .extras_export_templates_list_response import ExtrasExportTemplatesListResponse
    from .extras_image_attachments_list_response import ExtrasImageAttachmentsListResponse
    from .extras_job_results_list_response import ExtrasJobResultsListResponse
    from .extras_journal_entries_list_response import ExtrasJournalEntriesListResponse
    from .extras_object_changes_list_response import ExtrasObjectChangesListResponse
    from .extras_saved_filters_list_response import ExtrasSavedFiltersListResponse
    from .extras_tags_list_response import ExtrasTagsListResponse
    from .extras_webhooks_list_response import ExtrasWebhooksListResponse
_dynamic_imports: typing.Dict[str, str] = {
    "ExtrasConfigContextsListResponse": ".extras_config_contexts_list_response",
    "ExtrasContentTypesListResponse": ".extras_content_types_list_response",
    "ExtrasCustomFieldsListResponse": ".extras_custom_fields_list_response",
    "ExtrasCustomLinksListResponse": ".extras_custom_links_list_response",
    "ExtrasExportTemplatesListResponse": ".extras_export_templates_list_response",
    "ExtrasImageAttachmentsListResponse": ".extras_image_attachments_list_response",
    "ExtrasJobResultsListResponse": ".extras_job_results_list_response",
    "ExtrasJournalEntriesListResponse": ".extras_journal_entries_list_response",
    "ExtrasObjectChangesListResponse": ".extras_object_changes_list_response",
    "ExtrasSavedFiltersListResponse": ".extras_saved_filters_list_response",
    "ExtrasTagsListResponse": ".extras_tags_list_response",
    "ExtrasWebhooksListResponse": ".extras_webhooks_list_response",
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
    "ExtrasConfigContextsListResponse",
    "ExtrasContentTypesListResponse",
    "ExtrasCustomFieldsListResponse",
    "ExtrasCustomLinksListResponse",
    "ExtrasExportTemplatesListResponse",
    "ExtrasImageAttachmentsListResponse",
    "ExtrasJobResultsListResponse",
    "ExtrasJournalEntriesListResponse",
    "ExtrasObjectChangesListResponse",
    "ExtrasSavedFiltersListResponse",
    "ExtrasTagsListResponse",
    "ExtrasWebhooksListResponse",
]
