

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BarRecordPreview(UniversalBaseModel):
    bar_number: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="barNumber"), pydantic.Field(alias="barNumber")
    ] = None
    bar_source_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="barSourceType"), pydantic.Field(alias="barSourceType")
    ] = None
    object: str
    state_code: typing_extensions.Annotated[str, FieldMetadata(alias="stateCode"), pydantic.Field(alias="stateCode")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
