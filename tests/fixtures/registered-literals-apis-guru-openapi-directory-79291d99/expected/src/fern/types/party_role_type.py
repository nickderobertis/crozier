

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PartyRoleType(enum.StrEnum):
    """
    A value from a MISMO defined list that identifies the role that the party plays in the transaction. Parties may be either a person or legal entity. A party may play multiple roles in a transaction.A value from a MISMO defined list that identifies the role that the party plays in the transaction. Parties may be either a person or legal entity. A party may play multiple roles in a transaction.
    """

    BORROWER = "Borrower"

    def visit(self, borrower: typing.Callable[[], T_Result]) -> T_Result:
        if self is PartyRoleType.BORROWER:
            return borrower()
