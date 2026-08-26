

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VariableValue(UniversalBaseModel):
    """
    Variable value and type for variables panel.

        Attributes:
            name: Variable name.
            value: String representation of value.
            datatype: Data type as string.
    """

    datatype: typing.Optional[str] = None
    name: str
    value: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
