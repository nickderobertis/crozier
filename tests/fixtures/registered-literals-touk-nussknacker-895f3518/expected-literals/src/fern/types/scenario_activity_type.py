

import typing

ScenarioActivityType = typing.Union[
    typing.Literal[
        "SCENARIO_CREATED",
        "SCENARIO_ARCHIVED",
        "SCENARIO_UNARCHIVED",
        "SCENARIO_DEPLOYED",
        "SCENARIO_REDEPLOYED",
        "SCENARIO_PAUSED",
        "SCENARIO_CANCELED",
        "SCENARIO_MODIFIED",
        "SCENARIO_MODIFIED_WITH_AUTOSAVE",
        "SCENARIO_NAME_CHANGED",
        "COMMENT_ADDED",
        "ATTACHMENT_ADDED",
        "CHANGED_PROCESSING_MODE",
        "INCOMING_MIGRATION",
        "OUTGOING_MIGRATION",
        "PERFORMED_SINGLE_EXECUTION",
        "PERFORMED_SCHEDULED_EXECUTION",
        "AUTOMATIC_UPDATE",
    ],
    typing.Any,
]
