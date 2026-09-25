

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemFiftyEightRealmDomain(UniversalBaseModel):
    """
    Object containing details of the edited domain.
    """

    domain: str = pydantic.Field()
    """
    The allowed domain.
    """

    allow_subdomains: bool = pydantic.Field()
    """
    Whether subdomains are allowed for this domain.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
