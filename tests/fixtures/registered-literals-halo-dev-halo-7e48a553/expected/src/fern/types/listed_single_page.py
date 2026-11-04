

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .contributor import Contributor
from .single_page import SinglePage
from .stats import Stats


class ListedSinglePage(UniversalBaseModel):
    """
    Single page list item with resolved contributors, owner, and counters.
    """

    contributors: typing.List[Contributor] = pydantic.Field()
    """
    Users that have contributed to the single page content snapshots.
    """

    owner: Contributor
    page: SinglePage
    stats: Stats

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
