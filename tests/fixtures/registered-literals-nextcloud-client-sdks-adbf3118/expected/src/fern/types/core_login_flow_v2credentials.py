

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CoreLoginFlowV2Credentials(UniversalBaseModel):
    server: str
    login_name: typing_extensions.Annotated[str, FieldMetadata(alias="loginName"), pydantic.Field(alias="loginName")]
    app_password: typing_extensions.Annotated[
        str, FieldMetadata(alias="appPassword"), pydantic.Field(alias="appPassword")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
