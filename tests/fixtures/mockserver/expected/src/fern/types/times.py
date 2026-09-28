

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Times(UniversalBaseModel):
    """
    number of responses
    """

    remaining_times: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="remainingTimes"), pydantic.Field(alias="remainingTimes")
    ] = None
    unlimited: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
