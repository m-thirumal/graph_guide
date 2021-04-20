#### What makes a good graph

Connected data queries ?

Questions we want to ask of our data require us to understand

    1. Types of relationship
    2. Strength, weight or quality of relationships

### <U>Property or Vertex</U>

#### When should I make property into a vertex?

1. Relate entities at `query time`

    * Given your `use case`, is this `attribute` something that can be used to `relate entities`?
    * Queries may not know which attributes or what attribute values relate entities
        * Find all

2. Complex types

    * Attribute values with multiple fields
        * Eg: Address - Should be vertex instead of property
    * Attribute values that are part of a value structure or hierarchy

3. Reduce Fan-out

    * Extract hierarchy, prefixes
    * Reduces the number of edges it touch
    * Show me all customers who purchased in `May 2017`
	  * Split the date in to year, month and date.

    ![reduce_fanout.png](img/reduce_fanout.png)


### <U> Vertex or edge?</U>

#### When should I use a vertex instead of edge?
When you want to connect `multiple dimensions`(domain entities) in the context of a `fact`(or event).
Because it's easy to add new dimensions.
