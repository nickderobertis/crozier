



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .action import Action
    from .action_run import ActionRun
    from .action_run_status import ActionRunStatus
    from .action_runs import ActionRuns
    from .action_runs_runs_item import ActionRunsRunsItem
    from .action_runs_runs_item_status import ActionRunsRunsItemStatus
    from .action_runs_status_item import ActionRunsStatusItem
    from .actions import Actions
    from .actions_actions_item import ActionsActionsItem
    from .agent import Agent
    from .agent_run import AgentRun
    from .agent_run_status import AgentRunStatus
    from .agent_runs import AgentRuns
    from .agent_runs_runs_item import AgentRunsRunsItem
    from .agent_runs_runs_item_status import AgentRunsRunsItemStatus
    from .agent_statistics import AgentStatistics
    from .agents import Agents
    from .agents_agents_item import AgentsAgentsItem
    from .document import Document
    from .document_content_type import DocumentContentType
    from .document_ground_truth_item import DocumentGroundTruthItem
    from .document_ground_truth_item_raw_value import DocumentGroundTruthItemRawValue
    from .document_ground_truth_item_value import DocumentGroundTruthItemValue
    from .documents import Documents
    from .documents_documents_item import DocumentsDocumentsItem
    from .documents_documents_item_content_type import DocumentsDocumentsItemContentType
    from .documents_documents_item_ground_truth_item import DocumentsDocumentsItemGroundTruthItem
    from .documents_documents_item_ground_truth_item_raw_value import DocumentsDocumentsItemGroundTruthItemRawValue
    from .documents_documents_item_ground_truth_item_value import DocumentsDocumentsItemGroundTruthItemValue
    from .documents_order import DocumentsOrder
    from .documents_sort_by import DocumentsSortBy
    from .error import Error
    from .function import Function
    from .function_runtime import FunctionRuntime
    from .functions import Functions
    from .functions_functions_item import FunctionsFunctionsItem
    from .functions_functions_item_runtime import FunctionsFunctionsItemRuntime
    from .ground_truth_list import GroundTruthList
    from .ground_truth_list_one_item_item import GroundTruthListOneItemItem
    from .ground_truth_list_one_item_item_raw_value import GroundTruthListOneItemItemRawValue
    from .ground_truth_list_one_item_item_value import GroundTruthListOneItemItemValue
    from .ground_truth_list_zero_item import GroundTruthListZeroItem
    from .ground_truth_list_zero_item_raw_value import GroundTruthListZeroItemRawValue
    from .ground_truth_list_zero_item_value import GroundTruthListZeroItemValue
    from .hook import Hook
    from .hook_run import HookRun
    from .hook_run_status import HookRunStatus
    from .hook_runs import HookRuns
    from .hook_runs_runs_item import HookRunsRunsItem
    from .hook_runs_runs_item_status import HookRunsRunsItemStatus
    from .hook_runs_status_item import HookRunsStatusItem
    from .hook_trigger import HookTrigger
    from .hooks import Hooks
    from .hooks_hooks_item import HooksHooksItem
    from .hooks_hooks_item_trigger import HooksHooksItemTrigger
    from .log import Log
    from .logs import Logs
    from .logs_logs_item import LogsLogsItem
    from .logs_order import LogsOrder
    from .model import Model
    from .model_confidence_version import ModelConfidenceVersion
    from .model_llm_version import ModelLlmVersion
    from .model_postprocess_config import (
        ModelPostprocessConfig,
        ModelPostprocessConfig_BestFirst,
        ModelPostprocessConfig_BestNPages,
    )
    from .model_postprocess_config_best_first import ModelPostprocessConfigBestFirst
    from .model_postprocess_config_best_first_output_format import ModelPostprocessConfigBestFirstOutputFormat
    from .model_postprocess_config_best_n_pages import ModelPostprocessConfigBestNPages
    from .model_postprocess_config_best_n_pages_output_format import ModelPostprocessConfigBestNPagesOutputFormat
    from .model_postprocess_config_best_n_pages_parameters import ModelPostprocessConfigBestNPagesParameters
    from .model_preprocess_config import ModelPreprocessConfig
    from .model_preprocess_config_image_quality import ModelPreprocessConfigImageQuality
    from .model_status import ModelStatus
    from .models import Models
    from .models_models_item import ModelsModelsItem
    from .models_models_item_confidence_version import ModelsModelsItemConfidenceVersion
    from .models_models_item_llm_version import ModelsModelsItemLlmVersion
    from .models_models_item_postprocess_config import (
        ModelsModelsItemPostprocessConfig,
        ModelsModelsItemPostprocessConfig_BestFirst,
        ModelsModelsItemPostprocessConfig_BestNPages,
    )
    from .models_models_item_postprocess_config_best_first import ModelsModelsItemPostprocessConfigBestFirst
    from .models_models_item_postprocess_config_best_first_output_format import (
        ModelsModelsItemPostprocessConfigBestFirstOutputFormat,
    )
    from .models_models_item_postprocess_config_best_n_pages import ModelsModelsItemPostprocessConfigBestNPages
    from .models_models_item_postprocess_config_best_n_pages_output_format import (
        ModelsModelsItemPostprocessConfigBestNPagesOutputFormat,
    )
    from .models_models_item_postprocess_config_best_n_pages_parameters import (
        ModelsModelsItemPostprocessConfigBestNPagesParameters,
    )
    from .models_models_item_preprocess_config import ModelsModelsItemPreprocessConfig
    from .models_models_item_preprocess_config_image_quality import ModelsModelsItemPreprocessConfigImageQuality
    from .models_models_item_status import ModelsModelsItemStatus
    from .oauth_scope import OauthScope
    from .organization import Organization
    from .organizations import Organizations
    from .organizations_organizations_item import OrganizationsOrganizationsItem
    from .patch_action_run_id_status import PatchActionRunIdStatus
    from .patch_agent_run_id_status import PatchAgentRunIdStatus
    from .patch_document_id_ground_truth_item import PatchDocumentIdGroundTruthItem
    from .patch_document_id_ground_truth_item_raw_value import PatchDocumentIdGroundTruthItemRawValue
    from .patch_document_id_ground_truth_item_value import PatchDocumentIdGroundTruthItemValue
    from .patch_hook_id_trigger import PatchHookIdTrigger
    from .patch_hook_run_id_status import PatchHookRunIdStatus
    from .patch_model_id_confidence_version import PatchModelIdConfidenceVersion
    from .patch_model_id_llm_version import PatchModelIdLlmVersion
    from .patch_model_id_postprocess_config import (
        PatchModelIdPostprocessConfig,
        PatchModelIdPostprocessConfig_BestFirst,
        PatchModelIdPostprocessConfig_BestNPages,
    )
    from .patch_model_id_postprocess_config_best_first import PatchModelIdPostprocessConfigBestFirst
    from .patch_model_id_postprocess_config_best_first_output_format import (
        PatchModelIdPostprocessConfigBestFirstOutputFormat,
    )
    from .patch_model_id_postprocess_config_best_n_pages import PatchModelIdPostprocessConfigBestNPages
    from .patch_model_id_postprocess_config_best_n_pages_output_format import (
        PatchModelIdPostprocessConfigBestNPagesOutputFormat,
    )
    from .patch_model_id_postprocess_config_best_n_pages_parameters import (
        PatchModelIdPostprocessConfigBestNPagesParameters,
    )
    from .patch_model_id_preprocess_config import PatchModelIdPreprocessConfig
    from .patch_model_id_preprocess_config_image_quality import PatchModelIdPreprocessConfigImageQuality
    from .patch_role_id_permissions_item import PatchRoleIdPermissionsItem
    from .patch_role_id_permissions_item_action import PatchRoleIdPermissionsItemAction
    from .patch_role_id_permissions_item_effect import PatchRoleIdPermissionsItemEffect
    from .patch_validation_task_id_status import PatchValidationTaskIdStatus
    from .post_documents_content_type import PostDocumentsContentType
    from .post_documents_ground_truth_item import PostDocumentsGroundTruthItem
    from .post_documents_ground_truth_item_raw_value import PostDocumentsGroundTruthItemRawValue
    from .post_documents_ground_truth_item_value import PostDocumentsGroundTruthItemValue
    from .post_functions_runtime import PostFunctionsRuntime
    from .post_hooks_trigger import PostHooksTrigger
    from .post_models_confidence_version import PostModelsConfidenceVersion
    from .post_models_llm_version import PostModelsLlmVersion
    from .post_models_postprocess_config import (
        PostModelsPostprocessConfig,
        PostModelsPostprocessConfig_BestFirst,
        PostModelsPostprocessConfig_BestNPages,
    )
    from .post_models_postprocess_config_best_first import PostModelsPostprocessConfigBestFirst
    from .post_models_postprocess_config_best_first_output_format import (
        PostModelsPostprocessConfigBestFirstOutputFormat,
    )
    from .post_models_postprocess_config_best_n_pages import PostModelsPostprocessConfigBestNPages
    from .post_models_postprocess_config_best_n_pages_output_format import (
        PostModelsPostprocessConfigBestNPagesOutputFormat,
    )
    from .post_models_postprocess_config_best_n_pages_parameters import PostModelsPostprocessConfigBestNPagesParameters
    from .post_models_preprocess_config import PostModelsPreprocessConfig
    from .post_models_preprocess_config_image_quality import PostModelsPreprocessConfigImageQuality
    from .post_predictions_image_quality import PostPredictionsImageQuality
    from .post_predictions_postprocess_config import (
        PostPredictionsPostprocessConfig,
        PostPredictionsPostprocessConfig_BestFirst,
        PostPredictionsPostprocessConfig_BestNPages,
    )
    from .post_predictions_postprocess_config_best_first import PostPredictionsPostprocessConfigBestFirst
    from .post_predictions_postprocess_config_best_first_output_format import (
        PostPredictionsPostprocessConfigBestFirstOutputFormat,
    )
    from .post_predictions_postprocess_config_best_n_pages import PostPredictionsPostprocessConfigBestNPages
    from .post_predictions_postprocess_config_best_n_pages_output_format import (
        PostPredictionsPostprocessConfigBestNPagesOutputFormat,
    )
    from .post_predictions_postprocess_config_best_n_pages_parameters import (
        PostPredictionsPostprocessConfigBestNPagesParameters,
    )
    from .post_predictions_preprocess_config import PostPredictionsPreprocessConfig
    from .post_predictions_preprocess_config_image_quality import PostPredictionsPreprocessConfigImageQuality
    from .post_roles_permissions_item import PostRolesPermissionsItem
    from .post_roles_permissions_item_action import PostRolesPermissionsItemAction
    from .post_roles_permissions_item_effect import PostRolesPermissionsItemEffect
    from .prediction import Prediction
    from .prediction_postprocess_config import (
        PredictionPostprocessConfig,
        PredictionPostprocessConfig_BestFirst,
        PredictionPostprocessConfig_BestNPages,
    )
    from .prediction_postprocess_config_best_first import PredictionPostprocessConfigBestFirst
    from .prediction_postprocess_config_best_first_output_format import PredictionPostprocessConfigBestFirstOutputFormat
    from .prediction_postprocess_config_best_n_pages import PredictionPostprocessConfigBestNPages
    from .prediction_postprocess_config_best_n_pages_output_format import (
        PredictionPostprocessConfigBestNPagesOutputFormat,
    )
    from .prediction_postprocess_config_best_n_pages_parameters import PredictionPostprocessConfigBestNPagesParameters
    from .prediction_predictions import PredictionPredictions
    from .prediction_predictions_zero_item import PredictionPredictionsZeroItem
    from .prediction_predictions_zero_item_attention_map import PredictionPredictionsZeroItemAttentionMap
    from .prediction_predictions_zero_item_attention_map_source import PredictionPredictionsZeroItemAttentionMapSource
    from .prediction_predictions_zero_item_one import PredictionPredictionsZeroItemOne
    from .prediction_predictions_zero_item_one_value_item_item import PredictionPredictionsZeroItemOneValueItemItem
    from .prediction_predictions_zero_item_one_value_item_item_source import (
        PredictionPredictionsZeroItemOneValueItemItemSource,
    )
    from .prediction_preprocess_config import PredictionPreprocessConfig
    from .prediction_preprocess_config_image_quality import PredictionPreprocessConfigImageQuality
    from .prediction_status import PredictionStatus
    from .predictions import Predictions
    from .predictions_order import PredictionsOrder
    from .predictions_predictions_item import PredictionsPredictionsItem
    from .predictions_predictions_item_postprocess_config import (
        PredictionsPredictionsItemPostprocessConfig,
        PredictionsPredictionsItemPostprocessConfig_BestFirst,
        PredictionsPredictionsItemPostprocessConfig_BestNPages,
    )
    from .predictions_predictions_item_postprocess_config_best_first import (
        PredictionsPredictionsItemPostprocessConfigBestFirst,
    )
    from .predictions_predictions_item_postprocess_config_best_first_output_format import (
        PredictionsPredictionsItemPostprocessConfigBestFirstOutputFormat,
    )
    from .predictions_predictions_item_postprocess_config_best_n_pages import (
        PredictionsPredictionsItemPostprocessConfigBestNPages,
    )
    from .predictions_predictions_item_postprocess_config_best_n_pages_output_format import (
        PredictionsPredictionsItemPostprocessConfigBestNPagesOutputFormat,
    )
    from .predictions_predictions_item_postprocess_config_best_n_pages_parameters import (
        PredictionsPredictionsItemPostprocessConfigBestNPagesParameters,
    )
    from .predictions_predictions_item_predictions import PredictionsPredictionsItemPredictions
    from .predictions_predictions_item_predictions_zero_item import PredictionsPredictionsItemPredictionsZeroItem
    from .predictions_predictions_item_predictions_zero_item_attention_map import (
        PredictionsPredictionsItemPredictionsZeroItemAttentionMap,
    )
    from .predictions_predictions_item_predictions_zero_item_attention_map_source import (
        PredictionsPredictionsItemPredictionsZeroItemAttentionMapSource,
    )
    from .predictions_predictions_item_predictions_zero_item_one import PredictionsPredictionsItemPredictionsZeroItemOne
    from .predictions_predictions_item_predictions_zero_item_one_value_item_item import (
        PredictionsPredictionsItemPredictionsZeroItemOneValueItemItem,
    )
    from .predictions_predictions_item_predictions_zero_item_one_value_item_item_source import (
        PredictionsPredictionsItemPredictionsZeroItemOneValueItemItemSource,
    )
    from .predictions_predictions_item_preprocess_config import PredictionsPredictionsItemPreprocessConfig
    from .predictions_predictions_item_preprocess_config_image_quality import (
        PredictionsPredictionsItemPreprocessConfigImageQuality,
    )
    from .predictions_predictions_item_status import PredictionsPredictionsItemStatus
    from .predictions_sort_by import PredictionsSortBy
    from .role import Role
    from .role_permissions_item import RolePermissionsItem
    from .role_permissions_item_action import RolePermissionsItemAction
    from .role_permissions_item_effect import RolePermissionsItemEffect
    from .roles import Roles
    from .roles_roles_item import RolesRolesItem
    from .roles_roles_item_permissions_item import RolesRolesItemPermissionsItem
    from .roles_roles_item_permissions_item_action import RolesRolesItemPermissionsItemAction
    from .roles_roles_item_permissions_item_effect import RolesRolesItemPermissionsItemEffect
    from .user import User
    from .user_status import UserStatus
    from .users import Users
    from .users_users_item import UsersUsersItem
    from .users_users_item_status import UsersUsersItemStatus
    from .validation import Validation
    from .validation_task import ValidationTask
    from .validation_task_status import ValidationTaskStatus
    from .validation_tasks import ValidationTasks
    from .validation_tasks_status_item import ValidationTasksStatusItem
    from .validation_tasks_tasks_item import ValidationTasksTasksItem
    from .validation_tasks_tasks_item_status import ValidationTasksTasksItemStatus
    from .validations import Validations
    from .validations_validations_item import ValidationsValidationsItem
