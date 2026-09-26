

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemFiftyFiveRealmDomain(UniversalBaseModel):
    """
    Object containing details of the edited domain.
    """

    domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    The domain whose settings have changed.
    """

    allow_subdomains: typing.Optional[bool] = pydantic.Field(default=None)
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
