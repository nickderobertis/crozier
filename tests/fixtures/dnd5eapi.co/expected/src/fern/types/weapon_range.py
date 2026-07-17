

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class WeaponRange(UniversalBaseModel):
    long_: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="long"),
        pydantic.Field(alias="long", description="The weapon's long range in feet."),
    ] = None
    """
    The weapon's long range in feet.
    """

    normal: typing.Optional[float] = pydantic.Field(default=None)
    """
    The weapon's normal range in feet.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
