



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .participant_change_schedule_request_data import ParticipantChangeScheduleRequestData
    from .participant_change_schedule_request_data_attributes import ParticipantChangeScheduleRequestDataAttributes
    from .participant_change_schedule_request_data_attributes_course_identifier import (
        ParticipantChangeScheduleRequestDataAttributesCourseIdentifier,
    )
    from .participant_change_schedule_request_data_attributes_schedule_identifier import (
        ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier,
    )
    from .participant_defer_request_data import ParticipantDeferRequestData
    from .participant_defer_request_data_attributes import ParticipantDeferRequestDataAttributes
    from .participant_defer_request_data_attributes_course_identifier import (
        ParticipantDeferRequestDataAttributesCourseIdentifier,
    )
    from .participant_defer_request_data_attributes_reason import ParticipantDeferRequestDataAttributesReason
    from .participant_resume_request_data import ParticipantResumeRequestData
    from .participant_resume_request_data_attributes import ParticipantResumeRequestDataAttributes
    from .participant_resume_request_data_attributes_course_identifier import (
        ParticipantResumeRequestDataAttributesCourseIdentifier,
    )
    from .participant_withdraw_request_data import ParticipantWithdrawRequestData
    from .participant_withdraw_request_data_attributes import ParticipantWithdrawRequestDataAttributes
    from .participant_withdraw_request_data_attributes_course_identifier import (
        ParticipantWithdrawRequestDataAttributesCourseIdentifier,
    )
    from .participant_withdraw_request_data_attributes_reason import ParticipantWithdrawRequestDataAttributesReason
_dynamic_imports: typing.Dict[str, str] = {
    "ParticipantChangeScheduleRequestData": ".participant_change_schedule_request_data",
    "ParticipantChangeScheduleRequestDataAttributes": ".participant_change_schedule_request_data_attributes",
    "ParticipantChangeScheduleRequestDataAttributesCourseIdentifier": ".participant_change_schedule_request_data_attributes_course_identifier",
    "ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier": ".participant_change_schedule_request_data_attributes_schedule_identifier",
    "ParticipantDeferRequestData": ".participant_defer_request_data",
    "ParticipantDeferRequestDataAttributes": ".participant_defer_request_data_attributes",
    "ParticipantDeferRequestDataAttributesCourseIdentifier": ".participant_defer_request_data_attributes_course_identifier",
    "ParticipantDeferRequestDataAttributesReason": ".participant_defer_request_data_attributes_reason",
    "ParticipantResumeRequestData": ".participant_resume_request_data",
    "ParticipantResumeRequestDataAttributes": ".participant_resume_request_data_attributes",
    "ParticipantResumeRequestDataAttributesCourseIdentifier": ".participant_resume_request_data_attributes_course_identifier",
    "ParticipantWithdrawRequestData": ".participant_withdraw_request_data",
    "ParticipantWithdrawRequestDataAttributes": ".participant_withdraw_request_data_attributes",
    "ParticipantWithdrawRequestDataAttributesCourseIdentifier": ".participant_withdraw_request_data_attributes_course_identifier",
    "ParticipantWithdrawRequestDataAttributesReason": ".participant_withdraw_request_data_attributes_reason",
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
    "ParticipantChangeScheduleRequestData",
    "ParticipantChangeScheduleRequestDataAttributes",
    "ParticipantChangeScheduleRequestDataAttributesCourseIdentifier",
    "ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier",
    "ParticipantDeferRequestData",
    "ParticipantDeferRequestDataAttributes",
    "ParticipantDeferRequestDataAttributesCourseIdentifier",
    "ParticipantDeferRequestDataAttributesReason",
    "ParticipantResumeRequestData",
    "ParticipantResumeRequestDataAttributes",
    "ParticipantResumeRequestDataAttributesCourseIdentifier",
    "ParticipantWithdrawRequestData",
    "ParticipantWithdrawRequestDataAttributes",
    "ParticipantWithdrawRequestDataAttributesCourseIdentifier",
    "ParticipantWithdrawRequestDataAttributesReason",
]
