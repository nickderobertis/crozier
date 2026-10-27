

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ChatMessagePolicyViolationPolicyTip(UniversalBaseModel):
    general_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="generalText"), pydantic.Field(alias="generalText")
    ] = None
    compliance_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="complianceUrl"), pydantic.Field(alias="complianceUrl")
    ] = None
    matched_condition_descriptions: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="matchedConditionDescriptions"),
        pydantic.Field(alias="matchedConditionDescriptions"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
