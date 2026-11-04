

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cloud_environment_state import CloudEnvironmentState
from .environment_billing_info import EnvironmentBillingInfo


class EnvironmentStateChange(UniversalBaseModel):
    environment: typing.Optional[EnvironmentBillingInfo] = None
    id: typing.Optional[str] = None
    new_value: typing_extensions.Annotated[
        typing.Optional[CloudEnvironmentState], FieldMetadata(alias="newValue"), pydantic.Field(alias="newValue")
    ] = None
    old_value: typing_extensions.Annotated[
        typing.Optional[CloudEnvironmentState], FieldMetadata(alias="oldValue"), pydantic.Field(alias="oldValue")
    ] = None
    partition_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="partitionKey"), pydantic.Field(alias="partitionKey")
    ] = None
    time: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
