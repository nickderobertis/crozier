

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .policy_config_policy_topics_item import PolicyConfigPolicyTopicsItem


class PolicyConfig(UniversalBaseModel):
    id: typing.Optional[str] = None
    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None
    name: str
    version: str
    description: str
    topic_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="topicDescription"), pydantic.Field(alias="topicDescription")
    ]
    config: typing.Dict[str, typing.Any]
    status: typing.Optional[str] = None
    owner: typing.Optional[str] = None
    policy_roles: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="policyRoles"), pydantic.Field(alias="policyRoles")
    ] = None
    topic_id: typing_extensions.Annotated[str, FieldMetadata(alias="topicId"), pydantic.Field(alias="topicId")]
    policy_tag: typing_extensions.Annotated[str, FieldMetadata(alias="policyTag"), pydantic.Field(alias="policyTag")]
    policy_topics: typing_extensions.Annotated[
        typing.Optional[typing.List[PolicyConfigPolicyTopicsItem]],
        FieldMetadata(alias="policyTopics"),
        pydantic.Field(alias="policyTopics"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
