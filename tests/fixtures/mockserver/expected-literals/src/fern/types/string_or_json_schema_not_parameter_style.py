

import typing

StringOrJsonSchemaNotParameterStyle = typing.Union[
    typing.Literal[
        "SIMPLE",
        "SIMPLE_EXPLODED",
        "LABEL",
        "LABEL_EXPLODED",
        "MATRIX",
        "MATRIX_EXPLODED",
        "FORM_EXPLODED",
        "FORM",
        "SPACE_DELIMITED_EXPLODED",
        "SPACE_DELIMITED",
        "PIPE_DELIMITED_EXPLODED",
        "PIPE_DELIMITED",
        "DEEP_OBJECT",
    ],
    typing.Any,
]
