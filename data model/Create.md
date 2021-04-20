#### Create Vertex using Gremlin

Create popery graph data with Gremlin

```
g.addV('User').
    property(id, 'u-1').
    property('firstname', 'Thirumal').
    property('LastName', 'M').
    addV('User').
    property(id, 'u-2').
    property('firstname', 'Jessica').
    property('LastName', 'Alba').
    V('u-1').addE('Knows').to(V('u-2')).
    property(id, 'k-1').
    property('since', '2008-02-01')
```
