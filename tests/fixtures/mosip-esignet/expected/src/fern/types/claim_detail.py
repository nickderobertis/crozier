

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ClaimDetail(UniversalBaseModel):
    essential: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the Claim being requested is an Essential Claim. If the value is true, this indicates that the Claim is an Essential Claim. The default is false.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    Requests that the Claim be returned with a particular value. For instance the Claim request.
    
    "sub": {"value": "248289761001"} can be used to specify that the request apply to the End-User with Subject Identifier 248289761001.
    """

    values: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Requests that the Claim be returned with one of a set of values, with the values appearing in order of preference.
    """

    purpose: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reason for requesting claim.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
