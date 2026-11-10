

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PartnerEndCustomerSecrets(UniversalBaseModel):
    """
    The secrets for the newly created end customer in non-Production environments.
    """

    development: typing.Optional[str] = pydantic.Field(default=None)
    """
    The end customer's secret key for the Development environment.
    """

    sandbox: typing.Optional[str] = pydantic.Field(default=None)
    """
    The end customer's secret key for the Sandbox environment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
