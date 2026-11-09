

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .org_token_id import OrgTokenId
from .org_token_name import OrgTokenName
from .org_token_status import OrgTokenStatus


class OrgToken(UniversalBaseModel):
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    last_four_chars_of_key: typing_extensions.Annotated[
        str, FieldMetadata(alias="lastFourCharsOfKey"), pydantic.Field(alias="lastFourCharsOfKey")
    ]
    status: OrgTokenStatus
    name: OrgTokenName
    org_id: typing_extensions.Annotated[str, FieldMetadata(alias="orgId"), pydantic.Field(alias="orgId")]
    org_token_id: typing_extensions.Annotated[
        OrgTokenId, FieldMetadata(alias="orgTokenId"), pydantic.Field(alias="orgTokenId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
