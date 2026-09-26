

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ignored_parameters_unsupported import IgnoredParametersUnsupported
from .json_success_base_result import JsonSuccessBaseResult


class JsonSuccessBase(UniversalBaseModel):
    """
    **Changes**: As of Zulip 7.0 (feature level 167), if any
    parameters sent in the request are not supported by this
    endpoint, a successful JSON response will include an
    [`ignored_parameters_unsupported`][ignored_params] array.

    A typical successful JSON response may look like:

    [ignored_params]: /api/rest-error-handling#ignored-parameters
    """

    result: JsonSuccessBaseResult
    msg: str
    ignored_parameters_unsupported: typing.Optional[IgnoredParametersUnsupported] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
