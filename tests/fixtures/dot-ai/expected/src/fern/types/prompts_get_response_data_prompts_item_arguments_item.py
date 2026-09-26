

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PromptsGetResponseDataPromptsItemArgumentsItem(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Argument name
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Argument description
    """

    required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the argument is required
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
