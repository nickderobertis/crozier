

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .a2a_data_part import A2ADataPart
from .a2a_message_role import A2AMessageRole


class A2AMessage(UniversalBaseModel):
    """
    A2A v1.0 Message envelope. `messageId` is required on every Message; `role` is the protobuf enum string `ROLE_USER` (buyer agent) or `ROLE_AGENT` (dealer agent). Parts identify their kind by the member they carry — `data` for DataParts (no `kind` discriminator).
    """

    message_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="messageId"),
        pydantic.Field(alias="messageId", description="Unique identifier for this message (e.g. ULID or UUID)."),
    ]
    """
    Unique identifier for this message (e.g. ULID or UUID).
    """

    role: A2AMessageRole
    parts: typing.List[A2ADataPart]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
