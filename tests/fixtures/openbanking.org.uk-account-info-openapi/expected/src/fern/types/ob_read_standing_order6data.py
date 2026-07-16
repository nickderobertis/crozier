

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_standing_order6 import ObStandingOrder6


class ObReadStandingOrder6Data(UniversalBaseModel):
    standing_order: typing_extensions.Annotated[
        typing.Optional[typing.List[ObStandingOrder6]],
        FieldMetadata(alias="StandingOrder"),
        pydantic.Field(alias="StandingOrder"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
