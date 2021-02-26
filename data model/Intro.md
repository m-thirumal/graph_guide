#### When should I make property into a vertex?

1. Relate entities at `query time`

    * Given your `use case`, is this `attribute` something that can be used to `relate entities`?
    * Queries may not know which attributes or what attribute values relate entities
        * Find all
        
2. Complex types
    
    * Attribute values with multiple fields
        * Eg: Address 
    * Attribute values that are part of a value structure or hierarchy
    
3. Reduce Fan-out

    * Extract hierarchy, prefixes
    * Reduces the number of edges it touch
    * Show me all customers who purchased in `May 2017`. 
    
    ![reduce_fanout.png](reduce_fanout.png)

#### Vertex or edge?