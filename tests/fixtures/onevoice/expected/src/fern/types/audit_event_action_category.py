

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuditEventActionCategory(enum.StrEnum):
    RBAC = "rbac"
    AUTH = "auth"
    INTEGRATION = "integration"
    BUSINESS = "business"
    PROJECT = "project"
    RPA = "rpa"
    PLATFORM = "platform"
    REVIEW = "review"
    HITL = "hitl"
    OTHER = "other"

    def visit(
        self,
        rbac: typing.Callable[[], T_Result],
        auth: typing.Callable[[], T_Result],
        integration: typing.Callable[[], T_Result],
        business: typing.Callable[[], T_Result],
        project: typing.Callable[[], T_Result],
        rpa: typing.Callable[[], T_Result],
        platform: typing.Callable[[], T_Result],
        review: typing.Callable[[], T_Result],
        hitl: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuditEventActionCategory.RBAC:
            return rbac()
        if self is AuditEventActionCategory.AUTH:
            return auth()
        if self is AuditEventActionCategory.INTEGRATION:
            return integration()
        if self is AuditEventActionCategory.BUSINESS:
            return business()
        if self is AuditEventActionCategory.PROJECT:
            return project()
        if self is AuditEventActionCategory.RPA:
            return rpa()
        if self is AuditEventActionCategory.PLATFORM:
            return platform()
        if self is AuditEventActionCategory.REVIEW:
            return review()
        if self is AuditEventActionCategory.HITL:
            return hitl()
        if self is AuditEventActionCategory.OTHER:
            return other()
