# Export Neptune database

1. Clone https://github.com/awslabs/amazon-neptune-tools/tree/master/neptune-export and create jar using the commands `mvn clean install`

2. Then go to `target` & run `jar` with Variables

	   java -jar neptune-export.jar export-pg -e eballot-dev-instance-1.XXXXX.ca-central-1.neptune.amazonaws.com -d /Users/thirumal/Downloads/neptune --format json

3. 
