

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GoogleTypeExpr(UniversalBaseModel):
    """
    Represents an expression text. Example:

        title: "User account presence"
        description: "Determines whether the request has a user account"
        expression: "size(request.user) > 0"
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional description of the expression. This is a longer text which
    describes the expression, e.g. when hovered over it in a UI.
    """

    expression: typing.Optional[str] = pydantic.Field(default=None)
    """
    Textual representation of an expression in
    Common Expression Language syntax.
    
    The application context of the containing message determines which
    well-known feature set of CEL is supported.
    """

    location: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional string indicating the location of the expression for error
    reporting, e.g. a file name and a position in the file.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional title for the expression, i.e. a short string describing
    its purpose. This can be used e.g. in UIs which allow to enter the
    expression.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
