



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .dbv0037account import Dbv0037Account
    from .dbv0037account_info import Dbv0037AccountInfo
    from .dbv0037account_response import Dbv0037AccountResponse
    from .dbv0037association import Dbv0037Association
    from .dbv0037association_default import Dbv0037AssociationDefault
    from .dbv0037association_max import Dbv0037AssociationMax
    from .dbv0037association_max_jobs import Dbv0037AssociationMaxJobs
    from .dbv0037association_max_jobs_per import Dbv0037AssociationMaxJobsPer
    from .dbv0037association_max_per import Dbv0037AssociationMaxPer
    from .dbv0037association_max_per_account import Dbv0037AssociationMaxPerAccount
    from .dbv0037association_max_tres import Dbv0037AssociationMaxTres
    from .dbv0037association_max_tres_minutes import Dbv0037AssociationMaxTresMinutes
    from .dbv0037association_max_tres_minutes_per import Dbv0037AssociationMaxTresMinutesPer
    from .dbv0037association_max_tres_minutes_per_job_item import Dbv0037AssociationMaxTresMinutesPerJobItem
    from .dbv0037association_max_tres_minutes_total_item import Dbv0037AssociationMaxTresMinutesTotalItem
    from .dbv0037association_max_tres_per import Dbv0037AssociationMaxTresPer
    from .dbv0037association_max_tres_per_job_item import Dbv0037AssociationMaxTresPerJobItem
    from .dbv0037association_max_tres_per_node_item import Dbv0037AssociationMaxTresPerNodeItem
    from .dbv0037association_max_tres_total_item import Dbv0037AssociationMaxTresTotalItem
    from .dbv0037association_min import Dbv0037AssociationMin
    from .dbv0037association_short_info import Dbv0037AssociationShortInfo
    from .dbv0037association_usage import Dbv0037AssociationUsage
    from .dbv0037associations_info import Dbv0037AssociationsInfo
    from .dbv0037cluster_info import Dbv0037ClusterInfo
    from .dbv0037cluster_info_associations import Dbv0037ClusterInfoAssociations
    from .dbv0037cluster_info_controller import Dbv0037ClusterInfoController
    from .dbv0037config_info import Dbv0037ConfigInfo
    from .dbv0037config_response import Dbv0037ConfigResponse
    from .dbv0037coordinator_info import Dbv0037CoordinatorInfo
    from .dbv0037diag import Dbv0037Diag
    from .dbv0037diag_statistics import Dbv0037DiagStatistics
    from .dbv0037diag_statistics_rollups import Dbv0037DiagStatisticsRollups
    from .dbv0037diag_statistics_rp_cs import Dbv0037DiagStatisticsRpCs
    from .dbv0037diag_statistics_time import Dbv0037DiagStatisticsTime
    from .dbv0037diag_statistics_time1 import Dbv0037DiagStatisticsTime1
    from .dbv0037diag_statistics_users import Dbv0037DiagStatisticsUsers
    from .dbv0037error import Dbv0037Error
    from .dbv0037job import Dbv0037Job
    from .dbv0037job_array import Dbv0037JobArray
    from .dbv0037job_array_limits import Dbv0037JobArrayLimits
    from .dbv0037job_array_limits_max import Dbv0037JobArrayLimitsMax
    from .dbv0037job_array_limits_max_running import Dbv0037JobArrayLimitsMaxRunning
    from .dbv0037job_comment import Dbv0037JobComment
    from .dbv0037job_exit_code import Dbv0037JobExitCode
    from .dbv0037job_exit_code_signal import Dbv0037JobExitCodeSignal
    from .dbv0037job_het import Dbv0037JobHet
    from .dbv0037job_info import Dbv0037JobInfo
    from .dbv0037job_mcs import Dbv0037JobMcs
    from .dbv0037job_required import Dbv0037JobRequired
    from .dbv0037job_reservation import Dbv0037JobReservation
    from .dbv0037job_state import Dbv0037JobState
    from .dbv0037job_step import Dbv0037JobStep
    from .dbv0037job_step_cpu import Dbv0037JobStepCpu
    from .dbv0037job_step_cpu_requested_frequency import Dbv0037JobStepCpuRequestedFrequency
    from .dbv0037job_step_nodes import Dbv0037JobStepNodes
    from .dbv0037job_step_statistics import Dbv0037JobStepStatistics
    from .dbv0037job_step_statistics_cpu import Dbv0037JobStepStatisticsCpu
    from .dbv0037job_step_statistics_energy import Dbv0037JobStepStatisticsEnergy
    from .dbv0037job_step_step import Dbv0037JobStepStep
    from .dbv0037job_step_step_het import Dbv0037JobStepStepHet
    from .dbv0037job_step_step_task import Dbv0037JobStepStepTask
    from .dbv0037job_step_step_tres import Dbv0037JobStepStepTres
    from .dbv0037job_step_step_tres_allocated_item import Dbv0037JobStepStepTresAllocatedItem
    from .dbv0037job_step_step_tres_requested import Dbv0037JobStepStepTresRequested
    from .dbv0037job_step_step_tres_requested_average_item import Dbv0037JobStepStepTresRequestedAverageItem
    from .dbv0037job_step_step_tres_requested_max_item import Dbv0037JobStepStepTresRequestedMaxItem
    from .dbv0037job_step_step_tres_requested_min_item import Dbv0037JobStepStepTresRequestedMinItem
    from .dbv0037job_step_step_tres_requested_total_item import Dbv0037JobStepStepTresRequestedTotalItem
    from .dbv0037job_step_tasks import Dbv0037JobStepTasks
    from .dbv0037job_step_time import Dbv0037JobStepTime
    from .dbv0037job_time import Dbv0037JobTime
    from .dbv0037job_time_system import Dbv0037JobTimeSystem
    from .dbv0037job_time_total import Dbv0037JobTimeTotal
    from .dbv0037job_time_user import Dbv0037JobTimeUser
    from .dbv0037job_tres import Dbv0037JobTres
    from .dbv0037job_tres_allocated_item import Dbv0037JobTresAllocatedItem
    from .dbv0037job_tres_requested_item import Dbv0037JobTresRequestedItem
    from .dbv0037job_wckey import Dbv0037JobWckey
    from .dbv0037qos import Dbv0037Qos
    from .dbv0037qos_info import Dbv0037QosInfo
    from .dbv0037qos_limits import Dbv0037QosLimits
    from .dbv0037qos_limits_max import Dbv0037QosLimitsMax
    from .dbv0037qos_limits_max_accruing import Dbv0037QosLimitsMaxAccruing
    from .dbv0037qos_limits_max_accruing_per import Dbv0037QosLimitsMaxAccruingPer
    from .dbv0037qos_limits_max_jobs import Dbv0037QosLimitsMaxJobs
    from .dbv0037qos_limits_max_jobs_per import Dbv0037QosLimitsMaxJobsPer
    from .dbv0037qos_limits_max_tres import Dbv0037QosLimitsMaxTres
    from .dbv0037qos_limits_max_tres_minutes import Dbv0037QosLimitsMaxTresMinutes
    from .dbv0037qos_limits_max_tres_minutes_per import Dbv0037QosLimitsMaxTresMinutesPer
    from .dbv0037qos_limits_max_tres_minutes_per_account_item import Dbv0037QosLimitsMaxTresMinutesPerAccountItem
    from .dbv0037qos_limits_max_tres_minutes_per_job_item import Dbv0037QosLimitsMaxTresMinutesPerJobItem
    from .dbv0037qos_limits_max_tres_minutes_per_user_item import Dbv0037QosLimitsMaxTresMinutesPerUserItem
    from .dbv0037qos_limits_max_tres_per import Dbv0037QosLimitsMaxTresPer
    from .dbv0037qos_limits_max_tres_per_account_item import Dbv0037QosLimitsMaxTresPerAccountItem
    from .dbv0037qos_limits_max_tres_per_job_item import Dbv0037QosLimitsMaxTresPerJobItem
    from .dbv0037qos_limits_max_tres_per_node_item import Dbv0037QosLimitsMaxTresPerNodeItem
    from .dbv0037qos_limits_max_tres_per_user_item import Dbv0037QosLimitsMaxTresPerUserItem
    from .dbv0037qos_limits_max_wall_clock import Dbv0037QosLimitsMaxWallClock
    from .dbv0037qos_limits_max_wall_clock_per import Dbv0037QosLimitsMaxWallClockPer
    from .dbv0037qos_limits_min import Dbv0037QosLimitsMin
    from .dbv0037qos_limits_min_tres import Dbv0037QosLimitsMinTres
    from .dbv0037qos_limits_min_tres_per import Dbv0037QosLimitsMinTresPer
    from .dbv0037qos_limits_min_tres_per_job_item import Dbv0037QosLimitsMinTresPerJobItem
    from .dbv0037qos_preempt import Dbv0037QosPreempt
    from .dbv0037response_account_delete import Dbv0037ResponseAccountDelete
    from .dbv0037response_association_delete import Dbv0037ResponseAssociationDelete
    from .dbv0037response_cluster_add import Dbv0037ResponseClusterAdd
    from .dbv0037response_cluster_delete import Dbv0037ResponseClusterDelete
    from .dbv0037response_qos_delete import Dbv0037ResponseQosDelete
    from .dbv0037response_tres import Dbv0037ResponseTres
    from .dbv0037response_user_delete import Dbv0037ResponseUserDelete
    from .dbv0037response_user_update import Dbv0037ResponseUserUpdate
    from .dbv0037response_wckey_add import Dbv0037ResponseWckeyAdd
    from .dbv0037response_wckey_delete import Dbv0037ResponseWckeyDelete
    from .dbv0037tres_info import Dbv0037TresInfo
    from .dbv0037tres_list import Dbv0037TresList
    from .dbv0037tres_list_item import Dbv0037TresListItem
    from .dbv0037user import Dbv0037User
    from .dbv0037user_associations import Dbv0037UserAssociations
    from .dbv0037user_default import Dbv0037UserDefault
    from .dbv0037user_info import Dbv0037UserInfo
    from .dbv0037wckey import Dbv0037Wckey
    from .dbv0037wckey_info import Dbv0037WckeyInfo
