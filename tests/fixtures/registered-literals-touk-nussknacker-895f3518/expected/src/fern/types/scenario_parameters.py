

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ScenarioParameters(UniversalBaseModel):
    processing_mode: typing_extensions.Annotated[
        str, FieldMetadata(alias="processingMode"), pydantic.Field(alias="processingMode")
    ]
    category: str
    engine_setup_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="engineSetupName"), pydantic.Field(alias="engineSetupName")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
