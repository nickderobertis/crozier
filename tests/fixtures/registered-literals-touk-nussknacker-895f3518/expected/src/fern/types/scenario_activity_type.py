

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ScenarioActivityType(enum.StrEnum):
    SCENARIO_CREATED = "SCENARIO_CREATED"
    SCENARIO_ARCHIVED = "SCENARIO_ARCHIVED"
    SCENARIO_UNARCHIVED = "SCENARIO_UNARCHIVED"
    SCENARIO_DEPLOYED = "SCENARIO_DEPLOYED"
    SCENARIO_REDEPLOYED = "SCENARIO_REDEPLOYED"
    SCENARIO_PAUSED = "SCENARIO_PAUSED"
    SCENARIO_CANCELED = "SCENARIO_CANCELED"
    SCENARIO_MODIFIED = "SCENARIO_MODIFIED"
    SCENARIO_MODIFIED_WITH_AUTOSAVE = "SCENARIO_MODIFIED_WITH_AUTOSAVE"
    SCENARIO_NAME_CHANGED = "SCENARIO_NAME_CHANGED"
    COMMENT_ADDED = "COMMENT_ADDED"
    ATTACHMENT_ADDED = "ATTACHMENT_ADDED"
    CHANGED_PROCESSING_MODE = "CHANGED_PROCESSING_MODE"
    INCOMING_MIGRATION = "INCOMING_MIGRATION"
    OUTGOING_MIGRATION = "OUTGOING_MIGRATION"
    PERFORMED_SINGLE_EXECUTION = "PERFORMED_SINGLE_EXECUTION"
    PERFORMED_SCHEDULED_EXECUTION = "PERFORMED_SCHEDULED_EXECUTION"
    AUTOMATIC_UPDATE = "AUTOMATIC_UPDATE"

    def visit(
        self,
        scenario_created: typing.Callable[[], T_Result],
        scenario_archived: typing.Callable[[], T_Result],
        scenario_unarchived: typing.Callable[[], T_Result],
        scenario_deployed: typing.Callable[[], T_Result],
        scenario_redeployed: typing.Callable[[], T_Result],
        scenario_paused: typing.Callable[[], T_Result],
        scenario_canceled: typing.Callable[[], T_Result],
        scenario_modified: typing.Callable[[], T_Result],
        scenario_modified_with_autosave: typing.Callable[[], T_Result],
        scenario_name_changed: typing.Callable[[], T_Result],
        comment_added: typing.Callable[[], T_Result],
        attachment_added: typing.Callable[[], T_Result],
        changed_processing_mode: typing.Callable[[], T_Result],
        incoming_migration: typing.Callable[[], T_Result],
        outgoing_migration: typing.Callable[[], T_Result],
        performed_single_execution: typing.Callable[[], T_Result],
        performed_scheduled_execution: typing.Callable[[], T_Result],
        automatic_update: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ScenarioActivityType.SCENARIO_CREATED:
            return scenario_created()
        if self is ScenarioActivityType.SCENARIO_ARCHIVED:
            return scenario_archived()
        if self is ScenarioActivityType.SCENARIO_UNARCHIVED:
            return scenario_unarchived()
        if self is ScenarioActivityType.SCENARIO_DEPLOYED:
            return scenario_deployed()
        if self is ScenarioActivityType.SCENARIO_REDEPLOYED:
            return scenario_redeployed()
        if self is ScenarioActivityType.SCENARIO_PAUSED:
            return scenario_paused()
        if self is ScenarioActivityType.SCENARIO_CANCELED:
            return scenario_canceled()
        if self is ScenarioActivityType.SCENARIO_MODIFIED:
            return scenario_modified()
        if self is ScenarioActivityType.SCENARIO_MODIFIED_WITH_AUTOSAVE:
            return scenario_modified_with_autosave()
        if self is ScenarioActivityType.SCENARIO_NAME_CHANGED:
            return scenario_name_changed()
        if self is ScenarioActivityType.COMMENT_ADDED:
            return comment_added()
        if self is ScenarioActivityType.ATTACHMENT_ADDED:
            return attachment_added()
        if self is ScenarioActivityType.CHANGED_PROCESSING_MODE:
            return changed_processing_mode()
        if self is ScenarioActivityType.INCOMING_MIGRATION:
            return incoming_migration()
        if self is ScenarioActivityType.OUTGOING_MIGRATION:
            return outgoing_migration()
        if self is ScenarioActivityType.PERFORMED_SINGLE_EXECUTION:
            return performed_single_execution()
        if self is ScenarioActivityType.PERFORMED_SCHEDULED_EXECUTION:
            return performed_scheduled_execution()
        if self is ScenarioActivityType.AUTOMATIC_UPDATE:
            return automatic_update()
