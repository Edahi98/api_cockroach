from ariadne import MutationType, QueryType
from . import resolves_mutation, resolves_queries

mutation = MutationType()
query = QueryType()
mutation.set_field("addfilter", resolves_mutation.resolve_addfilter)
mutation.set_field("adduser", resolves_mutation.resolve_adduser)
query.set_field("login", resolves_queries.login)
query.set_field("islogged", resolves_queries.islogged)