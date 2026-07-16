

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stack_drift_information_summary_stack_drift_status import StackDriftInformationSummaryStackDriftStatus


class StackDriftInformationSummary(UniversalBaseModel):
    """
    Contains information about whether the stack's actual configuration differs, or has <i>drifted</i>, from its expected configuration, as defined in the stack template and any values specified as template parameters. A stack is considered to have drifted if one or more of its resources have drifted.
    """

    stack_drift_status: typing_extensions.Annotated[
        StackDriftInformationSummaryStackDriftStatus, FieldMetadata(alias="StackDriftStatus")
    ] = pydantic.Field()
    """
    <p>Status of the stack's actual configuration compared to its expected template configuration.</p> <ul> <li> <p> <code>DRIFTED</code>: The stack differs from its expected template configuration. A stack is considered to have drifted if one or more of its resources have drifted.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation hasn't checked if the stack differs from its expected template configuration.</p> </li> <li> <p> <code>IN_SYNC</code>: The stack's actual configuration matches its expected template configuration.</p> </li> <li> <p> <code>UNKNOWN</code>: This value is reserved for future use.</p> </li> </ul>
    """

    last_check_timestamp: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="LastCheckTimestamp")
    ] = pydantic.Field(default=None)
    """
    Most recent time when a drift detection operation was initiated on the stack, or any of its individual resources that support drift detection.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
