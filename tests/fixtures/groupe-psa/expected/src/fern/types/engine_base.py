

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .engine_base_extension import EngineBaseExtension
from .engine_base_gmp_status import EngineBaseGmpStatus
from .engine_base_type import EngineBaseType


class EngineBase(UniversalBaseModel):
    type: typing.Optional[EngineBaseType] = None
    speed: typing.Optional[float] = pydantic.Field(default=None)
    """
    Engine's speed in RPM
    """

    gmp_status: typing_extensions.Annotated[
        typing.Optional[EngineBaseGmpStatus], FieldMetadata(alias="gmpStatus"), pydantic.Field(alias="gmpStatus")
    ] = None
    extension: typing.Optional[EngineBaseExtension] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
