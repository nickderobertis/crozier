

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OrganizationsOrganizationsItem(UniversalBaseModel):
    number_of_agents_created: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numberOfAgentsCreated"),
        pydantic.Field(alias="numberOfAgentsCreated"),
    ] = None
    privileges: typing.Optional[typing.Dict[str, typing.Any]] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    monthly_number_of_agent_runs_created: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="monthlyNumberOfAgentRunsCreated"),
        pydantic.Field(alias="monthlyNumberOfAgentRunsCreated"),
    ] = None
    deployments_allowed: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="deploymentsAllowed"),
        pydantic.Field(alias="deploymentsAllowed"),
    ] = None
    monthly_number_of_hook_runs_created: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="monthlyNumberOfHookRunsCreated"),
        pydantic.Field(alias="monthlyNumberOfHookRunsCreated"),
    ] = None
    number_of_hooks_created: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="numberOfHooksCreated"), pydantic.Field(alias="numberOfHooksCreated")
    ] = None
    number_of_users_allowed: typing_extensions.Annotated[
        int, FieldMetadata(alias="numberOfUsersAllowed"), pydantic.Field(alias="numberOfUsersAllowed")
    ]
    monthly_number_of_predictions_allowed: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="monthlyNumberOfPredictionsAllowed"),
        pydantic.Field(alias="monthlyNumberOfPredictionsAllowed"),
    ]
    number_of_datasets_allowed: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numberOfDatasetsAllowed"),
        pydantic.Field(alias="numberOfDatasetsAllowed"),
    ] = None
    organization_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="organizationId"), pydantic.Field(alias="organizationId")
    ]
    number_of_models_created: typing_extensions.Annotated[
        int, FieldMetadata(alias="numberOfModelsCreated"), pydantic.Field(alias="numberOfModelsCreated")
    ]
    number_of_transitions_created: typing_extensions.Annotated[
        int, FieldMetadata(alias="numberOfTransitionsCreated"), pydantic.Field(alias="numberOfTransitionsCreated")
    ]
    monthly_number_of_documents_allowed: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="monthlyNumberOfDocumentsAllowed"),
        pydantic.Field(alias="monthlyNumberOfDocumentsAllowed"),
    ]
    number_of_actions_created: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numberOfActionsCreated"),
        pydantic.Field(alias="numberOfActionsCreated"),
    ] = None
    monthly_number_of_action_runs_allowed: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="monthlyNumberOfActionRunsAllowed"),
        pydantic.Field(alias="monthlyNumberOfActionRunsAllowed"),
    ] = None
    monthly_number_of_transformations_created: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="monthlyNumberOfTransformationsCreated"),
        pydantic.Field(alias="monthlyNumberOfTransformationsCreated"),
    ]
    created_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="createdTime"), pydantic.Field(alias="createdTime")
    ]
    plan_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="planId"), pydantic.Field(alias="planId")
    ] = None
    monthly_number_of_validation_tasks_created: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="monthlyNumberOfValidationTasksCreated"),
        pydantic.Field(alias="monthlyNumberOfValidationTasksCreated"),
    ] = None
    monthly_usage_summary: typing_extensions.Annotated[
        typing.Dict[str, typing.Any],
        FieldMetadata(alias="monthlyUsageSummary"),
        pydantic.Field(alias="monthlyUsageSummary"),
    ]
    updated_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedTime"), pydantic.Field(alias="updatedTime")
    ] = None
    monthly_number_of_page_predictions_allowed: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="monthlyNumberOfPagePredictionsAllowed"),
        pydantic.Field(alias="monthlyNumberOfPagePredictionsAllowed"),
    ] = None
    deployments_created: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="deploymentsCreated"),
        pydantic.Field(alias="deploymentsCreated"),
    ] = None
    monthly_number_of_gpu_hours_used: typing_extensions.Annotated[
        float, FieldMetadata(alias="monthlyNumberOfGpuHoursUsed"), pydantic.Field(alias="monthlyNumberOfGpuHoursUsed")
    ]
    updated_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedBy"), pydantic.Field(alias="updatedBy")
    ] = None
    number_of_agents_allowed: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numberOfAgentsAllowed"),
        pydantic.Field(alias="numberOfAgentsAllowed"),
    ] = None
    monthly_number_of_agent_runs_allowed: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="monthlyNumberOfAgentRunsAllowed"),
        pydantic.Field(alias="monthlyNumberOfAgentRunsAllowed"),
    ] = None
    monthly_number_of_workflow_executions_allowed: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="monthlyNumberOfWorkflowExecutionsAllowed"),
        pydantic.Field(alias="monthlyNumberOfWorkflowExecutionsAllowed"),
    ]
    monthly_number_of_active_models_used: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="monthlyNumberOfActiveModelsUsed"),
        pydantic.Field(alias="monthlyNumberOfActiveModelsUsed"),
    ]
    picture_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="pictureUrl"), pydantic.Field(alias="pictureUrl")
    ] = None
    monthly_number_of_data_bundles_created: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="monthlyNumberOfDataBundlesCreated"),
        pydantic.Field(alias="monthlyNumberOfDataBundlesCreated"),
    ]
    number_of_users_created: typing_extensions.Annotated[
        int, FieldMetadata(alias="numberOfUsersCreated"), pydantic.Field(alias="numberOfUsersCreated")
    ]
    monthly_number_of_action_runs_created: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="monthlyNumberOfActionRunsCreated"),
        pydantic.Field(alias="monthlyNumberOfActionRunsCreated"),
    ] = None
    monthly_number_of_transition_executions_created: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="monthlyNumberOfTransitionExecutionsCreated"),
        pydantic.Field(alias="monthlyNumberOfTransitionExecutionsCreated"),
    ]
    number_of_actions_allowed: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numberOfActionsAllowed"),
        pydantic.Field(alias="numberOfActionsAllowed"),
    ] = None
    number_of_secrets_created: typing_extensions.Annotated[
        int, FieldMetadata(alias="numberOfSecretsCreated"), pydantic.Field(alias="numberOfSecretsCreated")
    ]
    number_of_validations_created: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numberOfValidationsCreated"),
        pydantic.Field(alias="numberOfValidationsCreated"),
    ] = None
    name: typing.Optional[str] = None
    monthly_number_of_transformations_allowed: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="monthlyNumberOfTransformationsAllowed"),
        pydantic.Field(alias="monthlyNumberOfTransformationsAllowed"),
    ]
    monthly_number_of_production_workflow_minutes_used: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="monthlyNumberOfProductionWorkflowMinutesUsed"),
        pydantic.Field(alias="monthlyNumberOfProductionWorkflowMinutesUsed"),
    ] = None
    number_of_app_clients_allowed: typing_extensions.Annotated[
        int, FieldMetadata(alias="numberOfAppClientsAllowed"), pydantic.Field(alias="numberOfAppClientsAllowed")
    ]
    code: typing.Optional[str] = None
    number_of_workflows_created: typing_extensions.Annotated[
        int, FieldMetadata(alias="numberOfWorkflowsCreated"), pydantic.Field(alias="numberOfWorkflowsCreated")
    ]
    monthly_number_of_field_predictions_used: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="monthlyNumberOfFieldPredictionsUsed"),
        pydantic.Field(alias="monthlyNumberOfFieldPredictionsUsed"),
    ]
    monthly_number_of_workflow_executions_created: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="monthlyNumberOfWorkflowExecutionsCreated"),
        pydantic.Field(alias="monthlyNumberOfWorkflowExecutionsCreated"),
    ]
    description: typing.Optional[str] = None
    monthly_number_of_data_bundles_allowed: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="monthlyNumberOfDataBundlesAllowed"),
        pydantic.Field(alias="monthlyNumberOfDataBundlesAllowed"),
    ]
    monthly_number_of_transition_executions_allowed: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="monthlyNumberOfTransitionExecutionsAllowed"),
        pydantic.Field(alias="monthlyNumberOfTransitionExecutionsAllowed"),
    ]
    number_of_secrets_allowed: typing_extensions.Annotated[
        int, FieldMetadata(alias="numberOfSecretsAllowed"), pydantic.Field(alias="numberOfSecretsAllowed")
    ]
    monthly_number_of_trainings_created: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="monthlyNumberOfTrainingsCreated"),
        pydantic.Field(alias="monthlyNumberOfTrainingsCreated"),
    ]
    monthly_number_of_user_minutes_used: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="monthlyNumberOfUserMinutesUsed"),
        pydantic.Field(alias="monthlyNumberOfUserMinutesUsed"),
    ] = None
    number_of_validations_allowed: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numberOfValidationsAllowed"),
        pydantic.Field(alias="numberOfValidationsAllowed"),
    ] = None
    payment_method_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="paymentMethodId"), pydantic.Field(alias="paymentMethodId")
    ] = None
    monthly_number_of_model_deployment_units_used: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="monthlyNumberOfModelDeploymentUnitsUsed"),
        pydantic.Field(alias="monthlyNumberOfModelDeploymentUnitsUsed"),
    ] = None
    number_of_app_clients_created: typing_extensions.Annotated[
        int, FieldMetadata(alias="numberOfAppClientsCreated"), pydantic.Field(alias="numberOfAppClientsCreated")
    ]
    number_of_assets_created: typing_extensions.Annotated[
        int, FieldMetadata(alias="numberOfAssetsCreated"), pydantic.Field(alias="numberOfAssetsCreated")
    ]
    number_of_workflows_allowed: typing_extensions.Annotated[
        int, FieldMetadata(alias="numberOfWorkflowsAllowed"), pydantic.Field(alias="numberOfWorkflowsAllowed")
    ]
    client_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="clientId"), pydantic.Field(alias="clientId")
    ] = None
    document_retention_in_days: typing_extensions.Annotated[
        int, FieldMetadata(alias="documentRetentionInDays"), pydantic.Field(alias="documentRetentionInDays")
    ]
    number_of_connections_allowed: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numberOfConnectionsAllowed"),
        pydantic.Field(alias="numberOfConnectionsAllowed"),
    ] = None
    number_of_hooks_allowed: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="numberOfHooksAllowed"), pydantic.Field(alias="numberOfHooksAllowed")
    ] = None
    monthly_number_of_hook_runs_allowed: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="monthlyNumberOfHookRunsAllowed"),
        pydantic.Field(alias="monthlyNumberOfHookRunsAllowed"),
    ] = None
    monthly_number_of_predictions_created: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="monthlyNumberOfPredictionsCreated"),
        pydantic.Field(alias="monthlyNumberOfPredictionsCreated"),
    ]
    url: typing.Optional[str] = None
    number_of_datasets_created: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numberOfDatasetsCreated"),
        pydantic.Field(alias="numberOfDatasetsCreated"),
    ] = None
    monthly_number_of_page_predictions_used: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="monthlyNumberOfPagePredictionsUsed"),
        pydantic.Field(alias="monthlyNumberOfPagePredictionsUsed"),
    ] = None
    number_of_transitions_allowed: typing_extensions.Annotated[
        int, FieldMetadata(alias="numberOfTransitionsAllowed"), pydantic.Field(alias="numberOfTransitionsAllowed")
    ]
    monthly_number_of_documents_created: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="monthlyNumberOfDocumentsCreated"),
        pydantic.Field(alias="monthlyNumberOfDocumentsCreated"),
    ]
    number_of_connections_created: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numberOfConnectionsCreated"),
        pydantic.Field(alias="numberOfConnectionsCreated"),
    ] = None
    number_of_models_allowed: typing_extensions.Annotated[
        int, FieldMetadata(alias="numberOfModelsAllowed"), pydantic.Field(alias="numberOfModelsAllowed")
    ]
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    monthly_number_of_trainings_allowed: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="monthlyNumberOfTrainingsAllowed"),
        pydantic.Field(alias="monthlyNumberOfTrainingsAllowed"),
    ]
    monthly_number_of_field_predictions_allowed: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="monthlyNumberOfFieldPredictionsAllowed"),
        pydantic.Field(alias="monthlyNumberOfFieldPredictionsAllowed"),
    ]
    monthly_number_of_validation_tasks_allowed: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="monthlyNumberOfValidationTasksAllowed"),
        pydantic.Field(alias="monthlyNumberOfValidationTasksAllowed"),
    ] = None
    use_new_scopes: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="useNewScopes"), pydantic.Field(alias="useNewScopes")
    ] = None
    number_of_assets_allowed: typing_extensions.Annotated[
        int, FieldMetadata(alias="numberOfAssetsAllowed"), pydantic.Field(alias="numberOfAssetsAllowed")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
