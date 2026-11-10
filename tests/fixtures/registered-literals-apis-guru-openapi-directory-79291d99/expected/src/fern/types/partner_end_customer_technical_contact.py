

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PartnerEndCustomerTechnicalContact(UniversalBaseModel):
    """
    The technical contact for the end customer. Defaults to partner's technical contact if omitted.
    """

    email: typing.Optional[str] = None
    family_name: typing.Optional[str] = None
    given_name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