_dynamic_imports: typing.Dict[str, str] = {
    "Dbv0037Account": ".dbv0037account",
    "Dbv0037AccountInfo": ".dbv0037account_info",
    "Dbv0037AccountResponse": ".dbv0037account_response",
    "Dbv0037Association": ".dbv0037association",
    "Dbv0037AssociationDefault": ".dbv0037association_default",
    "Dbv0037AssociationMax": ".dbv0037association_max",
    "Dbv0037AssociationMaxJobs": ".dbv0037association_max_jobs",
    "Dbv0037AssociationMaxJobsPer": ".dbv0037association_max_jobs_per",
    "Dbv0037AssociationMaxPer": ".dbv0037association_max_per",
    "Dbv0037AssociationMaxPerAccount": ".dbv0037association_max_per_account",
    "Dbv0037AssociationMaxTres": ".dbv0037association_max_tres",
    "Dbv0037AssociationMaxTresMinutes": ".dbv0037association_max_tres_minutes",
    "Dbv0037AssociationMaxTresMinutesPer": ".dbv0037association_max_tres_minutes_per",
    "Dbv0037AssociationMaxTresMinutesPerJobItem": ".dbv0037association_max_tres_minutes_per_job_item",
    "Dbv0037AssociationMaxTresMinutesTotalItem": ".dbv0037association_max_tres_minutes_total_item",
    "Dbv0037AssociationMaxTresPer": ".dbv0037association_max_tres_per",
    "Dbv0037AssociationMaxTresPerJobItem": ".dbv0037association_max_tres_per_job_item",
    "Dbv0037AssociationMaxTresPerNodeItem": ".dbv0037association_max_tres_per_node_item",
    "Dbv0037AssociationMaxTresTotalItem": ".dbv0037association_max_tres_total_item",
    "Dbv0037AssociationMin": ".dbv0037association_min",
    "Dbv0037AssociationShortInfo": ".dbv0037association_short_info",
    "Dbv0037AssociationUsage": ".dbv0037association_usage",
    "Dbv0037AssociationsInfo": ".dbv0037associations_info",
    "Dbv0037ClusterInfo": ".dbv0037cluster_info",
    "Dbv0037ClusterInfoAssociations": ".dbv0037cluster_info_associations",
    "Dbv0037ClusterInfoController": ".dbv0037cluster_info_controller",
    "Dbv0037ConfigInfo": ".dbv0037config_info",
    "Dbv0037ConfigResponse": ".dbv0037config_response",
    "Dbv0037CoordinatorInfo": ".dbv0037coordinator_info",
    "Dbv0037Diag": ".dbv0037diag",
    "Dbv0037DiagStatistics": ".dbv0037diag_statistics",
    "Dbv0037DiagStatisticsRollups": ".dbv0037diag_statistics_rollups",
    "Dbv0037DiagStatisticsRpCs": ".dbv0037diag_statistics_rp_cs",
    "Dbv0037DiagStatisticsTime": ".dbv0037diag_statistics_time",
    "Dbv0037DiagStatisticsTime1": ".dbv0037diag_statistics_time1",
    "Dbv0037DiagStatisticsUsers": ".dbv0037diag_statistics_users",
    "Dbv0037Error": ".dbv0037error",
    "Dbv0037Job": ".dbv0037job",
    "Dbv0037JobArray": ".dbv0037job_array",
    "Dbv0037JobArrayLimits": ".dbv0037job_array_limits",
    "Dbv0037JobArrayLimitsMax": ".dbv0037job_array_limits_max",
    "Dbv0037JobArrayLimitsMaxRunning": ".dbv0037job_array_limits_max_running",
    "Dbv0037JobComment": ".dbv0037job_comment",
    "Dbv0037JobExitCode": ".dbv0037job_exit_code",
    "Dbv0037JobExitCodeSignal": ".dbv0037job_exit_code_signal",
    "Dbv0037JobHet": ".dbv0037job_het",
    "Dbv0037JobInfo": ".dbv0037job_info",
    "Dbv0037JobMcs": ".dbv0037job_mcs",
    "Dbv0037JobRequired": ".dbv0037job_required",
    "Dbv0037JobReservation": ".dbv0037job_reservation",
    "Dbv0037JobState": ".dbv0037job_state",
    "Dbv0037JobStep": ".dbv0037job_step",
    "Dbv0037JobStepCpu": ".dbv0037job_step_cpu",
    "Dbv0037JobStepCpuRequestedFrequency": ".dbv0037job_step_cpu_requested_frequency",
    "Dbv0037JobStepNodes": ".dbv0037job_step_nodes",
    "Dbv0037JobStepStatistics": ".dbv0037job_step_statistics",
    "Dbv0037JobStepStatisticsCpu": ".dbv0037job_step_statistics_cpu",
    "Dbv0037JobStepStatisticsEnergy": ".dbv0037job_step_statistics_energy",
    "Dbv0037JobStepStep": ".dbv0037job_step_step",
    "Dbv0037JobStepStepHet": ".dbv0037job_step_step_het",
    "Dbv0037JobStepStepTask": ".dbv0037job_step_step_task",
    "Dbv0037JobStepStepTres": ".dbv0037job_step_step_tres",
    "Dbv0037JobStepStepTresAllocatedItem": ".dbv0037job_step_step_tres_allocated_item",
    "Dbv0037JobStepStepTresRequested": ".dbv0037job_step_step_tres_requested",
    "Dbv0037JobStepStepTresRequestedAverageItem": ".dbv0037job_step_step_tres_requested_average_item",
    "Dbv0037JobStepStepTresRequestedMaxItem": ".dbv0037job_step_step_tres_requested_max_item",
    "Dbv0037JobStepStepTresRequestedMinItem": ".dbv0037job_step_step_tres_requested_min_item",
    "Dbv0037JobStepStepTresRequestedTotalItem": ".dbv0037job_step_step_tres_requested_total_item",
    "Dbv0037JobStepTasks": ".dbv0037job_step_tasks",
    "Dbv0037JobStepTime": ".dbv0037job_step_time",
    "Dbv0037JobTime": ".dbv0037job_time",
    "Dbv0037JobTimeSystem": ".dbv0037job_time_system",
    "Dbv0037JobTimeTotal": ".dbv0037job_time_total",
    "Dbv0037JobTimeUser": ".dbv0037job_time_user",
    "Dbv0037JobTres": ".dbv0037job_tres",
    "Dbv0037JobTresAllocatedItem": ".dbv0037job_tres_allocated_item",
    "Dbv0037JobTresRequestedItem": ".dbv0037job_tres_requested_item",
    "Dbv0037JobWckey": ".dbv0037job_wckey",
    "Dbv0037Qos": ".dbv0037qos",
    "Dbv0037QosInfo": ".dbv0037qos_info",
    "Dbv0037QosLimits": ".dbv0037qos_limits",
    "Dbv0037QosLimitsMax": ".dbv0037qos_limits_max",
    "Dbv0037QosLimitsMaxAccruing": ".dbv0037qos_limits_max_accruing",
    "Dbv0037QosLimitsMaxAccruingPer": ".dbv0037qos_limits_max_accruing_per",
    "Dbv0037QosLimitsMaxJobs": ".dbv0037qos_limits_max_jobs",
    "Dbv0037QosLimitsMaxJobsPer": ".dbv0037qos_limits_max_jobs_per",
    "Dbv0037QosLimitsMaxTres": ".dbv0037qos_limits_max_tres",
    "Dbv0037QosLimitsMaxTresMinutes": ".dbv0037qos_limits_max_tres_minutes",
    "Dbv0037QosLimitsMaxTresMinutesPer": ".dbv0037qos_limits_max_tres_minutes_per",
    "Dbv0037QosLimitsMaxTresMinutesPerAccountItem": ".dbv0037qos_limits_max_tres_minutes_per_account_item",
    "Dbv0037QosLimitsMaxTresMinutesPerJobItem": ".dbv0037qos_limits_max_tres_minutes_per_job_item",
    "Dbv0037QosLimitsMaxTresMinutesPerUserItem": ".dbv0037qos_limits_max_tres_minutes_per_user_item",
    "Dbv0037QosLimitsMaxTresPer": ".dbv0037qos_limits_max_tres_per",
    "Dbv0037QosLimitsMaxTresPerAccountItem": ".dbv0037qos_limits_max_tres_per_account_item",
    "Dbv0037QosLimitsMaxTresPerJobItem": ".dbv0037qos_limits_max_tres_per_job_item",
    "Dbv0037QosLimitsMaxTresPerNodeItem": ".dbv0037qos_limits_max_tres_per_node_item",
    "Dbv0037QosLimitsMaxTresPerUserItem": ".dbv0037qos_limits_max_tres_per_user_item",
    "Dbv0037QosLimitsMaxWallClock": ".dbv0037qos_limits_max_wall_clock",
    "Dbv0037QosLimitsMaxWallClockPer": ".dbv0037qos_limits_max_wall_clock_per",
    "Dbv0037QosLimitsMin": ".dbv0037qos_limits_min",
    "Dbv0037QosLimitsMinTres": ".dbv0037qos_limits_min_tres",
    "Dbv0037QosLimitsMinTresPer": ".dbv0037qos_limits_min_tres_per",
    "Dbv0037QosLimitsMinTresPerJobItem": ".dbv0037qos_limits_min_tres_per_job_item",
    "Dbv0037QosPreempt": ".dbv0037qos_preempt",
    "Dbv0037ResponseAccountDelete": ".dbv0037response_account_delete",
    "Dbv0037ResponseAssociationDelete": ".dbv0037response_association_delete",
    "Dbv0037ResponseClusterAdd": ".dbv0037response_cluster_add",
    "Dbv0037ResponseClusterDelete": ".dbv0037response_cluster_delete",
    "Dbv0037ResponseQosDelete": ".dbv0037response_qos_delete",
    "Dbv0037ResponseTres": ".dbv0037response_tres",
    "Dbv0037ResponseUserDelete": ".dbv0037response_user_delete",
    "Dbv0037ResponseUserUpdate": ".dbv0037response_user_update",
    "Dbv0037ResponseWckeyAdd": ".dbv0037response_wckey_add",
    "Dbv0037ResponseWckeyDelete": ".dbv0037response_wckey_delete",
    "Dbv0037TresInfo": ".dbv0037tres_info",
    "Dbv0037TresList": ".dbv0037tres_list",
    "Dbv0037TresListItem": ".dbv0037tres_list_item",
    "Dbv0037User": ".dbv0037user",
    "Dbv0037UserAssociations": ".dbv0037user_associations",
    "Dbv0037UserDefault": ".dbv0037user_default",
    "Dbv0037UserInfo": ".dbv0037user_info",
    "Dbv0037Wckey": ".dbv0037wckey",
    "Dbv0037WckeyInfo": ".dbv0037wckey_info",
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
    "Dbv0037Account",
    "Dbv0037AccountInfo",
    "Dbv0037AccountResponse",
    "Dbv0037Association",
    "Dbv0037AssociationDefault",
    "Dbv0037AssociationMax",
    "Dbv0037AssociationMaxJobs",
    "Dbv0037AssociationMaxJobsPer",
    "Dbv0037AssociationMaxPer",
    "Dbv0037AssociationMaxPerAccount",
    "Dbv0037AssociationMaxTres",
    "Dbv0037AssociationMaxTresMinutes",
    "Dbv0037AssociationMaxTresMinutesPer",
    "Dbv0037AssociationMaxTresMinutesPerJobItem",
    "Dbv0037AssociationMaxTresMinutesTotalItem",
    "Dbv0037AssociationMaxTresPer",
    "Dbv0037AssociationMaxTresPerJobItem",
    "Dbv0037AssociationMaxTresPerNodeItem",
    "Dbv0037AssociationMaxTresTotalItem",
    "Dbv0037AssociationMin",
    "Dbv0037AssociationShortInfo",
    "Dbv0037AssociationUsage",
    "Dbv0037AssociationsInfo",
    "Dbv0037ClusterInfo",
    "Dbv0037ClusterInfoAssociations",
    "Dbv0037ClusterInfoController",
    "Dbv0037ConfigInfo",
    "Dbv0037ConfigResponse",
    "Dbv0037CoordinatorInfo",
    "Dbv0037Diag",
    "Dbv0037DiagStatistics",
    "Dbv0037DiagStatisticsRollups",
    "Dbv0037DiagStatisticsRpCs",
    "Dbv0037DiagStatisticsTime",
    "Dbv0037DiagStatisticsTime1",
    "Dbv0037DiagStatisticsUsers",
    "Dbv0037Error",
    "Dbv0037Job",
    "Dbv0037JobArray",
    "Dbv0037JobArrayLimits",
    "Dbv0037JobArrayLimitsMax",
    "Dbv0037JobArrayLimitsMaxRunning",
    "Dbv0037JobComment",
    "Dbv0037JobExitCode",
    "Dbv0037JobExitCodeSignal",
    "Dbv0037JobHet",
    "Dbv0037JobInfo",
    "Dbv0037JobMcs",
    "Dbv0037JobRequired",
    "Dbv0037JobReservation",
    "Dbv0037JobState",
    "Dbv0037JobStep",
    "Dbv0037JobStepCpu",
    "Dbv0037JobStepCpuRequestedFrequency",
    "Dbv0037JobStepNodes",
    "Dbv0037JobStepStatistics",
    "Dbv0037JobStepStatisticsCpu",
    "Dbv0037JobStepStatisticsEnergy",
    "Dbv0037JobStepStep",
    "Dbv0037JobStepStepHet",
    "Dbv0037JobStepStepTask",
    "Dbv0037JobStepStepTres",
    "Dbv0037JobStepStepTresAllocatedItem",
    "Dbv0037JobStepStepTresRequested",
    "Dbv0037JobStepStepTresRequestedAverageItem",
    "Dbv0037JobStepStepTresRequestedMaxItem",
    "Dbv0037JobStepStepTresRequestedMinItem",
    "Dbv0037JobStepStepTresRequestedTotalItem",
    "Dbv0037JobStepTasks",
    "Dbv0037JobStepTime",
    "Dbv0037JobTime",
    "Dbv0037JobTimeSystem",
    "Dbv0037JobTimeTotal",
    "Dbv0037JobTimeUser",
    "Dbv0037JobTres",
    "Dbv0037JobTresAllocatedItem",
    "Dbv0037JobTresRequestedItem",
    "Dbv0037JobWckey",
    "Dbv0037Qos",
    "Dbv0037QosInfo",
    "Dbv0037QosLimits",
    "Dbv0037QosLimitsMax",
    "Dbv0037QosLimitsMaxAccruing",
    "Dbv0037QosLimitsMaxAccruingPer",
    "Dbv0037QosLimitsMaxJobs",
    "Dbv0037QosLimitsMaxJobsPer",
    "Dbv0037QosLimitsMaxTres",
    "Dbv0037QosLimitsMaxTresMinutes",
    "Dbv0037QosLimitsMaxTresMinutesPer",
    "Dbv0037QosLimitsMaxTresMinutesPerAccountItem",
    "Dbv0037QosLimitsMaxTresMinutesPerJobItem",
    "Dbv0037QosLimitsMaxTresMinutesPerUserItem",
    "Dbv0037QosLimitsMaxTresPer",
    "Dbv0037QosLimitsMaxTresPerAccountItem",
    "Dbv0037QosLimitsMaxTresPerJobItem",
    "Dbv0037QosLimitsMaxTresPerNodeItem",
    "Dbv0037QosLimitsMaxTresPerUserItem",
    "Dbv0037QosLimitsMaxWallClock",
    "Dbv0037QosLimitsMaxWallClockPer",
    "Dbv0037QosLimitsMin",
    "Dbv0037QosLimitsMinTres",
    "Dbv0037QosLimitsMinTresPer",
    "Dbv0037QosLimitsMinTresPerJobItem",
    "Dbv0037QosPreempt",
    "Dbv0037ResponseAccountDelete",
    "Dbv0037ResponseAssociationDelete",
    "Dbv0037ResponseClusterAdd",
    "Dbv0037ResponseClusterDelete",
    "Dbv0037ResponseQosDelete",
    "Dbv0037ResponseTres",
    "Dbv0037ResponseUserDelete",
    "Dbv0037ResponseUserUpdate",
    "Dbv0037ResponseWckeyAdd",
    "Dbv0037ResponseWckeyDelete",
    "Dbv0037TresInfo",
    "Dbv0037TresList",
    "Dbv0037TresListItem",
    "Dbv0037User",
    "Dbv0037UserAssociations",
    "Dbv0037UserDefault",
    "Dbv0037UserInfo",
    "Dbv0037Wckey",
    "Dbv0037WckeyInfo",
]
