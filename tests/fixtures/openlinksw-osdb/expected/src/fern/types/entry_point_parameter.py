

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entry_point_parameter_type import EntryPointParameterType


class EntryPointParameter(UniversalBaseModel):
    description: str = pydantic.Field()
    """
    A short description of the parameter for use in the OSDB Action Console. Optional - may be null.
    """

    display_name: str = pydantic.Field()
    """
    The parameter's display name in the OSDB Action Console. Optional - may be null.
    """

    parameter_name: str = pydantic.Field()
    """
    The parameter name as present in the HTTP request. e.g. the key name in a query string key-value pair.
    """

    permitted_values: typing.List[str] = pydantic.Field()
    """
    If the parameter accepts only a limited set of values, the allowed set of values. Null if not applicable.
    """

    required: int = pydantic.Field()
    """
    A flag indicating if the parameter is optional.
    """

    type: EntryPointParameterType = pydantic.Field()
    """
    The type of the parameter, indicating its location in the HTTP request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
