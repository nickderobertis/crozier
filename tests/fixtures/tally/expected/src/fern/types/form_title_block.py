

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .block_uuid import BlockUuid
from .form_title_block_group_type import FormTitleBlockGroupType
from .form_title_payload import FormTitlePayload
from .group_uuid import GroupUuid


class FormTitleBlock(UniversalBaseModel):
    """
    A block with type FORM_TITLE. Used for the main form title with optional logo and cover image.
    """

    uuid_: typing_extensions.Annotated[BlockUuid, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")]
    group_uuid: typing_extensions.Annotated[
        GroupUuid, FieldMetadata(alias="groupUuid"), pydantic.Field(alias="groupUuid")
    ]
    group_type: typing_extensions.Annotated[
        FormTitleBlockGroupType, FieldMetadata(alias="groupType"), pydantic.Field(alias="groupType")
    ]
    payload: FormTitlePayload

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
