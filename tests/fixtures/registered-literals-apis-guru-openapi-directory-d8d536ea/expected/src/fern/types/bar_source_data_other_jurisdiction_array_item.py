

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BarSourceDataOtherJurisdictionArrayItem(UniversalBaseModel):
    bar_number: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="barNumber"), pydantic.Field(alias="barNumber")
    ] = None
    state: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