_dynamic_imports: typing.Dict[str, str] = {
    "Action": ".action",
    "ActionRun": ".action_run",
    "ActionRunStatus": ".action_run_status",
    "ActionRuns": ".action_runs",
    "ActionRunsRunsItem": ".action_runs_runs_item",
    "ActionRunsRunsItemStatus": ".action_runs_runs_item_status",
    "ActionRunsStatusItem": ".action_runs_status_item",
    "Actions": ".actions",
    "ActionsActionsItem": ".actions_actions_item",
    "Agent": ".agent",
    "AgentRun": ".agent_run",
    "AgentRunStatus": ".agent_run_status",
    "AgentRuns": ".agent_runs",
    "AgentRunsRunsItem": ".agent_runs_runs_item",
    "AgentRunsRunsItemStatus": ".agent_runs_runs_item_status",
    "AgentStatistics": ".agent_statistics",
    "Agents": ".agents",
    "AgentsAgentsItem": ".agents_agents_item",
    "Document": ".document",
    "DocumentContentType": ".document_content_type",
    "DocumentGroundTruthItem": ".document_ground_truth_item",
    "DocumentGroundTruthItemRawValue": ".document_ground_truth_item_raw_value",
    "DocumentGroundTruthItemValue": ".document_ground_truth_item_value",
    "Documents": ".documents",
    "DocumentsDocumentsItem": ".documents_documents_item",
    "DocumentsDocumentsItemContentType": ".documents_documents_item_content_type",
    "DocumentsDocumentsItemGroundTruthItem": ".documents_documents_item_ground_truth_item",
    "DocumentsDocumentsItemGroundTruthItemRawValue": ".documents_documents_item_ground_truth_item_raw_value",
    "DocumentsDocumentsItemGroundTruthItemValue": ".documents_documents_item_ground_truth_item_value",
    "DocumentsOrder": ".documents_order",
    "DocumentsSortBy": ".documents_sort_by",
    "Error": ".error",
    "Function": ".function",
    "FunctionRuntime": ".function_runtime",
    "Functions": ".functions",
    "FunctionsFunctionsItem": ".functions_functions_item",
    "FunctionsFunctionsItemRuntime": ".functions_functions_item_runtime",
    "GroundTruthList": ".ground_truth_list",
    "GroundTruthListOneItemItem": ".ground_truth_list_one_item_item",
    "GroundTruthListOneItemItemRawValue": ".ground_truth_list_one_item_item_raw_value",
    "GroundTruthListOneItemItemValue": ".ground_truth_list_one_item_item_value",
    "GroundTruthListZeroItem": ".ground_truth_list_zero_item",
    "GroundTruthListZeroItemRawValue": ".ground_truth_list_zero_item_raw_value",
    "GroundTruthListZeroItemValue": ".ground_truth_list_zero_item_value",
    "Hook": ".hook",
    "HookRun": ".hook_run",
    "HookRunStatus": ".hook_run_status",
    "HookRuns": ".hook_runs",
    "HookRunsRunsItem": ".hook_runs_runs_item",
    "HookRunsRunsItemStatus": ".hook_runs_runs_item_status",
    "HookRunsStatusItem": ".hook_runs_status_item",
    "HookTrigger": ".hook_trigger",
    "Hooks": ".hooks",
    "HooksHooksItem": ".hooks_hooks_item",
    "HooksHooksItemTrigger": ".hooks_hooks_item_trigger",
    "Log": ".log",
    "Logs": ".logs",
    "LogsLogsItem": ".logs_logs_item",
    "LogsOrder": ".logs_order",
    "Model": ".model",
    "ModelConfidenceVersion": ".model_confidence_version",
    "ModelLlmVersion": ".model_llm_version",
    "ModelPostprocessConfig": ".model_postprocess_config",
    "ModelPostprocessConfigBestFirst": ".model_postprocess_config_best_first",
    "ModelPostprocessConfigBestFirstOutputFormat": ".model_postprocess_config_best_first_output_format",
    "ModelPostprocessConfigBestNPages": ".model_postprocess_config_best_n_pages",
    "ModelPostprocessConfigBestNPagesOutputFormat": ".model_postprocess_config_best_n_pages_output_format",
    "ModelPostprocessConfigBestNPagesParameters": ".model_postprocess_config_best_n_pages_parameters",
    "ModelPostprocessConfig_BestFirst": ".model_postprocess_config",
    "ModelPostprocessConfig_BestNPages": ".model_postprocess_config",
    "ModelPreprocessConfig": ".model_preprocess_config",
    "ModelPreprocessConfigImageQuality": ".model_preprocess_config_image_quality",
    "ModelStatus": ".model_status",
    "Models": ".models",
    "ModelsModelsItem": ".models_models_item",
    "ModelsModelsItemConfidenceVersion": ".models_models_item_confidence_version",
    "ModelsModelsItemLlmVersion": ".models_models_item_llm_version",
    "ModelsModelsItemPostprocessConfig": ".models_models_item_postprocess_config",
    "ModelsModelsItemPostprocessConfigBestFirst": ".models_models_item_postprocess_config_best_first",
    "ModelsModelsItemPostprocessConfigBestFirstOutputFormat": ".models_models_item_postprocess_config_best_first_output_format",
    "ModelsModelsItemPostprocessConfigBestNPages": ".models_models_item_postprocess_config_best_n_pages",
    "ModelsModelsItemPostprocessConfigBestNPagesOutputFormat": ".models_models_item_postprocess_config_best_n_pages_output_format",
    "ModelsModelsItemPostprocessConfigBestNPagesParameters": ".models_models_item_postprocess_config_best_n_pages_parameters",
    "ModelsModelsItemPostprocessConfig_BestFirst": ".models_models_item_postprocess_config",
    "ModelsModelsItemPostprocessConfig_BestNPages": ".models_models_item_postprocess_config",
    "ModelsModelsItemPreprocessConfig": ".models_models_item_preprocess_config",
    "ModelsModelsItemPreprocessConfigImageQuality": ".models_models_item_preprocess_config_image_quality",
    "ModelsModelsItemStatus": ".models_models_item_status",
    "OauthScope": ".oauth_scope",
    "Organization": ".organization",
    "Organizations": ".organizations",
    "OrganizationsOrganizationsItem": ".organizations_organizations_item",
    "PatchActionRunIdStatus": ".patch_action_run_id_status",
    "PatchAgentRunIdStatus": ".patch_agent_run_id_status",
    "PatchDocumentIdGroundTruthItem": ".patch_document_id_ground_truth_item",
    "PatchDocumentIdGroundTruthItemRawValue": ".patch_document_id_ground_truth_item_raw_value",
    "PatchDocumentIdGroundTruthItemValue": ".patch_document_id_ground_truth_item_value",
    "PatchHookIdTrigger": ".patch_hook_id_trigger",
    "PatchHookRunIdStatus": ".patch_hook_run_id_status",
    "PatchModelIdConfidenceVersion": ".patch_model_id_confidence_version",
    "PatchModelIdLlmVersion": ".patch_model_id_llm_version",
    "PatchModelIdPostprocessConfig": ".patch_model_id_postprocess_config",
    "PatchModelIdPostprocessConfigBestFirst": ".patch_model_id_postprocess_config_best_first",
    "PatchModelIdPostprocessConfigBestFirstOutputFormat": ".patch_model_id_postprocess_config_best_first_output_format",
    "PatchModelIdPostprocessConfigBestNPages": ".patch_model_id_postprocess_config_best_n_pages",
    "PatchModelIdPostprocessConfigBestNPagesOutputFormat": ".patch_model_id_postprocess_config_best_n_pages_output_format",
    "PatchModelIdPostprocessConfigBestNPagesParameters": ".patch_model_id_postprocess_config_best_n_pages_parameters",
    "PatchModelIdPostprocessConfig_BestFirst": ".patch_model_id_postprocess_config",
    "PatchModelIdPostprocessConfig_BestNPages": ".patch_model_id_postprocess_config",
    "PatchModelIdPreprocessConfig": ".patch_model_id_preprocess_config",
    "PatchModelIdPreprocessConfigImageQuality": ".patch_model_id_preprocess_config_image_quality",
    "PatchRoleIdPermissionsItem": ".patch_role_id_permissions_item",
    "PatchRoleIdPermissionsItemAction": ".patch_role_id_permissions_item_action",
    "PatchRoleIdPermissionsItemEffect": ".patch_role_id_permissions_item_effect",
    "PatchValidationTaskIdStatus": ".patch_validation_task_id_status",
    "PostDocumentsContentType": ".post_documents_content_type",
    "PostDocumentsGroundTruthItem": ".post_documents_ground_truth_item",
    "PostDocumentsGroundTruthItemRawValue": ".post_documents_ground_truth_item_raw_value",
    "PostDocumentsGroundTruthItemValue": ".post_documents_ground_truth_item_value",
    "PostFunctionsRuntime": ".post_functions_runtime",
    "PostHooksTrigger": ".post_hooks_trigger",
    "PostModelsConfidenceVersion": ".post_models_confidence_version",
    "PostModelsLlmVersion": ".post_models_llm_version",
    "PostModelsPostprocessConfig": ".post_models_postprocess_config",
    "PostModelsPostprocessConfigBestFirst": ".post_models_postprocess_config_best_first",
    "PostModelsPostprocessConfigBestFirstOutputFormat": ".post_models_postprocess_config_best_first_output_format",
    "PostModelsPostprocessConfigBestNPages": ".post_models_postprocess_config_best_n_pages",
    "PostModelsPostprocessConfigBestNPagesOutputFormat": ".post_models_postprocess_config_best_n_pages_output_format",
    "PostModelsPostprocessConfigBestNPagesParameters": ".post_models_postprocess_config_best_n_pages_parameters",
    "PostModelsPostprocessConfig_BestFirst": ".post_models_postprocess_config",
    "PostModelsPostprocessConfig_BestNPages": ".post_models_postprocess_config",
    "PostModelsPreprocessConfig": ".post_models_preprocess_config",
    "PostModelsPreprocessConfigImageQuality": ".post_models_preprocess_config_image_quality",
    "PostPredictionsImageQuality": ".post_predictions_image_quality",
    "PostPredictionsPostprocessConfig": ".post_predictions_postprocess_config",
    "PostPredictionsPostprocessConfigBestFirst": ".post_predictions_postprocess_config_best_first",
    "PostPredictionsPostprocessConfigBestFirstOutputFormat": ".post_predictions_postprocess_config_best_first_output_format",
    "PostPredictionsPostprocessConfigBestNPages": ".post_predictions_postprocess_config_best_n_pages",
    "PostPredictionsPostprocessConfigBestNPagesOutputFormat": ".post_predictions_postprocess_config_best_n_pages_output_format",
    "PostPredictionsPostprocessConfigBestNPagesParameters": ".post_predictions_postprocess_config_best_n_pages_parameters",
    "PostPredictionsPostprocessConfig_BestFirst": ".post_predictions_postprocess_config",
    "PostPredictionsPostprocessConfig_BestNPages": ".post_predictions_postprocess_config",
    "PostPredictionsPreprocessConfig": ".post_predictions_preprocess_config",
    "PostPredictionsPreprocessConfigImageQuality": ".post_predictions_preprocess_config_image_quality",
    "PostRolesPermissionsItem": ".post_roles_permissions_item",
    "PostRolesPermissionsItemAction": ".post_roles_permissions_item_action",
    "PostRolesPermissionsItemEffect": ".post_roles_permissions_item_effect",
    "Prediction": ".prediction",
    "PredictionPostprocessConfig": ".prediction_postprocess_config",
    "PredictionPostprocessConfigBestFirst": ".prediction_postprocess_config_best_first",
    "PredictionPostprocessConfigBestFirstOutputFormat": ".prediction_postprocess_config_best_first_output_format",
    "PredictionPostprocessConfigBestNPages": ".prediction_postprocess_config_best_n_pages",
    "PredictionPostprocessConfigBestNPagesOutputFormat": ".prediction_postprocess_config_best_n_pages_output_format",
    "PredictionPostprocessConfigBestNPagesParameters": ".prediction_postprocess_config_best_n_pages_parameters",
    "PredictionPostprocessConfig_BestFirst": ".prediction_postprocess_config",
    "PredictionPostprocessConfig_BestNPages": ".prediction_postprocess_config",
    "PredictionPredictions": ".prediction_predictions",
    "PredictionPredictionsZeroItem": ".prediction_predictions_zero_item",
    "PredictionPredictionsZeroItemAttentionMap": ".prediction_predictions_zero_item_attention_map",
    "PredictionPredictionsZeroItemAttentionMapSource": ".prediction_predictions_zero_item_attention_map_source",
    "PredictionPredictionsZeroItemOne": ".prediction_predictions_zero_item_one",
    "PredictionPredictionsZeroItemOneValueItemItem": ".prediction_predictions_zero_item_one_value_item_item",
    "PredictionPredictionsZeroItemOneValueItemItemSource": ".prediction_predictions_zero_item_one_value_item_item_source",
    "PredictionPreprocessConfig": ".prediction_preprocess_config",
    "PredictionPreprocessConfigImageQuality": ".prediction_preprocess_config_image_quality",
    "PredictionStatus": ".prediction_status",
    "Predictions": ".predictions",
    "PredictionsOrder": ".predictions_order",
    "PredictionsPredictionsItem": ".predictions_predictions_item",
    "PredictionsPredictionsItemPostprocessConfig": ".predictions_predictions_item_postprocess_config",
    "PredictionsPredictionsItemPostprocessConfigBestFirst": ".predictions_predictions_item_postprocess_config_best_first",
    "PredictionsPredictionsItemPostprocessConfigBestFirstOutputFormat": ".predictions_predictions_item_postprocess_config_best_first_output_format",
    "PredictionsPredictionsItemPostprocessConfigBestNPages": ".predictions_predictions_item_postprocess_config_best_n_pages",
    "PredictionsPredictionsItemPostprocessConfigBestNPagesOutputFormat": ".predictions_predictions_item_postprocess_config_best_n_pages_output_format",
    "PredictionsPredictionsItemPostprocessConfigBestNPagesParameters": ".predictions_predictions_item_postprocess_config_best_n_pages_parameters",
    "PredictionsPredictionsItemPostprocessConfig_BestFirst": ".predictions_predictions_item_postprocess_config",
    "PredictionsPredictionsItemPostprocessConfig_BestNPages": ".predictions_predictions_item_postprocess_config",
    "PredictionsPredictionsItemPredictions": ".predictions_predictions_item_predictions",
    "PredictionsPredictionsItemPredictionsZeroItem": ".predictions_predictions_item_predictions_zero_item",
    "PredictionsPredictionsItemPredictionsZeroItemAttentionMap": ".predictions_predictions_item_predictions_zero_item_attention_map",
    "PredictionsPredictionsItemPredictionsZeroItemAttentionMapSource": ".predictions_predictions_item_predictions_zero_item_attention_map_source",
    "PredictionsPredictionsItemPredictionsZeroItemOne": ".predictions_predictions_item_predictions_zero_item_one",
    "PredictionsPredictionsItemPredictionsZeroItemOneValueItemItem": ".predictions_predictions_item_predictions_zero_item_one_value_item_item",
    "PredictionsPredictionsItemPredictionsZeroItemOneValueItemItemSource": ".predictions_predictions_item_predictions_zero_item_one_value_item_item_source",
    "PredictionsPredictionsItemPreprocessConfig": ".predictions_predictions_item_preprocess_config",
    "PredictionsPredictionsItemPreprocessConfigImageQuality": ".predictions_predictions_item_preprocess_config_image_quality",
    "PredictionsPredictionsItemStatus": ".predictions_predictions_item_status",
    "PredictionsSortBy": ".predictions_sort_by",
    "Role": ".role",
    "RolePermissionsItem": ".role_permissions_item",
    "RolePermissionsItemAction": ".role_permissions_item_action",
    "RolePermissionsItemEffect": ".role_permissions_item_effect",
    "Roles": ".roles",
    "RolesRolesItem": ".roles_roles_item",
    "RolesRolesItemPermissionsItem": ".roles_roles_item_permissions_item",
    "RolesRolesItemPermissionsItemAction": ".roles_roles_item_permissions_item_action",
    "RolesRolesItemPermissionsItemEffect": ".roles_roles_item_permissions_item_effect",
    "User": ".user",
    "UserStatus": ".user_status",
    "Users": ".users",
    "UsersUsersItem": ".users_users_item",
    "UsersUsersItemStatus": ".users_users_item_status",
    "Validation": ".validation",
    "ValidationTask": ".validation_task",
    "ValidationTaskStatus": ".validation_task_status",
    "ValidationTasks": ".validation_tasks",
    "ValidationTasksStatusItem": ".validation_tasks_status_item",
    "ValidationTasksTasksItem": ".validation_tasks_tasks_item",
    "ValidationTasksTasksItemStatus": ".validation_tasks_tasks_item_status",
    "Validations": ".validations",
    "ValidationsValidationsItem": ".validations_validations_item",
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
    "Action",
    "ActionRun",
    "ActionRunStatus",
    "ActionRuns",
    "ActionRunsRunsItem",
    "ActionRunsRunsItemStatus",
    "ActionRunsStatusItem",
    "Actions",
    "ActionsActionsItem",
    "Agent",
    "AgentRun",
    "AgentRunStatus",
    "AgentRuns",
    "AgentRunsRunsItem",
    "AgentRunsRunsItemStatus",
    "AgentStatistics",
    "Agents",
    "AgentsAgentsItem",
    "Document",
    "DocumentContentType",
    "DocumentGroundTruthItem",
    "DocumentGroundTruthItemRawValue",
    "DocumentGroundTruthItemValue",
    "Documents",
    "DocumentsDocumentsItem",
    "DocumentsDocumentsItemContentType",
    "DocumentsDocumentsItemGroundTruthItem",
    "DocumentsDocumentsItemGroundTruthItemRawValue",
    "DocumentsDocumentsItemGroundTruthItemValue",
    "DocumentsOrder",
    "DocumentsSortBy",
    "Error",
    "Function",
    "FunctionRuntime",
    "Functions",
    "FunctionsFunctionsItem",
    "FunctionsFunctionsItemRuntime",
    "GroundTruthList",
    "GroundTruthListOneItemItem",
    "GroundTruthListOneItemItemRawValue",
    "GroundTruthListOneItemItemValue",
    "GroundTruthListZeroItem",
    "GroundTruthListZeroItemRawValue",
    "GroundTruthListZeroItemValue",
    "Hook",
    "HookRun",
    "HookRunStatus",
    "HookRuns",
    "HookRunsRunsItem",
    "HookRunsRunsItemStatus",
    "HookRunsStatusItem",
    "HookTrigger",
    "Hooks",
    "HooksHooksItem",
    "HooksHooksItemTrigger",
    "Log",
    "Logs",
    "LogsLogsItem",
    "LogsOrder",
    "Model",
    "ModelConfidenceVersion",
    "ModelLlmVersion",
    "ModelPostprocessConfig",
    "ModelPostprocessConfigBestFirst",
    "ModelPostprocessConfigBestFirstOutputFormat",
    "ModelPostprocessConfigBestNPages",
    "ModelPostprocessConfigBestNPagesOutputFormat",
    "ModelPostprocessConfigBestNPagesParameters",
    "ModelPostprocessConfig_BestFirst",
    "ModelPostprocessConfig_BestNPages",
    "ModelPreprocessConfig",
    "ModelPreprocessConfigImageQuality",
    "ModelStatus",
    "Models",
    "ModelsModelsItem",
    "ModelsModelsItemConfidenceVersion",
    "ModelsModelsItemLlmVersion",
    "ModelsModelsItemPostprocessConfig",
    "ModelsModelsItemPostprocessConfigBestFirst",
    "ModelsModelsItemPostprocessConfigBestFirstOutputFormat",
    "ModelsModelsItemPostprocessConfigBestNPages",
    "ModelsModelsItemPostprocessConfigBestNPagesOutputFormat",
    "ModelsModelsItemPostprocessConfigBestNPagesParameters",
    "ModelsModelsItemPostprocessConfig_BestFirst",
    "ModelsModelsItemPostprocessConfig_BestNPages",
    "ModelsModelsItemPreprocessConfig",
    "ModelsModelsItemPreprocessConfigImageQuality",
    "ModelsModelsItemStatus",
    "OauthScope",
    "Organization",
    "Organizations",
    "OrganizationsOrganizationsItem",
    "PatchActionRunIdStatus",
    "PatchAgentRunIdStatus",
    "PatchDocumentIdGroundTruthItem",
    "PatchDocumentIdGroundTruthItemRawValue",
    "PatchDocumentIdGroundTruthItemValue",
    "PatchHookIdTrigger",
    "PatchHookRunIdStatus",
    "PatchModelIdConfidenceVersion",
    "PatchModelIdLlmVersion",
    "PatchModelIdPostprocessConfig",
    "PatchModelIdPostprocessConfigBestFirst",
    "PatchModelIdPostprocessConfigBestFirstOutputFormat",
    "PatchModelIdPostprocessConfigBestNPages",
    "PatchModelIdPostprocessConfigBestNPagesOutputFormat",
    "PatchModelIdPostprocessConfigBestNPagesParameters",
    "PatchModelIdPostprocessConfig_BestFirst",
    "PatchModelIdPostprocessConfig_BestNPages",
    "PatchModelIdPreprocessConfig",
    "PatchModelIdPreprocessConfigImageQuality",
    "PatchRoleIdPermissionsItem",
    "PatchRoleIdPermissionsItemAction",
    "PatchRoleIdPermissionsItemEffect",
    "PatchValidationTaskIdStatus",
    "PostDocumentsContentType",
    "PostDocumentsGroundTruthItem",
    "PostDocumentsGroundTruthItemRawValue",
    "PostDocumentsGroundTruthItemValue",
    "PostFunctionsRuntime",
    "PostHooksTrigger",
    "PostModelsConfidenceVersion",
    "PostModelsLlmVersion",
    "PostModelsPostprocessConfig",
    "PostModelsPostprocessConfigBestFirst",
    "PostModelsPostprocessConfigBestFirstOutputFormat",
    "PostModelsPostprocessConfigBestNPages",
    "PostModelsPostprocessConfigBestNPagesOutputFormat",
    "PostModelsPostprocessConfigBestNPagesParameters",
    "PostModelsPostprocessConfig_BestFirst",
    "PostModelsPostprocessConfig_BestNPages",
    "PostModelsPreprocessConfig",
    "PostModelsPreprocessConfigImageQuality",
    "PostPredictionsImageQuality",
    "PostPredictionsPostprocessConfig",
    "PostPredictionsPostprocessConfigBestFirst",
    "PostPredictionsPostprocessConfigBestFirstOutputFormat",
    "PostPredictionsPostprocessConfigBestNPages",
    "PostPredictionsPostprocessConfigBestNPagesOutputFormat",
    "PostPredictionsPostprocessConfigBestNPagesParameters",
    "PostPredictionsPostprocessConfig_BestFirst",
    "PostPredictionsPostprocessConfig_BestNPages",
    "PostPredictionsPreprocessConfig",
    "PostPredictionsPreprocessConfigImageQuality",
    "PostRolesPermissionsItem",
    "PostRolesPermissionsItemAction",
    "PostRolesPermissionsItemEffect",
    "Prediction",
    "PredictionPostprocessConfig",
    "PredictionPostprocessConfigBestFirst",
    "PredictionPostprocessConfigBestFirstOutputFormat",
    "PredictionPostprocessConfigBestNPages",
    "PredictionPostprocessConfigBestNPagesOutputFormat",
    "PredictionPostprocessConfigBestNPagesParameters",
    "PredictionPostprocessConfig_BestFirst",
    "PredictionPostprocessConfig_BestNPages",
    "PredictionPredictions",
    "PredictionPredictionsZeroItem",
    "PredictionPredictionsZeroItemAttentionMap",
    "PredictionPredictionsZeroItemAttentionMapSource",
    "PredictionPredictionsZeroItemOne",
    "PredictionPredictionsZeroItemOneValueItemItem",
    "PredictionPredictionsZeroItemOneValueItemItemSource",
    "PredictionPreprocessConfig",
    "PredictionPreprocessConfigImageQuality",
    "PredictionStatus",
    "Predictions",
    "PredictionsOrder",
    "PredictionsPredictionsItem",
    "PredictionsPredictionsItemPostprocessConfig",
    "PredictionsPredictionsItemPostprocessConfigBestFirst",
    "PredictionsPredictionsItemPostprocessConfigBestFirstOutputFormat",
    "PredictionsPredictionsItemPostprocessConfigBestNPages",
    "PredictionsPredictionsItemPostprocessConfigBestNPagesOutputFormat",
    "PredictionsPredictionsItemPostprocessConfigBestNPagesParameters",
    "PredictionsPredictionsItemPostprocessConfig_BestFirst",
    "PredictionsPredictionsItemPostprocessConfig_BestNPages",
    "PredictionsPredictionsItemPredictions",
    "PredictionsPredictionsItemPredictionsZeroItem",
    "PredictionsPredictionsItemPredictionsZeroItemAttentionMap",
    "PredictionsPredictionsItemPredictionsZeroItemAttentionMapSource",
    "PredictionsPredictionsItemPredictionsZeroItemOne",
    "PredictionsPredictionsItemPredictionsZeroItemOneValueItemItem",
    "PredictionsPredictionsItemPredictionsZeroItemOneValueItemItemSource",
    "PredictionsPredictionsItemPreprocessConfig",
    "PredictionsPredictionsItemPreprocessConfigImageQuality",
    "PredictionsPredictionsItemStatus",
    "PredictionsSortBy",
    "Role",
    "RolePermissionsItem",
    "RolePermissionsItemAction",
    "RolePermissionsItemEffect",
    "Roles",
    "RolesRolesItem",
    "RolesRolesItemPermissionsItem",
    "RolesRolesItemPermissionsItemAction",
    "RolesRolesItemPermissionsItemEffect",
    "User",
    "UserStatus",
    "Users",
    "UsersUsersItem",
    "UsersUsersItemStatus",
    "Validation",
    "ValidationTask",
    "ValidationTaskStatus",
    "ValidationTasks",
    "ValidationTasksStatusItem",
    "ValidationTasksTasksItem",
    "ValidationTasksTasksItemStatus",
    "Validations",
    "ValidationsValidationsItem",
]
