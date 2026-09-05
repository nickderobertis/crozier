

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ContainerImage(UniversalBaseModel):
    """
    Container image specification
    """

    reference: str = pydantic.Field()
    """
    Complete OCI image reference.
    Format: [REGISTRY/]REPOSITORY[:TAG|@DIGEST]
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
