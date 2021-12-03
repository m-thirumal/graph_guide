##### Create Modern toy graph

    graph=TinkerFactory.createModern()

##### Traversal

    g=graph.traversal()
 
### `GET/LIST`
| Steps | Meaning |
| :--:  |  :--:   |
| V()   | get all vertices in the graph |
| E()   | get all edges in the graph |
| V().hasLabel(label1, label2, …​) | get all vertices with the specified labels |
| V().has(label, key, value) | get all vertices with the specified label and the property `key` matching the provided `value` |
| V(1) | get the vertex with the id 1 | 

##### `List all vertices`

    g.V()

##### `List all edges`

    g.E()

#### `List all vertices using LABEL`

    g.V().hasLabel('mobile')

#### `List all vertices using more than one LABEL`

    g.V().hasLabel(label1, label2, …​)
    g.V().hasLabel('email', 'mobile')
    g.V().hasLabel('user', 'mobile', 'email').elementMap()

##### `Get the vertex using id`

    g.V(1)

#### `Get all vertices with the specified label and the property key matching the provided value`

    g.V().has(label, key, value)

##### `Get the value of given property & vertex`

    g.V(1).values('name')

##### `List all the outgoing edges` 

    g.V(1).outE('knows').elementMap()

##### `List all incoming vertices` 


#### `Search Edges by multiple labels`

    g.E().or(hasLabel(startingWith('')), hasLabel('')).elementMap()


###### Get the vertices which has edges with propery of `knows`. `Long version`

    g.V(1).outE('knows').inV().elementMap()
    
###### `Short version`

    g.V(1).out('knows').elementMap()
    

##### `List with conditions`

    g.V(1).out('knows').has(age, gt(30)).values('name')
 

### `Access Properties`

| Steps | Meaning |
| :--:  |  :--:   |
| properties(key1, key2, …​) | get all specified properties for the current element | 
| values(key1, key2, …​) | get all specified property values for the current element |
| valueMap(key1, key2, …​) | get all specified property values for the current element as a map |
#### `Get all specified properties for the current element`

    properties(key1, key2, …​)

    gremlin> g.V().hasLabel("person").properties("name")
    ==>vp[name->marko]
    ==>vp[name->vadas]
    ==>vp[name->josh]
    ==>vp[name->peter]

#### `Get all specified property values for the current element`

    values(key1, key2, …​)
    gremlin> g.V().hasLabel("person").values("name")
    ==>marko
    ==>vadas
    ==>josh
    ==>peter

#### `Get all specified property values for the current element as a map`

    valueMap(key1, key2, …​)
    gremlin> g.V().hasLabel("person").valueMap("name","age")
    ==>[name:[marko],age:[29]]
    ==>[name:[vadas],age:[27]]
    ==>[name:[josh],age:[32]]
    ==>[name:[peter],age:[35]]

### `Traversing the Graph`

| Steps | Meaning |
| :--:  |  :--:   |
| out(label1, label2, …​) | Get all adjacent vertices connected by outgoing edges with the specified labels |
| in(label1, label2, …​)  | get all adjacent vertices connected by incoming edges with the specified labels |
| outE(label1, label2, …​) | get all outgoing edges with the specified labels |
| inE(label1, label2, …​) | get all incoming edges with the specified labels |
| both(label1, label2, …​) | get all adjacent vertices connected by an edge with the specified labels |
| bothE(label1, label2, …​).otherV() | traverse to all incident edges with the specified labels and then to the respective other vertices |

#### `Examples`

    gremlin> g.V(1).outE("created")
    ==>e[9][1-created->3]
    gremlin> g.V(1).out("created")
    ==>v[3]
    gremlin> g.V().has("software","name","lop").in("created").values("name")
    ==>marko
    ==>josh
    ==>peter

### `Filter`


| Steps | Meaning |
| :--:  |  :--:   |
| has(key, value)| keep the current element if the specified property has the given value |
| has(key, predicate) | keep the current element if the specified property matches the given predicate |
| filter(traversal) | keep the current element if the provided traversal emits a result |
| not(traversal) | keep the current element if the provided traversal doesn’t emit a result |
| where(predicate) | keep the current element if it matches the predicate referencing another element |

#### `Example`

    gremlin> g.V().has("age",29).valueMap("name","age")
    ==>[name:[marko],age:[29]]

    gremlin> g.V().has("age",gt(30)).valueMap("name","age")
    ==>[name:[josh],age:[32]]
    ==>[name:[peter],age:[35]]

    gremlin> g.V().filter(outE())
    ==>v[1]
    ==>v[4]
    ==>v[6]

    gremlin> g.V().not(outE())
    ==>v[2]
    ==>v[3]
    ==>v[5]

    gremlin> g.V(1).as("other").out("knows").where(gt("other")).by("age").valueMap()
    ==>[name:[josh],age:[32]]

### `Aggregations`

| Steps | Meaning |
| :--:  |  :--:   |
| store(key) | store the current element in the side-effect with the provided key |
| aggregate(key) | store all elements held by all current traversers in the side-effect with the provided key |
| group([key]).by(keySelector) | group all current elements by the provided keySelector; group into a side-effect if a side-effect key was provided, otherwise emit the result immediately |
| fold() | fold all current elements into a single list |
| unfold() | unfold the incoming list and continue processing each element individually |
| count() | count the number of current elements |
| min()/max() | find the min/max value |
| sum() | compute the sum of all current values |
| mean() | compute the mean value of all current values |

