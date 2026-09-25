

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class A2AMessageRequestConfiguration(UniversalBaseModel):
    accepted_output_modes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="acceptedOutputModes"),
        pydantic.Field(alias="acceptedOutputModes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
