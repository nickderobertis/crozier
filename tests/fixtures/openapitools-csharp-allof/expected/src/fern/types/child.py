

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Child(UniversalBaseModel):
    age: typing.Optional[int] = None
    booster_seat: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="boosterSeat"), pydantic.Field(alias="boosterSeat")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
