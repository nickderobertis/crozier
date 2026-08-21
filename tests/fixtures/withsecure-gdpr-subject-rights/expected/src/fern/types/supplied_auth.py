

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .supplied_auth_custom_identifier import SuppliedAuthCustomIdentifier
from .supplied_auth_government_id_number import SuppliedAuthGovernmentIdNumber


class SuppliedAuth(UniversalBaseModel):
    """
    A collection of authenticated identifiers uniquely identifying a data subject. The collection must match one of the alternatives dictated by the context for the given operation.
    """

    tel: typing.Optional[str] = pydantic.Field(default=None)
    """
    A telephone number.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    An email address.
    """

    government_id_number: typing.Optional[SuppliedAuthGovernmentIdNumber] = pydantic.Field(default=None)
    """
    A governmental identification number.
    """

    custom_identifier: typing.Optional[SuppliedAuthCustomIdentifier] = pydantic.Field(default=None)
    """
    Any custom identifier.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
