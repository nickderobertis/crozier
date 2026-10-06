

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .hal_link_method import HalLinkMethod


class HalLink(UniversalBaseModel):
    """
    A link target in a HAL response.
    """

    href: str = pydantic.Field()
    """
    Target url for this link.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of the resource referenced by this link.
    """

    method: typing.Optional[HalLinkMethod] = pydantic.Field(default=None)
    """
    Http method required to resolve the link.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
