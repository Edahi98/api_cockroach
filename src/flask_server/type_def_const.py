TYPE_DEF = """
    scalar JSON
    
    type Query {
        login(pwd: String!, nickname: String!): JSON
        islogged(token: String!): Int
    }
    
    type Mutation{
        addfilter(bs64: String!, filter: String!, format_image: String!, token: String!): String!
        adduser(pwd: String!, nick: String!): String
    }
"""