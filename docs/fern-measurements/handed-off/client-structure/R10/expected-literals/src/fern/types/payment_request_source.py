

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PaymentRequestSource_Tag(UniversalBaseModel):
    kind: typing.Literal["tag"] = "tag"
    tag_id: typing_extensions.Annotated[str, FieldMetadata(alias="tagId"), pydantic.Field(alias="tagId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PaymentRequestSource_Card(UniversalBaseModel):
    kind: typing.Literal["card"] = "card"
    last4: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PaymentRequestSource = typing_extensions.Annotated[
    typing.Union[PaymentRequestSource_Tag, PaymentRequestSource_Card], pydantic.Field(discriminator="kind")
]
