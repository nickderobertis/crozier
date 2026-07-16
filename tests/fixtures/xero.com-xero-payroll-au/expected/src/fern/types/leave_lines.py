

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .leave_line import LeaveLine


class LeaveLines(UniversalBaseModel):
    """
    The leave type lines
    """

    employee: typing_extensions.Annotated[
        typing.Optional[typing.List[LeaveLine]], FieldMetadata(alias="Employee"), pydantic.Field(alias="Employee")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
