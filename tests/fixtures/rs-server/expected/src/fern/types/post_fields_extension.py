

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PostFieldsExtension(UniversalBaseModel):
    """
    FieldsExtension.

    Attributes:
        include: set of fields to include.
        exclude: set of fields to exclude.
    """

    include: typing.Optional[typing.List[str]] = None
    exclude: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
