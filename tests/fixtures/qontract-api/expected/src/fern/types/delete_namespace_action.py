

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeleteNamespaceAction(UniversalBaseModel):
    """
    Action: Delete a namespace from a cluster.
    """

    cluster: str = pydantic.Field()
    """
    Cluster name
    """

    namespace: str = pydantic.Field()
    """
    Namespace name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
