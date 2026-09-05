

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostPositionsRequestPosition(enum.StrEnum):
    EXECUTIVE_MANAGEMENT_C_LEVEL = "Executive Management (C-level)"
    VP_LEVEL_EXECUTIVE = "VP-level Executive"
    MANAGER_DIRECTOR_SUPERVISOR = "Manager / Director / Supervisor"
    SYSTEMS_DEVELOPMENT = "Systems Development"
    SOFTWARE_DEVELOPMENT = "Software Development"
    WEB_DEVELOPER = "Web Developer"
    IT_CONSULTANT = "IT Consultant"
    TECHNICAL_SUPPORT = "Technical Support"
    SALES = "Sales"
    OTHER_TECHNOLOGY_RELATED = "Other technology related"
    OTHER_NON_TECHNOLOGY_RELATED = "Other non-technology related"
    STUDENT = "Student"
    RETIRED = "Retired"

    def visit(
        self,
        executive_management_c_level: typing.Callable[[], T_Result],
        vp_level_executive: typing.Callable[[], T_Result],
        manager_director_supervisor: typing.Callable[[], T_Result],
        systems_development: typing.Callable[[], T_Result],
        software_development: typing.Callable[[], T_Result],
        web_developer: typing.Callable[[], T_Result],
        it_consultant: typing.Callable[[], T_Result],
        technical_support: typing.Callable[[], T_Result],
        sales: typing.Callable[[], T_Result],
        other_technology_related: typing.Callable[[], T_Result],
        other_non_technology_related: typing.Callable[[], T_Result],
        student: typing.Callable[[], T_Result],
        retired: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostPositionsRequestPosition.EXECUTIVE_MANAGEMENT_C_LEVEL:
            return executive_management_c_level()
        if self is PostPositionsRequestPosition.VP_LEVEL_EXECUTIVE:
            return vp_level_executive()
        if self is PostPositionsRequestPosition.MANAGER_DIRECTOR_SUPERVISOR:
            return manager_director_supervisor()
        if self is PostPositionsRequestPosition.SYSTEMS_DEVELOPMENT:
            return systems_development()
        if self is PostPositionsRequestPosition.SOFTWARE_DEVELOPMENT:
            return software_development()
        if self is PostPositionsRequestPosition.WEB_DEVELOPER:
            return web_developer()
        if self is PostPositionsRequestPosition.IT_CONSULTANT:
            return it_consultant()
        if self is PostPositionsRequestPosition.TECHNICAL_SUPPORT:
            return technical_support()
        if self is PostPositionsRequestPosition.SALES:
            return sales()
        if self is PostPositionsRequestPosition.OTHER_TECHNOLOGY_RELATED:
            return other_technology_related()
        if self is PostPositionsRequestPosition.OTHER_NON_TECHNOLOGY_RELATED:
            return other_non_technology_related()
        if self is PostPositionsRequestPosition.STUDENT:
            return student()
        if self is PostPositionsRequestPosition.RETIRED:
            return retired()
