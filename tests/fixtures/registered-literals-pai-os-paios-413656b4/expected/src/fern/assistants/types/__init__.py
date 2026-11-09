



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_assistant_request_model import CreateAssistantRequestModel
    from .create_assistant_request_model_one import CreateAssistantRequestModelOne
    from .create_assistant_request_tools_item import (
        CreateAssistantRequestToolsItem,
        CreateAssistantRequestToolsItem_CodeInterpreter,
        CreateAssistantRequestToolsItem_Function,
        CreateAssistantRequestToolsItem_Retrieval,
    )
    from .create_run_request_model import CreateRunRequestModel
    from .create_run_request_model_one import CreateRunRequestModelOne
    from .create_run_request_tools_item import (
        CreateRunRequestToolsItem,
        CreateRunRequestToolsItem_CodeInterpreter,
        CreateRunRequestToolsItem_Function,
        CreateRunRequestToolsItem_Retrieval,
    )
    from .create_thread_and_run_request_model import CreateThreadAndRunRequestModel
    from .create_thread_and_run_request_model_one import CreateThreadAndRunRequestModelOne
    from .create_thread_and_run_request_tools_item import (
        CreateThreadAndRunRequestToolsItem,
        CreateThreadAndRunRequestToolsItem_CodeInterpreter,
        CreateThreadAndRunRequestToolsItem_Function,
        CreateThreadAndRunRequestToolsItem_Retrieval,
    )
    from .list_assistant_files_request_order import ListAssistantFilesRequestOrder
    from .list_assistants_request_order import ListAssistantsRequestOrder
    from .list_message_files_request_order import ListMessageFilesRequestOrder
    from .list_messages_request_order import ListMessagesRequestOrder
    from .list_run_steps_request_order import ListRunStepsRequestOrder
    from .list_runs_request_order import ListRunsRequestOrder
    from .modify_assistant_request_tools_item import (
        ModifyAssistantRequestToolsItem,
        ModifyAssistantRequestToolsItem_CodeInterpreter,
        ModifyAssistantRequestToolsItem_Function,
        ModifyAssistantRequestToolsItem_Retrieval,
    )
    from .submit_tool_outputs_run_request_tool_outputs_item import SubmitToolOutputsRunRequestToolOutputsItem
_dynamic_imports: typing.Dict[str, str] = {
    "CreateAssistantRequestModel": ".create_assistant_request_model",
    "CreateAssistantRequestModelOne": ".create_assistant_request_model_one",
    "CreateAssistantRequestToolsItem": ".create_assistant_request_tools_item",
    "CreateAssistantRequestToolsItem_CodeInterpreter": ".create_assistant_request_tools_item",
    "CreateAssistantRequestToolsItem_Function": ".create_assistant_request_tools_item",
    "CreateAssistantRequestToolsItem_Retrieval": ".create_assistant_request_tools_item",
    "CreateRunRequestModel": ".create_run_request_model",
    "CreateRunRequestModelOne": ".create_run_request_model_one",
    "CreateRunRequestToolsItem": ".create_run_request_tools_item",
    "CreateRunRequestToolsItem_CodeInterpreter": ".create_run_request_tools_item",
    "CreateRunRequestToolsItem_Function": ".create_run_request_tools_item",
    "CreateRunRequestToolsItem_Retrieval": ".create_run_request_tools_item",
    "CreateThreadAndRunRequestModel": ".create_thread_and_run_request_model",
    "CreateThreadAndRunRequestModelOne": ".create_thread_and_run_request_model_one",
    "CreateThreadAndRunRequestToolsItem": ".create_thread_and_run_request_tools_item",
    "CreateThreadAndRunRequestToolsItem_CodeInterpreter": ".create_thread_and_run_request_tools_item",
    "CreateThreadAndRunRequestToolsItem_Function": ".create_thread_and_run_request_tools_item",
    "CreateThreadAndRunRequestToolsItem_Retrieval": ".create_thread_and_run_request_tools_item",
    "ListAssistantFilesRequestOrder": ".list_assistant_files_request_order",
    "ListAssistantsRequestOrder": ".list_assistants_request_order",
    "ListMessageFilesRequestOrder": ".list_message_files_request_order",
    "ListMessagesRequestOrder": ".list_messages_request_order",
    "ListRunStepsRequestOrder": ".list_run_steps_request_order",
    "ListRunsRequestOrder": ".list_runs_request_order",
    "ModifyAssistantRequestToolsItem": ".modify_assistant_request_tools_item",
    "ModifyAssistantRequestToolsItem_CodeInterpreter": ".modify_assistant_request_tools_item",
    "ModifyAssistantRequestToolsItem_Function": ".modify_assistant_request_tools_item",
    "ModifyAssistantRequestToolsItem_Retrieval": ".modify_assistant_request_tools_item",
    "SubmitToolOutputsRunRequestToolOutputsItem": ".submit_tool_outputs_run_request_tool_outputs_item",
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
