

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .block_uuid import BlockUuid
from .group_uuid import GroupUuid
from .respondent_country_block_group_type import RespondentCountryBlockGroupType
from .respondent_country_payload import RespondentCountryPayload


class RespondentCountryBlock(UniversalBaseModel):
    """
    A block with type RESPONDENT_COUNTRY. Used for capturing respondent location.
    """

    uuid_: typing_extensions.Annotated[BlockUuid, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")]
    group_uuid: typing_extensions.Annotated[
        GroupUuid, FieldMetadata(alias="groupUuid"), pydantic.Field(alias="groupUuid")
    ]
    group_type: typing_extensions.Annotated[
        RespondentCountryBlockGroupType, FieldMetadata(alias="groupType"), pydantic.Field(alias="groupType")
    ]
    payload: RespondentCountryPayload

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
