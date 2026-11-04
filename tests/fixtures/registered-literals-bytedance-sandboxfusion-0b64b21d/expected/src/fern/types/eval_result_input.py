

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .eval_result_input_extracted_type import EvalResultInputExtractedType
from .eval_result_input_id import EvalResultInputId
from .eval_test_case_input import EvalTestCaseInput


class EvalResultInput(UniversalBaseModel):
    id: EvalResultInputId
    accepted: bool
    extracted_code: str
    full_code: typing.Optional[str] = None
    test_code: typing.Optional[str] = None
    tests: typing.List[EvalTestCaseInput]
    extracted_type: typing.Optional[EvalResultInputExtractedType] = None
    extra: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
