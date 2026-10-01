

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .explicit_grid import ExplicitGrid
from .inferred_any_grid import InferredAnyGrid
from .inferred_grid import InferredGrid
from .inherited_grid import InheritedGrid
from .pet import Pet


class Grids(UniversalBaseModel):
    explicit: typing.Optional[ExplicitGrid] = None
    inferred: typing.Optional[InferredGrid] = None
    inferred_any: typing_extensions.Annotated[
        typing.Optional[InferredAnyGrid], FieldMetadata(alias="inferredAny"), pydantic.Field(alias="inferredAny")
    ] = None
    inherited: typing.Optional[InheritedGrid] = None
    pet: typing.Optional[Pet] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
