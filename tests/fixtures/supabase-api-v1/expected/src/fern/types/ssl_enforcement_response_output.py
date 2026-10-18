

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ssl_enforcement_response_output_current_config import SslEnforcementResponseOutputCurrentConfig


class SslEnforcementResponseOutput(UniversalBaseModel):
    current_config: typing_extensions.Annotated[
        SslEnforcementResponseOutputCurrentConfig,
        FieldMetadata(alias="currentConfig"),
        pydantic.Field(alias="currentConfig"),
    ]
    applied_successfully: typing_extensions.Annotated[
        bool, FieldMetadata(alias="appliedSuccessfully"), pydantic.Field(alias="appliedSuccessfully")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
