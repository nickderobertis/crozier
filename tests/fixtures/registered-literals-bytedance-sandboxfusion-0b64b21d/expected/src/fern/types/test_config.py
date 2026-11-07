

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .test_config_language import TestConfigLanguage
from .test_config_provided_data import TestConfigProvidedData


class TestConfig(UniversalBaseModel):
    """
    custom_extract_logic: a piece of python code that calls `submit_code_blocks(cbs)` to extract custom code
                          cbs: List[CodeBlock], CodeBlock(priority=40, code='xxx', language='xxx')
                          priority: fenced = 30, incomplete fenced = 20, heuristic = 10
    """

    dataset_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    the dataset class used to process, only works when the dataset id is not registered.
    """

    language: typing.Optional[TestConfigLanguage] = None
    locale: typing.Optional[str] = None
    is_fewshot: typing.Optional[bool] = None
    compile_timeout: typing.Optional[float] = None
    run_timeout: typing.Optional[float] = None
    custom_extract_logic: typing.Optional[str] = None
    provided_data: typing.Optional[TestConfigProvidedData] = None
    extra: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
