

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ListTypesInputVisibility(str, enum.Enum):
    """
    <p>The scope at which the extensions are visible and usable in CloudFormation operations.</p> <p>Valid values include:</p> <ul> <li> <p> <code>PRIVATE</code>: Extensions that are visible and usable within this account and region. This includes:</p> <ul> <li> <p>Private extensions you have registered in this account and region.</p> </li> <li> <p>Public extensions that you have activated in this account and region.</p> </li> </ul> </li> <li> <p> <code>PUBLIC</code>: Extensions that are publicly visible and available to be activated within any Amazon Web Services account. This includes extensions from Amazon Web Services, in addition to third-party publishers.</p> </li> </ul> <p>The default is <code>PRIVATE</code>.</p>
    """

    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"

    def visit(self, public: typing.Callable[[], T_Result], private: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListTypesInputVisibility.PUBLIC:
            return public()
        if self is ListTypesInputVisibility.PRIVATE:
            return private()
