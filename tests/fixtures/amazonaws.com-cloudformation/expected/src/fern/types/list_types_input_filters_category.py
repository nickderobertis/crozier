

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ListTypesInputFiltersCategory(str, enum.Enum):
    """
    <p>The category of extensions to return.</p> <ul> <li> <p> <code>REGISTERED</code>: Private extensions that have been registered for this account and region.</p> </li> <li> <p> <code>ACTIVATED</code>: Public extensions that have been activated for this account and region.</p> </li> <li> <p> <code>THIRD_PARTY</code>: Extensions available for use from publishers other than Amazon. This includes:</p> <ul> <li> <p>Private extensions registered in the account.</p> </li> <li> <p>Public extensions from publishers other than Amazon, whether activated or not.</p> </li> </ul> </li> <li> <p> <code>AWS_TYPES</code>: Extensions available for use from Amazon.</p> </li> </ul>
    """

    REGISTERED = "REGISTERED"
    ACTIVATED = "ACTIVATED"
    THIRD_PARTY = "THIRD_PARTY"
    AWS_TYPES = "AWS_TYPES"

    def visit(
        self,
        registered: typing.Callable[[], T_Result],
        activated: typing.Callable[[], T_Result],
        third_party: typing.Callable[[], T_Result],
        aws_types: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListTypesInputFiltersCategory.REGISTERED:
            return registered()
        if self is ListTypesInputFiltersCategory.ACTIVATED:
            return activated()
        if self is ListTypesInputFiltersCategory.THIRD_PARTY:
            return third_party()
        if self is ListTypesInputFiltersCategory.AWS_TYPES:
            return aws_types()
