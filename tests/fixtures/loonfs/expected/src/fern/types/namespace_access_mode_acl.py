

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .principal_scope import PrincipalScope


class NamespaceAccessModeAcl(UniversalBaseModel):
    """
    Access rows control the operations that principals in this identity domain can perform.
    """

    principal_scope: PrincipalScope = pydantic.Field()
    """
    The identity domain that the namespace's principal IDs belong to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
