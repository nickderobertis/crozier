

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetDigitalFilterTypeSupportListResponseDigitalFilterTypesItem(UniversalBaseModel):
    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    Index of the digital filter type
    """

    args: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of arguments to set this filter type
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the digital filter type
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
