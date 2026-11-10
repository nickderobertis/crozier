



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CreateAssistantRequestModel,
        CreateAssistantRequestModelOne,
        CreateAssistantRequestToolsItem,
        CreateAssistantRequestToolsItem_CodeInterpreter,
        CreateAssistantRequestToolsItem_Function,
        CreateAssistantRequestToolsItem_Retrieval,
        CreateRunRequestModel,
        CreateRunRequestModelOne,
        CreateRunRequestToolsItem,
        CreateRunRequestToolsItem_CodeInterpreter,
        CreateRunRequestToolsItem_Function,
        CreateRunRequestToolsItem_Retrieval,
        CreateThreadAndRunRequestModel,
        CreateThreadAndRunRequestModelOne,
        CreateThreadAndRunRequestToolsItem,
        CreateThreadAndRunRequestToolsItem_CodeInterpreter,
        CreateThreadAndRunRequestToolsItem_Function,
        CreateThreadAndRunRequestToolsItem_Retrieval,
        ListAssistantFilesRequestOrder,
        ListAssistantsRequestOrder,
        ListMessageFilesRequestOrder,
        ListMessagesRequestOrder,
        ListRunStepsRequestOrder,
        ListRunsRequestOrder,
        ModifyAssistantRequestToolsItem,
        ModifyAssistantRequestToolsItem_CodeInterpreter,
        ModifyAssistantRequestToolsItem_Function,
        ModifyAssistantRequestToolsItem_Retrieval,
        SubmitToolOutputsRunRequestToolOutputsItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CreateAssistantRequestModel": ".types",
    "CreateAssistantRequestModelOne": ".types",
    "CreateAssistantRequestToolsItem": ".types",
    "CreateAssistantRequestToolsItem_CodeInterpreter": ".types",
    "CreateAssistantRequestToolsItem_Function": ".types",
    "CreateAssistantRequestToolsItem_Retrieval": ".types",
    "CreateRunRequestModel": ".types",
    "CreateRunRequestModelOne": ".types",
    "CreateRunRequestToolsItem": ".types",
    "CreateRunRequestToolsItem_CodeInterpreter": ".types",
    "CreateRunRequestToolsItem_Function": ".types",
    "CreateRunRequestToolsItem_Retrieval": ".types",
    "CreateThreadAndRunRequestModel": ".types",
    "CreateThreadAndRunRequestModelOne": ".types",
    "CreateThreadAndRunRequestToolsItem": ".types",
    "CreateThreadAndRunRequestToolsItem_CodeInterpreter": ".types",
    "CreateThreadAndRunRequestToolsItem_Function": ".types",
    "CreateThreadAndRunRequestToolsItem_Retrieval": ".types",
    "ListAssistantFilesRequestOrder": ".types",
    "ListAssistantsRequestOrder": ".types",
    "ListMessageFilesRequestOrder": ".types",
    "ListMessagesRequestOrder": ".types",
    "ListRunStepsRequestOrder": ".types",
    "ListRunsRequestOrder": ".types",
    "ModifyAssistantRequestToolsItem": ".types",
    "ModifyAssistantRequestToolsItem_CodeInterpreter": ".types",
    "ModifyAssistantRequestToolsItem_Function": ".types",
    "ModifyAssistantRequestToolsItem_Retrieval": ".types",
    "SubmitToolOutputsRunRequestToolOutputsItem": ".types",
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
    "CreateAssistantRequestModel",
    "CreateAssistantRequestModelOne",
    "CreateAssistantRequestToolsItem",
    "CreateAssistantRequestToolsItem_CodeInterpreter",
    "CreateAssistantRequestToolsItem_Function",
    "CreateAssistantRequestToolsItem_Retrieval",
    "CreateRunRequestModel",
    "CreateRunRequestModelOne",
    "CreateRunRequestToolsItem",
    "CreateRunRequestToolsItem_CodeInterpreter",
    "CreateRunRequestToolsItem_Function",
    "CreateRunRequestToolsItem_Retrieval",
    "CreateThreadAndRunRequestModel",
    "CreateThreadAndRunRequestModelOne",
    "CreateThreadAndRunRequestToolsItem",
    "CreateThreadAndRunRequestToolsItem_CodeInterpreter",
    "CreateThreadAndRunRequestToolsItem_Function",
    "CreateThreadAndRunRequestToolsItem_Retrieval",
    "ListAssistantFilesRequestOrder",
    "ListAssistantsRequestOrder",
    "ListMessageFilesRequestOrder",
    "ListMessagesRequestOrder",
    "ListRunStepsRequestOrder",
    "ListRunsRequestOrder",
    "ModifyAssistantRequestToolsItem",
    "ModifyAssistantRequestToolsItem_CodeInterpreter",
    "ModifyAssistantRequestToolsItem_Function",
    "ModifyAssistantRequestToolsItem_Retrieval",
    "SubmitToolOutputsRunRequestToolOutputsItem",
]
