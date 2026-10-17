

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusProgress(enum.StrEnum):
    ZERO_REQUESTED = "0_requested"
    ONE_STARTED = "1_started"
    TWO_LAUNCHED_UPGRADED_INSTANCE = "2_launched_upgraded_instance"
    THREE_DETACHED_VOLUME_FROM_UPGRADED_INSTANCE = "3_detached_volume_from_upgraded_instance"
    FOUR_ATTACHED_VOLUME_TO_ORIGINAL_INSTANCE = "4_attached_volume_to_original_instance"
    FIVE_INITIATED_DATA_UPGRADE = "5_initiated_data_upgrade"
    SIX_COMPLETED_DATA_UPGRADE = "6_completed_data_upgrade"
    SEVEN_DETACHED_VOLUME_FROM_ORIGINAL_INSTANCE = "7_detached_volume_from_original_instance"
    EIGHT_ATTACHED_VOLUME_TO_UPGRADED_INSTANCE = "8_attached_volume_to_upgraded_instance"
    NINE_COMPLETED_UPGRADE = "9_completed_upgrade"
    TEN_COMPLETED_POST_PHYSICAL_BACKUP = "10_completed_post_physical_backup"

    def visit(
        self,
        zero_requested: typing.Callable[[], T_Result],
        one_started: typing.Callable[[], T_Result],
        two_launched_upgraded_instance: typing.Callable[[], T_Result],
        three_detached_volume_from_upgraded_instance: typing.Callable[[], T_Result],
        four_attached_volume_to_original_instance: typing.Callable[[], T_Result],
        five_initiated_data_upgrade: typing.Callable[[], T_Result],
        six_completed_data_upgrade: typing.Callable[[], T_Result],
        seven_detached_volume_from_original_instance: typing.Callable[[], T_Result],
        eight_attached_volume_to_upgraded_instance: typing.Callable[[], T_Result],
        nine_completed_upgrade: typing.Callable[[], T_Result],
        ten_completed_post_physical_backup: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusProgress.ZERO_REQUESTED:
            return zero_requested()
        if self is DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusProgress.ONE_STARTED:
            return one_started()
        if self is DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusProgress.TWO_LAUNCHED_UPGRADED_INSTANCE:
            return two_launched_upgraded_instance()
        if (
            self
            is DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusProgress.THREE_DETACHED_VOLUME_FROM_UPGRADED_INSTANCE
        ):
            return three_detached_volume_from_upgraded_instance()
        if (
            self
            is DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusProgress.FOUR_ATTACHED_VOLUME_TO_ORIGINAL_INSTANCE
        ):
            return four_attached_volume_to_original_instance()
        if self is DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusProgress.FIVE_INITIATED_DATA_UPGRADE:
            return five_initiated_data_upgrade()
        if self is DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusProgress.SIX_COMPLETED_DATA_UPGRADE:
            return six_completed_data_upgrade()
        if (
            self
            is DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusProgress.SEVEN_DETACHED_VOLUME_FROM_ORIGINAL_INSTANCE
        ):
            return seven_detached_volume_from_original_instance()
        if (
            self
            is DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusProgress.EIGHT_ATTACHED_VOLUME_TO_UPGRADED_INSTANCE
        ):
            return eight_attached_volume_to_upgraded_instance()
        if self is DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusProgress.NINE_COMPLETED_UPGRADE:
            return nine_completed_upgrade()
        if self is DatabaseUpgradeStatusResponseOutputDatabaseUpgradeStatusProgress.TEN_COMPLETED_POST_PHYSICAL_BACKUP:
            return ten_completed_post_physical_backup()
