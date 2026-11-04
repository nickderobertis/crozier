

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .prebuild_environment_options import PrebuildEnvironmentOptions
from .secret_data_body import SecretDataBody


class CreateEnvironmentPoolResourceBody(UniversalBaseModel):
    environment_options: typing_extensions.Annotated[
        typing.Optional[PrebuildEnvironmentOptions],
        FieldMetadata(alias="environmentOptions"),
        pydantic.Field(alias="environmentOptions"),
    ] = None
    secrets: typing.Optional[typing.List[SecretDataBody]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
