##### Create Modern toy graph

    graph=TinkerFactory.createModern()

##### Traversal

    g=graph.traversal()
 
 ### `GET/LIST`

##### List all vertices

    g.V()

##### List all edges

    g.E()

#### List all vertices using `LABEL`

    g.V().hasLabel('mobile')

#### List all vertices using more than one `LABEL`

    g.V().hasLabel(label1, label2, …​)
    g.V().hasLabel('email', 'mobile')
    g.V().hasLabel('user', 'mobile', 'email').elementMap()

##### Get the vertex using id

    g.V(1)

#### Get all vertices with the specified `label` and the `property key` matching the provided `value`

    g.V().has(label, key, value)

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
 

### `Access Properties`

#### Get all specified properties for the current element

    properties(key1, key2, …​)

    gremlin> g.V().hasLabel("person").properties("name")
    ==>vp[name->marko]
    ==>vp[name->vadas]
    ==>vp[name->josh]
    ==>vp[name->peter]

#### Get all specified property values for the current element

    values(key1, key2, …​)
    gremlin> g.V().hasLabel("person").values("name")
    ==>marko
    ==>vadas
    ==>josh
    ==>peter

#### Get all specified property values for the current element as a map

    valueMap(key1, key2, …​)
    gremlin> g.V().hasLabel("person").valueMap("name","age")
    ==>[name:[marko],age:[29]]
    ==>[name:[vadas],age:[27]]
    ==>[name:[josh],age:[32]]
    ==>[name:[peter],age:[35]]

### `Traversing the Graph`

| Steps | Meaning |
| :--:  |  :--:   |
| out(label1, label2, …​) | Get all adjacent vertices connected by outgoing edges with the specified labels

 ### `DROP`

 ### DROP using labels

    g.V().hasLabel("user", 'mobile', 'email').drop().iterate()