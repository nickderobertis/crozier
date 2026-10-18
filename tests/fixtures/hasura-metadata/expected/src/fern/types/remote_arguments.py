

import typing

from .graph_ql_value_name import GraphQlValueName

RemoteArguments = typing.Dict[str, typing.Optional[GraphQlValueName]]
"""
Remote arguments are represented by an object that maps each argument name to its value.
"""
