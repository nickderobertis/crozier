

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NonDynamic5Qi(UniversalBaseModel):
    priority_level: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="priorityLevel"), pydantic.Field(alias="priorityLevel")
    ] = None
    aver_window: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="averWindow"), pydantic.Field(alias="averWindow")
    ] = None
    max_data_burst_vol: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxDataBurstVol"), pydantic.Field(alias="maxDataBurstVol")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
