

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ProvisioningApiUserDetailsBackendCapabilities(UniversalBaseModel):
    set_display_name: typing_extensions.Annotated[
        bool, FieldMetadata(alias="setDisplayName"), pydantic.Field(alias="setDisplayName")
    ]
    set_password: typing_extensions.Annotated[
        bool, FieldMetadata(alias="setPassword"), pydantic.Field(alias="setPassword")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
