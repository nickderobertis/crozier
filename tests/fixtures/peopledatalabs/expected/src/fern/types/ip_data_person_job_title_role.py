

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IpDataPersonJobTitleRole(enum.StrEnum):
    """
    A person's current job title derived role
    """

    CUSTOMER_SERVICE = "customer_service"
    DESIGN = "design"
    EDUCATION = "education"
    ENGINEERING = "engineering"
    FINANCE = "finance"
    HEALTH = "health"
    HUMAN_RESOURCES = "human_resources"
    LEGAL = "legal"
    MARKETING = "marketing"
    MEDIA = "media"
    OPERATIONS = "operations"
    PUBLIC_RELATIONS = "public_relations"
    REAL_ESTATE = "real_estate"
    SALES = "sales"
    TRADES = "trades"

    def visit(
        self,
        customer_service: typing.Callable[[], T_Result],
        design: typing.Callable[[], T_Result],
        education: typing.Callable[[], T_Result],
        engineering: typing.Callable[[], T_Result],
        finance: typing.Callable[[], T_Result],
        health: typing.Callable[[], T_Result],
        human_resources: typing.Callable[[], T_Result],
        legal: typing.Callable[[], T_Result],
        marketing: typing.Callable[[], T_Result],
        media: typing.Callable[[], T_Result],
        operations: typing.Callable[[], T_Result],
        public_relations: typing.Callable[[], T_Result],
        real_estate: typing.Callable[[], T_Result],
        sales: typing.Callable[[], T_Result],
        trades: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IpDataPersonJobTitleRole.CUSTOMER_SERVICE:
            return customer_service()
        if self is IpDataPersonJobTitleRole.DESIGN:
            return design()
        if self is IpDataPersonJobTitleRole.EDUCATION:
            return education()
        if self is IpDataPersonJobTitleRole.ENGINEERING:
            return engineering()
        if self is IpDataPersonJobTitleRole.FINANCE:
            return finance()
        if self is IpDataPersonJobTitleRole.HEALTH:
            return health()
        if self is IpDataPersonJobTitleRole.HUMAN_RESOURCES:
            return human_resources()
        if self is IpDataPersonJobTitleRole.LEGAL:
            return legal()
        if self is IpDataPersonJobTitleRole.MARKETING:
            return marketing()
        if self is IpDataPersonJobTitleRole.MEDIA:
            return media()
        if self is IpDataPersonJobTitleRole.OPERATIONS:
            return operations()
        if self is IpDataPersonJobTitleRole.PUBLIC_RELATIONS:
            return public_relations()
        if self is IpDataPersonJobTitleRole.REAL_ESTATE:
            return real_estate()
        if self is IpDataPersonJobTitleRole.SALES:
            return sales()
        if self is IpDataPersonJobTitleRole.TRADES:
            return trades()
