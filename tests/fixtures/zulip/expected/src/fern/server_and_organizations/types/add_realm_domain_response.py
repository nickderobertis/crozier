

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .add_realm_domain_response_new_domain_item import AddRealmDomainResponseNewDomainItem


class AddRealmDomainResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    new_domain: typing.Optional[typing.List[AddRealmDomainResponseNewDomainItem]] = pydantic.Field(default=None)
    """
    An array containing the ID of the newly added domain
    and the submitted domain name string.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
