

import typing

CaptureRuleSource = typing.Union[
    typing.Literal["jsonPath", "xpath", "header", "queryStringParameter", "cookie", "pathParameter"], typing.Any
]
