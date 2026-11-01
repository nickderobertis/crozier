

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GrepGcReport(UniversalBaseModel):
    """
    The counts from one pass of the grep index's collector over one namespace.
    """

    deleted_other_objects: int = pydantic.Field()
    """
    The other unreferenced grep objects that the pass deleted after the grace window.
    """

    deleted_segments: int = pydantic.Field()
    """
    The unreferenced grep segments that the pass deleted because they were older than the
    minimum segment age.
    """

    listed_bytes: int = pydantic.Field()
    """
    The bytes of every grep object that the pass listed under the namespace, before the pass's
    deletes.
    """

    namespace_reaped: bool = pydantic.Field()
    """
    Whether the pass deleted the grep extension state of a namespace that is missing or
    deleted.
    """

    retained_candidates: int = pydantic.Field()
    """
    The candidates that the pass kept because they were referenced, too young, or
    unrecognized.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
