

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TransmissionGearboxMode(UniversalBaseModel):
    automatic: typing.Optional[bool] = None
    sport: typing.Optional[bool] = None
    snow: typing.Optional[bool] = None
    sequential: typing.Optional[bool] = None
    semi_manual: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="semiManual"), pydantic.Field(alias="semiManual")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
