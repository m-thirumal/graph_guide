# Pagination

List and count in one query

     g.V().hasLabel('person').
        union(range(2,4).elementMap(),count()).
        fold()  
