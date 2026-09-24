

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ui_filter_model_operator import UiFilterModelOperator


class UiFilterModel(UniversalBaseModel):
    """
    Model for UIFilter
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name
    """

    operator: typing.Optional[UiFilterModelOperator] = pydantic.Field(default=None)
    """
    Operator
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    Value
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
