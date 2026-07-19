

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TriggerType(enum.StrEnum):
    QUOTA_THRESHOLD = "QUOTA_THRESHOLD"
    QHT = "QHT"
    FINAL = "FINAL"
    QUOTA_EXHAUSTED = "QUOTA_EXHAUSTED"
    VALIDITY_TIME = "VALIDITY_TIME"
    OTHER_QUOTA_TYPE = "OTHER_QUOTA_TYPE"
    FORCED_REAUTHORISATION = "FORCED_REAUTHORISATION"
    UNUSED_QUOTA_TIMER = "UNUSED_QUOTA_TIMER"
    ABNORMAL_RELEASE = "ABNORMAL_RELEASE"
    QOS_CHANGE = "QOS_CHANGE"
    VOLUME_LIMIT = "VOLUME_LIMIT"
    TIME_LIMIT = "TIME_LIMIT"
    PLMN_CHANGE = "PLMN_CHANGE"
    USER_LOCATION_CHANGE = "USER_LOCATION_CHANGE"
    RAT_CHANGE = "RAT_CHANGE"
    UE_TIMEZONE_CHANGE = "UE_TIMEZONE_CHANGE"
    TARIFF_TIME_CHANGE = "TARIFF_TIME_CHANGE"
    MAX_NUMBER_OF_CHANGES_IN_CHARGING_CONDITIONS = "MAX_NUMBER_OF_CHANGES_IN CHARGING_CONDITIONS"
    MANAGEMENT_INTERVENTION = "MANAGEMENT_INTERVENTION"
    CHANGE_OF_UE_PRESENCE_IN_PRESENCE_REPORTING_AREA = "CHANGE_OF_UE_PRESENCE_IN PRESENCE_REPORTING_AREA"
    CHANGE_OF3GPP_PS_DATA_OFF_STATUS = "CHANGE_OF_3GPP_PS_DATA_OFF_STATUS"
    SERVING_NODE_CHANGE = "SERVING_NODE_CHANGE"
    REMOVAL_OF_UPF = "REMOVAL_OF_UPF"
    ADDITION_OF_UPF = "ADDITION_OF_UPF"

    def visit(
        self,
        quota_threshold: typing.Callable[[], T_Result],
        qht: typing.Callable[[], T_Result],
        final: typing.Callable[[], T_Result],
        quota_exhausted: typing.Callable[[], T_Result],
        validity_time: typing.Callable[[], T_Result],
        other_quota_type: typing.Callable[[], T_Result],
        forced_reauthorisation: typing.Callable[[], T_Result],
        unused_quota_timer: typing.Callable[[], T_Result],
        abnormal_release: typing.Callable[[], T_Result],
        qos_change: typing.Callable[[], T_Result],
        volume_limit: typing.Callable[[], T_Result],
        time_limit: typing.Callable[[], T_Result],
        plmn_change: typing.Callable[[], T_Result],
        user_location_change: typing.Callable[[], T_Result],
        rat_change: typing.Callable[[], T_Result],
        ue_timezone_change: typing.Callable[[], T_Result],
        tariff_time_change: typing.Callable[[], T_Result],
        max_number_of_changes_in_charging_conditions: typing.Callable[[], T_Result],
        management_intervention: typing.Callable[[], T_Result],
        change_of_ue_presence_in_presence_reporting_area: typing.Callable[[], T_Result],
        change_of3gpp_ps_data_off_status: typing.Callable[[], T_Result],
        serving_node_change: typing.Callable[[], T_Result],
        removal_of_upf: typing.Callable[[], T_Result],
        addition_of_upf: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TriggerType.QUOTA_THRESHOLD:
            return quota_threshold()
        if self is TriggerType.QHT:
            return qht()
        if self is TriggerType.FINAL:
            return final()
        if self is TriggerType.QUOTA_EXHAUSTED:
            return quota_exhausted()
        if self is TriggerType.VALIDITY_TIME:
            return validity_time()
        if self is TriggerType.OTHER_QUOTA_TYPE:
            return other_quota_type()
        if self is TriggerType.FORCED_REAUTHORISATION:
            return forced_reauthorisation()
        if self is TriggerType.UNUSED_QUOTA_TIMER:
            return unused_quota_timer()
        if self is TriggerType.ABNORMAL_RELEASE:
            return abnormal_release()
        if self is TriggerType.QOS_CHANGE:
            return qos_change()
        if self is TriggerType.VOLUME_LIMIT:
            return volume_limit()
        if self is TriggerType.TIME_LIMIT:
            return time_limit()
        if self is TriggerType.PLMN_CHANGE:
            return plmn_change()
        if self is TriggerType.USER_LOCATION_CHANGE:
            return user_location_change()
        if self is TriggerType.RAT_CHANGE:
            return rat_change()
        if self is TriggerType.UE_TIMEZONE_CHANGE:
            return ue_timezone_change()
        if self is TriggerType.TARIFF_TIME_CHANGE:
            return tariff_time_change()
        if self is TriggerType.MAX_NUMBER_OF_CHANGES_IN_CHARGING_CONDITIONS:
            return max_number_of_changes_in_charging_conditions()
        if self is TriggerType.MANAGEMENT_INTERVENTION:
            return management_intervention()
        if self is TriggerType.CHANGE_OF_UE_PRESENCE_IN_PRESENCE_REPORTING_AREA:
            return change_of_ue_presence_in_presence_reporting_area()
        if self is TriggerType.CHANGE_OF3GPP_PS_DATA_OFF_STATUS:
            return change_of3gpp_ps_data_off_status()
        if self is TriggerType.SERVING_NODE_CHANGE:
            return serving_node_change()
        if self is TriggerType.REMOVAL_OF_UPF:
            return removal_of_upf()
        if self is TriggerType.ADDITION_OF_UPF:
            return addition_of_upf()
