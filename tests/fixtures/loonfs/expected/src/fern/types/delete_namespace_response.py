

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .change_seq import ChangeSeq
from .namespace_id import NamespaceId


class DeleteNamespaceResponse(UniversalBaseModel):
    """
    The result of deleting a namespace.
    """

    head_seq: ChangeSeq = pydantic.Field()
    """
    The last committed sequence before the namespace was deleted.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The deleted namespace.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
