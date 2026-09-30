

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CockroachLogicalModelField(UniversalBaseModel):
    """
    A field of a logical model
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional description of this field
    """

    name: str = pydantic.Field()
    """
    Name of the field
    """

    type: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    Type of the field
    A type used in a Logical Model field
    value with unspecified type - this is a placeholder that will eventually be replaced with a more detailed description
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
