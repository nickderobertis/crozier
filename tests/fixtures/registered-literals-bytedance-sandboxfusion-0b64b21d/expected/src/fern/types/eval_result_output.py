

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .eval_result_output_extracted_type import EvalResultOutputExtractedType
from .eval_result_output_id import EvalResultOutputId
from .eval_test_case_output import EvalTestCaseOutput


class EvalResultOutput(UniversalBaseModel):
    id: EvalResultOutputId
    accepted: bool
    extracted_code: str
    full_code: typing.Optional[str] = None
    test_code: typing.Optional[str] = None
    tests: typing.List[EvalTestCaseOutput]
    extracted_type: typing.Optional[EvalResultOutputExtractedType] = None
    extra: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
