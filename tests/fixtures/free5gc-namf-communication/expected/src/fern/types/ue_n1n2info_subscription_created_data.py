

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UeN1N2InfoSubscriptionCreatedData(UniversalBaseModel):
    n1n2notify_subscription_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="n1n2NotifySubscriptionId"), pydantic.Field(alias="n1n2NotifySubscriptionId")
    ]
    supported_features: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="supportedFeatures"), pydantic.Field(alias="supportedFeatures")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
