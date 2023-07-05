I was referred to Clip by a good friend and former coworker. Clip, also known as Payclip 
in the United States, provided payment processing and digital transaction services in 
Mexico. When I started there, they had just signed a contract with Snowflake and were 
looking to migrate their business intelligence off AWS Redshift and onto Snowflake. 

The first thing I did was set up replication from existing redshift databases to Snowflake. 
This allowed for users to access the familiar data in a new environment. I did this using 
AWS command-line functionality and Pentaho, an open-source ETL server software. Pentaho 
primarily acted as orchestration, doing the EL part of ETL.

Once users were migrated off Redshift, we set up new replication from the original source 
systems, also based in AWS, bringing raw transaction data into Snowflake. Once there, I 
partnered with a skilled member of the devops team and we created a CI/CD pipeline for 
deploying code automatically. Once code was checked into certain permanent branches, a 
new Pentaho ETL server would be instantiated in EC2, a server image applied, code compiled 
and imported, and schedules started. This was one of the coolest projects I had worked on 
in my career to this point.

With CI/CD in place, I built a Kimball-style data warehouse and used this system to deploy 
data objects to a three-tiered environment; development, test, and production.

With a data warehouse created, we struggled with adoption. Those who had been migrated to 
Snowflake using the legacy data structures, didn't really want to learn a new model. As 
such, we created a training and mentoring program at Clip in which we would invite data 
analysts from across the company and teach them how to use the new systems and how to 
solve some of their problems using the new data models. We also used this method to help 
onboard members of the company when we adopted new visualization tools.
