

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .abstract_bin_grid import AbstractBinGrid
from .max_mis_location import MaxMisLocation


class ConvertBinGridResponse(UniversalBaseModel):
    applied_operations: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="AppliedOperations"),
        pydantic.Field(alias="AppliedOperations"),
    ] = None
    max_mis_location: typing_extensions.Annotated[
        typing.Optional[MaxMisLocation], FieldMetadata(alias="maxMisLocation"), pydantic.Field(alias="maxMisLocation")
    ] = None
    out_bin_grid: typing_extensions.Annotated[
        typing.Optional[AbstractBinGrid], FieldMetadata(alias="outBinGrid"), pydantic.Field(alias="outBinGrid")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
