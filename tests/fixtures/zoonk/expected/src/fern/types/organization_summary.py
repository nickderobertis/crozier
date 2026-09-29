

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OrganizationSummary(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Organization ID
    """

    logo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Organization logo URL
    """

    name: str = pydantic.Field()
    """
    Organization name
    """

    slug: str = pydantic.Field()
    """
    Organization slug
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
