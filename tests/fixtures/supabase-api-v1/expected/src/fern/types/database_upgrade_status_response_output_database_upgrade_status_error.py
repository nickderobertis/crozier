

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusError(enum.StrEnum):
    ONE_UPGRADED_INSTANCE_LAUNCH_FAILED = "1_upgraded_instance_launch_failed"
    TWO_VOLUME_DETACHCHMENT_FROM_UPGRADED_INSTANCE_FAILED = "2_volume_detachchment_from_upgraded_instance_failed"
    THREE_VOLUME_ATTACHMENT_TO_ORIGINAL_INSTANCE_FAILED = "3_volume_attachment_to_original_instance_failed"
    FOUR_DATA_UPGRADE_INITIATION_FAILED = "4_data_upgrade_initiation_failed"
    FIVE_DATA_UPGRADE_COMPLETION_FAILED = "5_data_upgrade_completion_failed"
    SIX_VOLUME_DETACHCHMENT_FROM_ORIGINAL_INSTANCE_FAILED = "6_volume_detachchment_from_original_instance_failed"
    SEVEN_VOLUME_ATTACHMENT_TO_UPGRADED_INSTANCE_FAILED = "7_volume_attachment_to_upgraded_instance_failed"
    EIGHT_UPGRADE_COMPLETION_FAILED = "8_upgrade_completion_failed"
    NINE_POST_PHYSICAL_BACKUP_FAILED = "9_post_physical_backup_failed"

    def visit(
        self,
        one_upgraded_instance_launch_failed: typing.Callable[[], T_Result],
        two_volume_detachchment_from_upgraded_instance_failed: typing.Callable[[], T_Result],
        three_volume_attachment_to_original_instance_failed: typing.Callable[[], T_Result],
        four_data_upgrade_initiation_failed: typing.Callable[[], T_Result],
        five_data_upgrade_completion_failed: typing.Callable[[], T_Result],
        six_volume_detachchment_from_original_instance_failed: typing.Callable[[], T_Result],
        seven_volume_attachment_to_upgraded_instance_failed: typing.Callable[[], T_Result],
        eight_upgrade_completion_failed: typing.Callable[[], T_Result],
        nine_post_physical_backup_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusError.ONE_UPGRADED_INSTANCE_LAUNCH_FAILED:
            return one_upgraded_instance_launch_failed()
        if (
            self
            is DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusError.TWO_VOLUME_DETACHCHMENT_FROM_UPGRADED_INSTANCE_FAILED
        ):
            return two_volume_detachchment_from_upgraded_instance_failed()
        if (
            self
            is DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusError.THREE_VOLUME_ATTACHMENT_TO_ORIGINAL_INSTANCE_FAILED
        ):
            return three_volume_attachment_to_original_instance_failed()
        if self is DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusError.FOUR_DATA_UPGRADE_INITIATION_FAILED:
            return four_data_upgrade_initiation_failed()
        if self is DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusError.FIVE_DATA_UPGRADE_COMPLETION_FAILED:
            return five_data_upgrade_completion_failed()
        if (
            self
            is DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusError.SIX_VOLUME_DETACHCHMENT_FROM_ORIGINAL_INSTANCE_FAILED
        ):
            return six_volume_detachchment_from_original_instance_failed()
        if (
            self
            is DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusError.SEVEN_VOLUME_ATTACHMENT_TO_UPGRADED_INSTANCE_FAILED
        ):
            return seven_volume_attachment_to_upgraded_instance_failed()
        if self is DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusError.EIGHT_UPGRADE_COMPLETION_FAILED:
            return eight_upgrade_completion_failed()
        if self is DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusError.NINE_POST_PHYSICAL_BACKUP_FAILED:
            return nine_post_physical_backup_failed()
