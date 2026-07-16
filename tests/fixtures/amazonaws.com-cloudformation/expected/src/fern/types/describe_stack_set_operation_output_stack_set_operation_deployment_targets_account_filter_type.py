

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DescribeStackSetOperationOutputStackSetOperationDeploymentTargetsAccountFilterType(str, enum.Enum):
    """
    <p>Limit deployment targets to individual accounts or include additional accounts with provided OUs.</p> <p>The following is a list of possible values for the <code>AccountFilterType</code> operation.</p> <ul> <li> <p> <code>INTERSECTION</code>: StackSets deploys to the accounts specified in <code>Accounts</code> parameter. </p> </li> <li> <p> <code>DIFFERENCE</code>: StackSets excludes the accounts specified in <code>Accounts</code> parameter. This enables user to avoid certain accounts within an OU such as suspended accounts.</p> </li> <li> <p> <code>UNION</code>: StackSets includes additional accounts deployment targets. </p> <p>This is the default value if <code>AccountFilterType</code> is not provided. This enables user to update an entire OU and individual accounts from a different OU in one request, which used to be two separate requests.</p> </li> <li> <p> <code>NONE</code>: Deploys to all the accounts in specified organizational units (OU).</p> </li> </ul>
    """

    NONE = "NONE"
    INTERSECTION = "INTERSECTION"
    DIFFERENCE = "DIFFERENCE"
    UNION = "UNION"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        intersection: typing.Callable[[], T_Result],
        difference: typing.Callable[[], T_Result],
        union: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DescribeStackSetOperationOutputStackSetOperationDeploymentTargetsAccountFilterType.NONE:
            return none()
        if self is DescribeStackSetOperationOutputStackSetOperationDeploymentTargetsAccountFilterType.INTERSECTION:
            return intersection()
        if self is DescribeStackSetOperationOutputStackSetOperationDeploymentTargetsAccountFilterType.DIFFERENCE:
            return difference()
        if self is DescribeStackSetOperationOutputStackSetOperationDeploymentTargetsAccountFilterType.UNION:
            return union()
