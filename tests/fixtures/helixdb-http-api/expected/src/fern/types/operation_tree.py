

import typing

OperationTree = typing.Dict[str, typing.Any]
"""
One externally tagged, snake_case HelixDB AstNode operation. Source operations start a traversal; subsequent operations contain their predecessor under input. Use a typed HelixDB SDK or the query documentation to construct this recursive tree.
"""
