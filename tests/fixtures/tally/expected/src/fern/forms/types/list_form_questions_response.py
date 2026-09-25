

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.question import Question


class ListFormQuestionsResponse(UniversalBaseModel):
    questions: typing.Optional[typing.List[Question]] = None
    has_responses: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hasResponses"), pydantic.Field(alias="hasResponses")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
