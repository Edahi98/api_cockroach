TYPE_DEF = """
    type Query {
        _empty: String
    }
    type Mutation{
        addfilter(bs64: String!, filter: String!, format_image: String!): String!
    }
"""