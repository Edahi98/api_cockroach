from ariadne import MutationType
from . import resolves_mutation

mutation = MutationType()
mutation.set_field("addfilter", resolves_mutation.resolve_addfilter)