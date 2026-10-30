

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .config_disable_registration import ConfigDisableRegistration
from .config_total import ConfigTotal
from .config_user import ConfigUser


class Config(UniversalBaseModel):
    max_users: typing_extensions.Annotated[float, FieldMetadata(alias="maxUsers"), pydantic.Field(alias="maxUsers")]
    disable_registration: typing_extensions.Annotated[
        ConfigDisableRegistration,
        FieldMetadata(alias="disableRegistration"),
        pydantic.Field(alias="disableRegistration"),
    ]
    total: ConfigTotal
    user: ConfigUser

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
