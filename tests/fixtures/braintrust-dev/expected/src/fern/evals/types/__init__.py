



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .run_eval_data import RunEvalData
    from .run_eval_data_data import RunEvalDataData
    from .run_eval_data_dataset_id import RunEvalDataDatasetId
    from .run_eval_data_dataset_name import RunEvalDataDatasetName
    from .run_eval_mcp_auth_value import RunEvalMcpAuthValue
    from .run_eval_parent import RunEvalParent
    from .run_eval_parent_object_id import RunEvalParentObjectId
    from .run_eval_parent_object_id_object_type import RunEvalParentObjectIdObjectType
    from .run_eval_parent_object_id_row_ids import RunEvalParentObjectIdRowIds
    from .run_eval_repo_info import RunEvalRepoInfo
    from .run_eval_scores_item import RunEvalScoresItem
    from .run_eval_scores_item_code import RunEvalScoresItemCode
    from .run_eval_scores_item_code_function_type import RunEvalScoresItemCodeFunctionType
    from .run_eval_scores_item_code_inline_context import RunEvalScoresItemCodeInlineContext
    from .run_eval_scores_item_code_inline_context_runtime import RunEvalScoresItemCodeInlineContextRuntime
    from .run_eval_scores_item_function_id import RunEvalScoresItemFunctionId
    from .run_eval_scores_item_global_function import RunEvalScoresItemGlobalFunction
    from .run_eval_scores_item_inline_function import RunEvalScoresItemInlineFunction
    from .run_eval_scores_item_name import RunEvalScoresItemName
    from .run_eval_scores_item_project_name import RunEvalScoresItemProjectName
    from .run_eval_scores_item_prompt_session_function_id import RunEvalScoresItemPromptSessionFunctionId
_dynamic_imports: typing.Dict[str, str] = {
    "RunEvalData": ".run_eval_data",
    "RunEvalDataData": ".run_eval_data_data",
    "RunEvalDataDatasetId": ".run_eval_data_dataset_id",
    "RunEvalDataDatasetName": ".run_eval_data_dataset_name",
    "RunEvalMcpAuthValue": ".run_eval_mcp_auth_value",
    "RunEvalParent": ".run_eval_parent",
    "RunEvalParentObjectId": ".run_eval_parent_object_id",
    "RunEvalParentObjectIdObjectType": ".run_eval_parent_object_id_object_type",
    "RunEvalParentObjectIdRowIds": ".run_eval_parent_object_id_row_ids",
    "RunEvalRepoInfo": ".run_eval_repo_info",
    "RunEvalScoresItem": ".run_eval_scores_item",
    "RunEvalScoresItemCode": ".run_eval_scores_item_code",
    "RunEvalScoresItemCodeFunctionType": ".run_eval_scores_item_code_function_type",
    "RunEvalScoresItemCodeInlineContext": ".run_eval_scores_item_code_inline_context",
    "RunEvalScoresItemCodeInlineContextRuntime": ".run_eval_scores_item_code_inline_context_runtime",
    "RunEvalScoresItemFunctionId": ".run_eval_scores_item_function_id",
    "RunEvalScoresItemGlobalFunction": ".run_eval_scores_item_global_function",
    "RunEvalScoresItemInlineFunction": ".run_eval_scores_item_inline_function",
    "RunEvalScoresItemName": ".run_eval_scores_item_name",
    "RunEvalScoresItemProjectName": ".run_eval_scores_item_project_name",
    "RunEvalScoresItemPromptSessionFunctionId": ".run_eval_scores_item_prompt_session_function_id",
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
    "RunEvalData",
    "RunEvalDataData",
    "RunEvalDataDatasetId",
    "RunEvalDataDatasetName",
    "RunEvalMcpAuthValue",
    "RunEvalParent",
    "RunEvalParentObjectId",
    "RunEvalParentObjectIdObjectType",
    "RunEvalParentObjectIdRowIds",
    "RunEvalRepoInfo",
    "RunEvalScoresItem",
    "RunEvalScoresItemCode",
    "RunEvalScoresItemCodeFunctionType",
    "RunEvalScoresItemCodeInlineContext",
    "RunEvalScoresItemCodeInlineContextRuntime",
    "RunEvalScoresItemFunctionId",
    "RunEvalScoresItemGlobalFunction",
    "RunEvalScoresItemInlineFunction",
    "RunEvalScoresItemName",
    "RunEvalScoresItemProjectName",
    "RunEvalScoresItemPromptSessionFunctionId",
]
