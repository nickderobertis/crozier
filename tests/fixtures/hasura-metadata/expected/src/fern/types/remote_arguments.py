

import typing

from .graph_ql_value_name import GraphQlValueName

RemoteArguments = typing.Dict[str, GraphQlValueName]
"""
Remote arguments are represented by an object that maps each argument name to its value.
"""
