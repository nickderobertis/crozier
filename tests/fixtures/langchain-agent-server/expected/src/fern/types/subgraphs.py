

import typing

from .graph_schema_no_id import GraphSchemaNoId

Subgraphs = typing.Dict[str, GraphSchemaNoId]
"""
Map of graph name to graph schema metadata (`input_schema`, `output_schema`, `state_schema`, `config_schema`, `context_schema`).
"""
