##### Create Modern toy graph

    graph=TinkerFactory.createModern()

##### Traversal

    g=graph.traversal()
 
##### List all vertices

    g.V()

##### Get the vertex using id

    g.V(1)

##### Get the value of given property & vertex

    g.V(1).values('name')

##### List all the outgoing edges 

    g.V(1).outE('knows')

##### List all incoming vertices 

###### Long version

    g.V(1).outE('knows').inV().values('name')
    
###### Short version

    g.V(1).out('knows').values('names')
    

##### List with conditions

    g.V(1).out('knows').has(age, gt(30)).values('name')
 