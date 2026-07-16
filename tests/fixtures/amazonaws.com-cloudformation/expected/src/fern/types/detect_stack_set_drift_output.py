

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DetectStackSetDriftOutput(UniversalBaseModel):
    operation_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="OperationId")] = (
        pydantic.Field(default=None)
    )
    """
    <p>The ID of the drift detection stack set operation.</p> <p>You can use this operation ID with <code> <a>DescribeStackSetOperation</a> </code> to monitor the progress of the drift detection operation.</p>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
