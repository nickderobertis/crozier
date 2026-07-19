

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .n1message_container import N1MessageContainer
from .registration_context_container import RegistrationContextContainer


class N1MessageNotification(UniversalBaseModel):
    n1notify_subscription_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="n1NotifySubscriptionId"),
        pydantic.Field(alias="n1NotifySubscriptionId"),
    ] = None
    n1message_container: typing_extensions.Annotated[
        N1MessageContainer, FieldMetadata(alias="n1MessageContainer"), pydantic.Field(alias="n1MessageContainer")
    ]
    lcs_correlation_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lcsCorrelationId"), pydantic.Field(alias="lcsCorrelationId")
    ] = None
    registration_ctxt_container: typing_extensions.Annotated[
        typing.Optional[RegistrationContextContainer],
        FieldMetadata(alias="registrationCtxtContainer"),
        pydantic.Field(alias="registrationCtxtContainer"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
