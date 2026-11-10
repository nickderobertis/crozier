

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OwnershipType(enum.StrEnum):
    """
    How an asset is owned.

    `association`: Ownership by a corporation, partnership, or unincorporated association, including for-profit and not-for-profit organizations.
    `individual`: Ownership by an individual.
    `joint`: Joint ownership by multiple parties.
    `trust`: Ownership by a revocable or irrevocable trust.
    """

    INDIVIDUAL = "individual"
    JOINT = "joint"
    ASSOCIATION = "association"
    TRUST = "trust"

    def visit(
        self,
        individual: typing.Callable[[], T_Result],
        joint: typing.Callable[[], T_Result],
        association: typing.Callable[[], T_Result],
        trust: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OwnershipType.INDIVIDUAL:
            return individual()
        if self is OwnershipType.JOINT:
            return joint()
        if self is OwnershipType.ASSOCIATION:
            return association()
        if self is OwnershipType.TRUST:
            return trust()
