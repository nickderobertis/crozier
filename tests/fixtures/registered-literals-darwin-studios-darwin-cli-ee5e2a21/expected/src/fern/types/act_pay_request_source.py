

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ActPayRequestSource_OneTime(UniversalBaseModel):
    kind: typing.Literal["one_time"] = "one_time"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ActPayRequestSource_SavedPaymentMethod(UniversalBaseModel):
    kind: typing.Literal["saved_payment_method"] = "saved_payment_method"
    payment_method_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="paymentMethodId"), pydantic.Field(alias="paymentMethodId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ActPayRequestSource = typing_extensions.Annotated[
    typing.Union[ActPayRequestSource_OneTime, ActPayRequestSource_SavedPaymentMethod],
    pydantic.Field(discriminator="kind"),
]
