

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class WizardConfigPolicy(UniversalBaseModel):
    name: typing.Optional[str] = None
    description: typing.Optional[str] = None
    topic_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="topicDescription"), pydantic.Field(alias="topicDescription")
    ] = None
    policy_tag: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="policyTag"), pydantic.Field(alias="policyTag")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
