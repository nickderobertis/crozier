

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PolicyDto(UniversalBaseModel):
    id: typing_extensions.Annotated[str, FieldMetadata(alias="_id"), pydantic.Field(alias="_id")]
    create_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createDate"), pydantic.Field(alias="createDate")
    ]
    uuid_: typing_extensions.Annotated[str, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")]
    name: str
    description: str
    status: str
    creator: str
    owner: str
    topic_id: typing_extensions.Annotated[str, FieldMetadata(alias="topicId"), pydantic.Field(alias="topicId")]
    policy_tag: typing_extensions.Annotated[str, FieldMetadata(alias="policyTag"), pydantic.Field(alias="policyTag")]
    code_version: typing_extensions.Annotated[
        str, FieldMetadata(alias="codeVersion"), pydantic.Field(alias="codeVersion")
    ]
    user_roles: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="userRoles"), pydantic.Field(alias="userRoles")
    ]
    user_groups: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="userGroups"), pydantic.Field(alias="userGroups")
    ]
    user_role: typing_extensions.Annotated[str, FieldMetadata(alias="userRole"), pydantic.Field(alias="userRole")]
    user_group: typing_extensions.Annotated[str, FieldMetadata(alias="userGroup"), pydantic.Field(alias="userGroup")]
    id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
