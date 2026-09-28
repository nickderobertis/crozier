

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class TrustRuleSuggestRequestRiskAssessment(UniversalBaseModel):
    risk: str
    reasoning: str
    reason_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="reasonDescription"), pydantic.Field(alias="reasonDescription")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
