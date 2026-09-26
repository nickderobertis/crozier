

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V2RunColumnData(UniversalBaseModel):
    """
    Acknowledgement for a table column run.
    """

    dispatch_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="dispatchId"),
        pydantic.Field(
            alias="dispatchId",
            description="Run dispatch ID, or null when no dispatch is available to poll. Use row reads with `includeRunState` to check cell outcomes.",
        ),
    ] = None
    """
    Run dispatch ID, or null when no dispatch is available to poll. Use row reads with `includeRunState` to check cell outcomes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
