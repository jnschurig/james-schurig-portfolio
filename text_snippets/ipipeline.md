When starting at iPipeline, the Insuresight product was in startup mode. They had signed 
a couple customers, but had yet to do an official production deployment for any of them. 
This was the first time I had encountered a group who were actively selling data as a service 
to external customers. All my previous experience had been in serving internal stakeholders 
and processes. The prospect of contributing to an analytics product with active revenue was 
very exciting to me. 

After starting, I was first tasked with taking the initial work that had been done by a 
consulting firm and bringing it to a "production ready" state. I commenced a rewrite of 
hundreds of lines of batch scripts, which had to be run in Windows, and converted them to 
python for the sake of multi-platform compatibility and future programmability. Then I wrote 
a tool, also in python, to deploy sql objects written by BI developers, analysts, and other 
report writers. 

As time went on, this tool developed more and more features and eventually came to be known 
as the JBT, or "James Build Tool" because it ended up working so similarly to DBT. This tool 
allowed for metadata driven deployments and customer build testing, development, and 
environment simulation. The JBT was also capable of cross-region data replication and managing 
Snowflake Marketplace Shares.

In addition to work on the JBT, I wrote dozens of procedures, functions, and scripts related 
to ingesting and transforming data, as well as providing insight and oversight over the 
entire, multi-account and multi-region, system. 
