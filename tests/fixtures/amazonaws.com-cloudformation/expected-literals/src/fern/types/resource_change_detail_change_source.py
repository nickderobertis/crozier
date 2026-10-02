

import typing

ResourceChangeDetailChangeSource = typing.Union[
    typing.Literal["ResourceReference", "ParameterReference", "ResourceAttribute", "DirectModification", "Automatic"],
    typing.Any,
]
