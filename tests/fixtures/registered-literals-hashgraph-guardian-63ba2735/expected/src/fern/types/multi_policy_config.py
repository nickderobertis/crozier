

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MultiPolicyConfig(UniversalBaseModel):
    id: typing.Optional[str] = None
    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None
    owner: typing.Optional[str] = None
    type: typing.Optional[str] = None
    instance_topic_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="instanceTopicId"), pydantic.Field(alias="instanceTopicId")
    ] = None
    main_policy_topic_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mainPolicyTopicId"), pydantic.Field(alias="mainPolicyTopicId")
    ] = None
    synchronization_topic_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="synchronizationTopicId"),
        pydantic.Field(alias="synchronizationTopicId"),
    ] = None
    policy_owner: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="policyOwner"), pydantic.Field(alias="policyOwner")
    ] = None
    user: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
