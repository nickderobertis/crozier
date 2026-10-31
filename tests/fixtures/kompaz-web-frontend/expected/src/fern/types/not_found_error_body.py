

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NotFoundErrorBody(UniversalBaseModel):
    type: str = pydantic.Field()
    """
    The section of the HTTP specification that defines this status.
    """

    title: str = pydantic.Field()
    """
    The English name of the status, from the HTTP specification's own vocabulary.
    """

    status: int = pydantic.Field()
    """
    The HTTP status, repeated in the body so a stored problem still names it.
    """

    detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    What went wrong, in Dutch, written for the person using the product. Omitted when the status says everything.
    """

    instance: str = pydantic.Field()
    """
    The path of the request that was refused.
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
