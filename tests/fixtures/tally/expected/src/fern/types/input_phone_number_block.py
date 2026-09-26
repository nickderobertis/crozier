

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .block_uuid import BlockUuid
from .group_uuid import GroupUuid
from .input_phone_number_block_group_type import InputPhoneNumberBlockGroupType
from .input_phone_number_payload import InputPhoneNumberPayload


class InputPhoneNumberBlock(UniversalBaseModel):
    """
    A block with type INPUT_PHONE_NUMBER. Used for phone number input.
    """

    uuid_: typing_extensions.Annotated[BlockUuid, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")]
    group_uuid: typing_extensions.Annotated[
        GroupUuid, FieldMetadata(alias="groupUuid"), pydantic.Field(alias="groupUuid")
    ]
    group_type: typing_extensions.Annotated[
        InputPhoneNumberBlockGroupType, FieldMetadata(alias="groupType"), pydantic.Field(alias="groupType")
    ]
    payload: InputPhoneNumberPayload

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
