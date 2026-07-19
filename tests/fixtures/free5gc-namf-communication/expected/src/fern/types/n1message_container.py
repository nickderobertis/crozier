

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .n1message_class import N1MessageClass
from .ref_to_binary_data import RefToBinaryData


class N1MessageContainer(UniversalBaseModel):
    n1message_class: typing_extensions.Annotated[
        N1MessageClass, FieldMetadata(alias="n1MessageClass"), pydantic.Field(alias="n1MessageClass")
    ]
    n1message_content: typing_extensions.Annotated[
        RefToBinaryData, FieldMetadata(alias="n1MessageContent"), pydantic.Field(alias="n1MessageContent")
    ]
    nf_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nfId"), pydantic.Field(alias="nfId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
