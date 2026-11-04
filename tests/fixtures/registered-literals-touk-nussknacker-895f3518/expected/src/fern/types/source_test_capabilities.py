

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .capability_status_t import CapabilityStatusT


class SourceTestCapabilities(UniversalBaseModel):
    test_with_parameters: typing_extensions.Annotated[
        CapabilityStatusT, FieldMetadata(alias="testWithParameters"), pydantic.Field(alias="testWithParameters")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
