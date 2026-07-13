

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ContactsFilter(UniversalBaseModel):
    company_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the associated company of the contact to filter on
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email of the contact to filter on
    """

    first_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    First name of the contact to filter on
    """

    last_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Last name of the contact to filter on
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the contact to filter on
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
