

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Link(UniversalBaseModel):
    """
    Details of a link to a related resource.
    """

    rel: typing.Optional[str] = pydantic.Field(default=None)
    """
    Relation of the linked resource to the current resource.
    """

    href: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL for accessing the related resource.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Media type of the linked resource.
    """

    min_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Minimum amount allowed for a refund, in major units.
    """

    max_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Maximum amount allowed for a refund, in major units.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
