

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .extra_link import ExtraLink


class ExtraLinkCollection(UniversalBaseModel):
    """
    The collection of extra links.
    """

    extra_links: typing.Optional[typing.List[ExtraLink]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
