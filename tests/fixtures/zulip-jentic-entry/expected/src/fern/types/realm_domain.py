

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RealmDomain(UniversalBaseModel):
    """
    Object containing details of the newly added domain.
    """

    domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    The new allowed domain.
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
