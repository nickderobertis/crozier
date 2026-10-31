

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BadRequestErrorBody(UniversalBaseModel):
    type: str = pydantic.Field()
    """
    The section of the HTTP specification that defines this status.
    """

    title: str = pydantic.Field()
    """
    The sentence the form shows. Dutch, because a validation failure is the one problem whose title is read by the person filling the form in rather than by whoever is debugging.
    """

    status: int = pydantic.Field()
    """
    The HTTP status, repeated in the body so a stored problem still names it.
    """

    instance: str = pydantic.Field()
    """
    The path of the request that was refused.
    """

    errors: typing.Dict[str, typing.List[str]] = pydantic.Field()
    """
    Every field that failed, and the Dutch messages it failed with.
    """

    trace_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="traceId"),
        pydantic.Field(
            alias="traceId",
            description="The identifier of this request, echoed in the X-Request-Id response header. A caller-supplied X-Request-Id is kept.",
        ),
    ]
    """
    The identifier of this request, echoed in the X-Request-Id response header. A caller-supplied X-Request-Id is kept.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
