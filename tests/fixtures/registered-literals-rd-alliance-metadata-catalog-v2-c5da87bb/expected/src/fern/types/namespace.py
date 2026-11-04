

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Namespace(UniversalBaseModel):
    prefix: typing.Optional[str] = pydantic.Field(default=None)
    """
    Recommended prefix to use when abbreviating predicate URIs from this namespace.
    """

    uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    URI of the scheme’s namespace, to which a predicate name can be appended to generate the URI of a predicate of the scheme. Must begin with a protocol string (e.g. `https://`) and end in a slash (/) or a hash (#).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
