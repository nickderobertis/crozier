

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchUsersRequestGoalsItem(enum.StrEnum):
    FIND_BUSINESS_PARTNERSHIPS = "Find business partnerships"
    FIND_PROSPECTIVE_CLIENTS = "Find prospective clients"
    HIRE_EMPLOYEES = "Hire employees"
    FIND_A_JOB = "Find a job"
    FIND_A_CO_FOUNDER = "Find a co-founder"
    RECEIVE_MENTORSHIP_FROM_OTHERS = "Receive mentorship from others"
    MENTOR_OTHERS = "Mentor others"

    def visit(
        self,
        find_business_partnerships: typing.Callable[[], T_Result],
        find_prospective_clients: typing.Callable[[], T_Result],
        hire_employees: typing.Callable[[], T_Result],
        find_a_job: typing.Callable[[], T_Result],
        find_a_co_founder: typing.Callable[[], T_Result],
        receive_mentorship_from_others: typing.Callable[[], T_Result],
        mentor_others: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PatchUsersRequestGoalsItem.FIND_BUSINESS_PARTNERSHIPS:
            return find_business_partnerships()
        if self is PatchUsersRequestGoalsItem.FIND_PROSPECTIVE_CLIENTS:
            return find_prospective_clients()
        if self is PatchUsersRequestGoalsItem.HIRE_EMPLOYEES:
            return hire_employees()
        if self is PatchUsersRequestGoalsItem.FIND_A_JOB:
            return find_a_job()
        if self is PatchUsersRequestGoalsItem.FIND_A_CO_FOUNDER:
            return find_a_co_founder()
        if self is PatchUsersRequestGoalsItem.RECEIVE_MENTORSHIP_FROM_OTHERS:
            return receive_mentorship_from_others()
        if self is PatchUsersRequestGoalsItem.MENTOR_OTHERS:
            return mentor_others()
