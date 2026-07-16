

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DescribeStackSetOutputStackSetManagedExecution(UniversalBaseModel):
    """
    Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.
    """

    active: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="Active")] = pydantic.Field(
        default=None
    )
    """
    <p>When <code>true</code>, StackSets performs non-conflicting operations concurrently and queues conflicting operations. After conflicting operations finish, StackSets starts queued operations in request order.</p> <note> <p>If there are already running or queued operations, StackSets queues all incoming operations even if they are non-conflicting.</p> <p>You can't modify your stack set's execution configuration while there are running or queued operations for that stack set.</p> </note> <p>When <code>false</code> (default), StackSets performs one operation at a time in request order.</p>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
