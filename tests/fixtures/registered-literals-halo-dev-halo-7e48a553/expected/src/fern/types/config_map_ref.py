

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConfigMapRef(UniversalBaseModel):
    """
    Reference to a ConfigMap used by this provider.
    """

    name: str = pydantic.Field()
    """
    ConfigMap metadata.name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
