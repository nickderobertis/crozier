

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ActivateTypeInputVersionBump(str, enum.Enum):
    """
    <p>Manually updates a previously-activated type to a new major or minor version, if available. You can also use this parameter to update the value of <code>AutoUpdate</code>.</p> <ul> <li> <p> <code>MAJOR</code>: CloudFormation updates the extension to the newest major version, if one is available.</p> </li> <li> <p> <code>MINOR</code>: CloudFormation updates the extension to the newest minor version, if one is available.</p> </li> </ul>
    """

    MAJOR = "MAJOR"
    MINOR = "MINOR"

    def visit(self, major: typing.Callable[[], T_Result], minor: typing.Callable[[], T_Result]) -> T_Result:
        if self is ActivateTypeInputVersionBump.MAJOR:
            return major()
        if self is ActivateTypeInputVersionBump.MINOR:
            return minor()
