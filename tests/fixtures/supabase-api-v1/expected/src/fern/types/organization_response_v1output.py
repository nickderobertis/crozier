

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OrganizationResponseV1Output(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Deprecated: Use `slug` instead.
    """

    slug: str = pydantic.Field()
    """
    Organization slug
    """

    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
