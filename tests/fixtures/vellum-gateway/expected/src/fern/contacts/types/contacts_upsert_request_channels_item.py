

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class ContactsUpsertRequestChannelsItem(UniversalBaseModel):
    type: str
    address: str
    is_primary: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isPrimary"), pydantic.Field(alias="isPrimary")
    ] = None
    external_chat_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="externalChatId"),
        pydantic.Field(
            alias="externalChatId",
            description="Delivery chat id. Omit to preserve the stored value. A legacy explicit null is accepted for compatibility and treated as omitted; clearing is not supported (a stored null is indistinguishable from never-learned, so no consumer could tell a clear from a gap).",
        ),
    ] = None
    """
    Delivery chat id. Omit to preserve the stored value. A legacy explicit null is accepted for compatibility and treated as omitted; clearing is not supported (a stored null is indistinguishable from never-learned, so no consumer could tell a clear from a gap).
    """

    status: typing.Optional[str] = None
    policy: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
