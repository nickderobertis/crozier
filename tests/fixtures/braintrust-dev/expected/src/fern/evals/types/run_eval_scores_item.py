

import typing

from .run_eval_scores_item_code import RunEvalScoresItemCode
from .run_eval_scores_item_function_id import RunEvalScoresItemFunctionId
from .run_eval_scores_item_global_function import RunEvalScoresItemGlobalFunction
from .run_eval_scores_item_inline_function import RunEvalScoresItemInlineFunction
from .run_eval_scores_item_name import RunEvalScoresItemName
from .run_eval_scores_item_project_name import RunEvalScoresItemProjectName
from .run_eval_scores_item_prompt_session_function_id import RunEvalScoresItemPromptSessionFunctionId

RunEvalScoresItem = typing.Union[
    RunEvalScoresItemFunctionId,
    RunEvalScoresItemProjectName,
    RunEvalScoresItemGlobalFunction,
    RunEvalScoresItemPromptSessionFunctionId,
    RunEvalScoresItemCode,
    RunEvalScoresItemInlineFunction,
    RunEvalScoresItemName,
]
