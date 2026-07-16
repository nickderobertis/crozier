

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .links import Links
from .meta import Meta
from .ob_read_standing_order6data import ObReadStandingOrder6Data


class ObReadStandingOrder6(UniversalBaseModel):
    data: typing_extensions.Annotated[ObReadStandingOrder6Data, FieldMetadata(alias="Data")]
    links: typing_extensions.Annotated[typing.Optional[Links], FieldMetadata(alias="Links")] = None
    meta: typing_extensions.Annotated[typing.Optional[Meta], FieldMetadata(alias="Meta")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
