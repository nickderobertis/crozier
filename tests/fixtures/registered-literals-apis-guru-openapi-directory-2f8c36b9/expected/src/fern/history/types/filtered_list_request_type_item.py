

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class FilteredListRequestTypeItem(enum.StrEnum):
    CREATED = "CREATED"
    DESTROYED = "DESTROYED"
    RECYCLED = "RECYCLED"
    SHIPMENT_PREPARED = "SHIPMENT_PREPARED"
    STORED = "STORED"
    RETRIEVED_FROM_STORAGE = "RETRIEVED_FROM_STORAGE"
    PACKAGED = "PACKAGED"
    DISPATCHED = "DISPATCHED"
    RECEIVED = "RECEIVED"
    DELIVERY_REFUSED = "DELIVERY_REFUSED"
    REPROCESSING_STARTED = "REPROCESSING_STARTED"
    REPROCESSING_STEP_STARTED = "REPROCESSING_STEP_STARTED"
    REPROCESSING_STEP_CANCELLED = "REPROCESSING_STEP_CANCELLED"
    REPROCESSING_STEP_FINISHED = "REPROCESSING_STEP_FINISHED"
    REPROCESSING_CANCELLED = "REPROCESSING_CANCELLED"
    REPROCESSING_FINISHED = "REPROCESSING_FINISHED"
    DISASSEMBLED = "DISASSEMBLED"
    MAINTENANCE_STARTED = "MAINTENANCE_STARTED"
    MAINTENANCE_STEP_STARTED = "MAINTENANCE_STEP_STARTED"
    MAINTENANCE_STEP_CANCELLED = "MAINTENANCE_STEP_CANCELLED"
    MAINTENANCE_STEP_FINISHED = "MAINTENANCE_STEP_FINISHED"
    MAINTENANCE_CANCELLED = "MAINTENANCE_CANCELLED"
    MAINTENANCE_FINISHED = "MAINTENANCE_FINISHED"
    PRODUCTION_STARTED = "PRODUCTION_STARTED"
    PRODUCTION_CANCELLED = "PRODUCTION_CANCELLED"
    PRODUCTION_FINISHED = "PRODUCTION_FINISHED"
    PRODUCTION_STEP_STARTED = "PRODUCTION_STEP_STARTED"
    PRODUCTION_STEP_CANCELLED = "PRODUCTION_STEP_CANCELLED"
    PRODUCTION_STEP_FINISHED = "PRODUCTION_STEP_FINISHED"
    QUALITY_CHECK_PERFORMED = "QUALITY_CHECK_PERFORMED"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        destroyed: typing.Callable[[], T_Result],
        recycled: typing.Callable[[], T_Result],
        shipment_prepared: typing.Callable[[], T_Result],
        stored: typing.Callable[[], T_Result],
        retrieved_from_storage: typing.Callable[[], T_Result],
        packaged: typing.Callable[[], T_Result],
        dispatched: typing.Callable[[], T_Result],
        received: typing.Callable[[], T_Result],
        delivery_refused: typing.Callable[[], T_Result],
        reprocessing_started: typing.Callable[[], T_Result],
        reprocessing_step_started: typing.Callable[[], T_Result],
        reprocessing_step_cancelled: typing.Callable[[], T_Result],
        reprocessing_step_finished: typing.Callable[[], T_Result],
        reprocessing_cancelled: typing.Callable[[], T_Result],
        reprocessing_finished: typing.Callable[[], T_Result],
        disassembled: typing.Callable[[], T_Result],
        maintenance_started: typing.Callable[[], T_Result],
        maintenance_step_started: typing.Callable[[], T_Result],
        maintenance_step_cancelled: typing.Callable[[], T_Result],
        maintenance_step_finished: typing.Callable[[], T_Result],
        maintenance_cancelled: typing.Callable[[], T_Result],
        maintenance_finished: typing.Callable[[], T_Result],
        production_started: typing.Callable[[], T_Result],
        production_cancelled: typing.Callable[[], T_Result],
        production_finished: typing.Callable[[], T_Result],
        production_step_started: typing.Callable[[], T_Result],
        production_step_cancelled: typing.Callable[[], T_Result],
        production_step_finished: typing.Callable[[], T_Result],
        quality_check_performed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FilteredListRequestTypeItem.CREATED:
            return created()
        if self is FilteredListRequestTypeItem.DESTROYED:
            return destroyed()
        if self is FilteredListRequestTypeItem.RECYCLED:
            return recycled()
        if self is FilteredListRequestTypeItem.SHIPMENT_PREPARED:
            return shipment_prepared()
        if self is FilteredListRequestTypeItem.STORED:
            return stored()
        if self is FilteredListRequestTypeItem.RETRIEVED_FROM_STORAGE:
            return retrieved_from_storage()
        if self is FilteredListRequestTypeItem.PACKAGED:
            return packaged()
        if self is FilteredListRequestTypeItem.DISPATCHED:
            return dispatched()
        if self is FilteredListRequestTypeItem.RECEIVED:
            return received()
        if self is FilteredListRequestTypeItem.DELIVERY_REFUSED:
            return delivery_refused()
        if self is FilteredListRequestTypeItem.REPROCESSING_STARTED:
            return reprocessing_started()
        if self is FilteredListRequestTypeItem.REPROCESSING_STEP_STARTED:
            return reprocessing_step_started()
        if self is FilteredListRequestTypeItem.REPROCESSING_STEP_CANCELLED:
            return reprocessing_step_cancelled()
        if self is FilteredListRequestTypeItem.REPROCESSING_STEP_FINISHED:
            return reprocessing_step_finished()
        if self is FilteredListRequestTypeItem.REPROCESSING_CANCELLED:
            return reprocessing_cancelled()
        if self is FilteredListRequestTypeItem.REPROCESSING_FINISHED:
            return reprocessing_finished()
        if self is FilteredListRequestTypeItem.DISASSEMBLED:
            return disassembled()
        if self is FilteredListRequestTypeItem.MAINTENANCE_STARTED:
            return maintenance_started()
        if self is FilteredListRequestTypeItem.MAINTENANCE_STEP_STARTED:
            return maintenance_step_started()
        if self is FilteredListRequestTypeItem.MAINTENANCE_STEP_CANCELLED:
            return maintenance_step_cancelled()
        if self is FilteredListRequestTypeItem.MAINTENANCE_STEP_FINISHED:
            return maintenance_step_finished()
        if self is FilteredListRequestTypeItem.MAINTENANCE_CANCELLED:
            return maintenance_cancelled()
        if self is FilteredListRequestTypeItem.MAINTENANCE_FINISHED:
            return maintenance_finished()
        if self is FilteredListRequestTypeItem.PRODUCTION_STARTED:
            return production_started()
        if self is FilteredListRequestTypeItem.PRODUCTION_CANCELLED:
            return production_cancelled()
        if self is FilteredListRequestTypeItem.PRODUCTION_FINISHED:
            return production_finished()
        if self is FilteredListRequestTypeItem.PRODUCTION_STEP_STARTED:
            return production_step_started()
        if self is FilteredListRequestTypeItem.PRODUCTION_STEP_CANCELLED:
            return production_step_cancelled()
        if self is FilteredListRequestTypeItem.PRODUCTION_STEP_FINISHED:
            return production_step_finished()
        if self is FilteredListRequestTypeItem.QUALITY_CHECK_PERFORMED:
            return quality_check_performed()