#### `Examples`

    gremlin> g.V().hasLabel("person").store("x").select("x")
    ==>[v[1]]
    ==>[v[1],v[2]]
    ==>[v[1],v[2],v[4]]
    ==>[v[1],v[2],v[4],v[6]]
    gremlin> g.V().hasLabel("person").aggregate("x").select("x")
    ==>[v[1],v[2],v[4],v[6]]
    ==>[v[1],v[2],v[4],v[6]]
    ==>[v[1],v[2],v[4],v[6]]
    ==>[v[1],v[2],v[4],v[6]]
    gremlin> g.V().group().by(label)
    ==>[software:[v[3],v[5]],person:[v[1],v[2],v[4],v[6]]]
    gremlin> g.V().fold()
    ==>[v[1],v[2],v[3],v[4],v[5],v[6]]
    gremlin> g.V().count()
    ==>6
    gremlin> g.V().fold().count(local)
    ==>6

### `Branches`

| Steps | Meaning |
| :--:  |  :--:   |
| union(branch1, branch2, …​) | execute all branches and emit their results |
| choose(condition, true-branch, false-branch) | if/then/else-based traversal. If the condition matches (yields something), execute the true-branch, otherwise follow the false-branch | 
| choose(selector).option(opt1, traversal).option(opt2, traversal).option(optN, traversal) | value-based traversal; If an option value matches the value emitted by the selector traversal, the respective option traversal will be executed. |

#### Example

    gremlin> g.V().hasLabel("person").union(out("knows"), count())
    ==>v[2]
    ==>v[4]
    ==>4

    gremlin> g.V().hasLabel("person").choose(has("age",gt(30)), constant("senior"), constant("junior"))
    ==>junior
    ==>junior
    ==>senior
    ==>senior

    gremlin> g.V().hasLabel("person").values("age").union(min(), max(), sum(), mean(), count())
    ==>27
    ==>35
    ==>123
    ==>30.75
    ==>4

## `Mutating Traversals`

| Steps | Meaning |
| :--:  |  :--:   |
| addV(label) | add a new vertex |
| addE(label).from(source).to(target) | adds a new edge between the two given vertices |
| property(key, value) | adds or updates the property with the given key |

#### `Example`

    gremlin> g.addV('company').
                property('name','datastax').as('ds').
               addV('software').
                property('name','dse graph').as('dse').
               addV('software').
                property('name','tinkerpop').as('tp').
               addE('develops').from('ds').to('dse').
               addE('uses').from('dse').to('tp').
            addE('likes').from('ds').to('tp').iterate()

    gremlin> g.V().outE().inV().path().by('name').by(label)
    ==>[datastax,develops,dse graph]
    ==>[datastax,likes,tinkerpop]
    ==>[dse graph,uses,tinkerpop]

#### UPSERT GetOrCreate

    g.V(user).fold().coalesce(__.unfold(), __.addV('user').property(T.id, user)).next()
        g.V(user).fold().coalesce(__.unfold(), __.addV('email').property(T.id, email)).next()
        g.V(user).fold().coalesce(__.unfold(), __.addV('mobile').property(T.id, mobile)).next()

## `Paths`

| Steps | Meaning |
| :--:  |  :--:   |
| simplePath() | keep simple, non-cyclic paths (no element must appear twice or more in the current path) | 
| cyclicPath() | keep cyclic paths (at least one element must appear twice or more in the current path) | 

#### Example 

    gremlin> g.V(1).out().in().simplePath().path()
    ==>[v[1],v[3],v[4]]
    ==>[v[1],v[3],v[6]]

    gremlin> g.V(1).out().in().cyclicPath().path()
    ==>[v[1],v[3],v[1]]
    ==>[v[1],v[2],v[1]]
    ==>[v[1],v[4],v[1]]

## `Variables`

| Steps | Meaning |
| :--:  |  :--:   |
| sack(operator) | assign or compute a path-local variable |
| sack() | emit the current sack value | 
| as(label)…​select(Pop, label) | select values from previously labeled steps |

#### `Example`

    gremlin> g.V(1).sack(assign).
                by("age").
                out("knows").
                sack(sum).
                by("age").
                sack().
                path().
                by("age").by("age").by()
    ==>[29,27,56]
    ==>[29,32,61]

    gremlin> g.V(1).as("a").out("knows").as("a").
            select(last, "a")
    ==>v[2]
    ==>v[4]

    gremlin> g.V(1).as("a").out("knows").as("a").
        select(first, "a")
    ==>v[1]
    ==>v[1]

    gremlin> g.V(1).as("a").out("knows").as("a").
        select(all, "a")
    ==>[v[1],v[2]]
    ==>[v[1],v[4]]

# `Pattern Matching`

| Steps | Meaning |
| :--:  |  :--:   |
| match(traversals) | attempts to find matches for the provided patterns in the underlying graph |
| where(traversal) | puts contraints on labeled steps |

#### `Example`

    gremlin> g.V().match(
        __.as("a").has("name", "Garcia"),
        __.as("a").in("writtenBy").as("b"),
        __.as("a").in("sungBy").as("b")).
        select("b").values("name")
    ==>CREAM PUFF WAR
    ==>CRYPTICAL ENVELOPMENT

    gremlin> g.V().match(
        __.as("a").in("writtenBy").as("b"),
        __.as("a").in("sungBy").as("b")).
        where(__.as("a").has("name", "Garcia")).
        select("b").values("name")
    ==>CREAM PUFF WAR
    ==>CRYPTICAL ENVELOPMENT

    gremlin> g.V().has("artist","name","Garcia").as("a").
        in("writtenBy").as("b").
        where(__.as("a").in("sungBy").as("b")).
        values("name")
    ==>CREAM PUFF WAR
    ==>CRYPTICAL ENVELOPMENT

### `DROP`

### Drop property

    g.V().properties('key').drop()

### `DROP using labels`

    g.V().hasLabel("user", 'mobile', 'email').drop().iterate()
