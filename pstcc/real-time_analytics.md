# notes from real-time analytics text ...
# impediments to real-time analytics
They are 
1. latency, 
1. freshness, 
1. throughput, and 
1. concurrency, 


!include real-time_imgestion.png

see real-time_imgestion.png diagram

## Latency
The speed of your data depends greatly on how it is stored, and that then dictates what needs to happen to pull and combine it into actionable information successfully.

## Freshness
you need to react quickly when things change.

How long does your company wait before data from your transaction systems is available for a model to make a prediction from it?


## Throughput
In many cases, the volume you can process is heavily dependent on the bandwidth of the network passing the data, along with the number of nodes, processors, and memory levels of the databases used to store the data.

Another issue related to throughput is change. Can your database rapidly update existing fields while simultaneously being able to add new fields? Can it add those new fields without needing to create an entirely new schema?

## Concurrency
Concurrency is also very susceptible to data growth.

The combination of latency, freshness, throughput, and concurrency forms the basis of real-time analytics.


# Trade-offs and Workarounds
## Freshness for Latency

### Views
1. Materialized views are queries that generate a transformed copy of the data within the database, whereas 
1. non-materialized views execute at the time they are needed. 

### Pre-Aggregated Data
Aggregation removes the individual row-level detail from the data. While the aggregated view may produce summary results quickly, the resulting dataset may be missing key information that may be relevant to analysis.


### Batch Processing (ugh ...)
The fundamental trade-off with batch processing is freshness for latency.

## Concurrency for Latency

### Query Queuing
### Database Clustering
Another method for improving concurrency is database separation.
This technique organizes schemas and tables by content, keeping disparate data separate.

Throughput for Latency and Overall Efficiency
1. Poorly written queries
Users writing code against the analytics database pull more data than needed or use methodologies that require more processing to complete (such as using a WHERE clause in place of an inner join).

1. Indexing
While they improve query performance, they delay the write process as the new data is indexed.

1. Too much access
establish un-needed access, remove users, push downstream, etc.
1. Resources

The database server’s processor, memory, and/or storage allocation is insufficient to maintain the required usage. Network performance is also vital in large-volume data reporting and analytics.


### Indexing
quicker access to 'key' data ... These chunks contain a portion of the data and a pointer to another location on disk where a continuation of the data might be found.

The downside to indexes is that they take up additional space on the server and are expensive to maintain.

### Resources
The more servers and architecture a company adds, the more personnel resources are required to keep those systems running.

Some companies will simply resort to smaller reporting windows or limited data. They are forced to pull two to three years because five years simply takes too much time and effort for their server to run.


# Driving Forces of Real Time
1. Historical (descriptive) reporting
What happened and when?

1. Diagnostic analytics
Why did these things happen?

1. Predictive analytics
When will this thing happen again?

1. Preemptive analytics
How do we stop this thing from happening again?

# Collecting Real-Time Data

The main component of real-time is streaming event data. Event streams encapsulate an unbounded stream of structured row data continuously fed into the database.

# Combining Real-Time Data with Historical Data



# Real-Time Analytics Database Solutions
## Indexes
1. Sparse indexes
Indexes do not contain all values from the field but rather indicate a range where the queried value might be found.

1. Aggregating indexes
Instead of the query engine finding all the data and then aggregating, the indexer aggregates and groups on the fly.

1. Join indexes
Contains information from multiple tables (or multiple columns within a table). A join index is a separate table that can also be used to join two other tables.

1. Metadata indexes
Uses information about the data to organize it in an easily navigable hierarchical structure.

1. String indexes
These are indexes of values within a string and can be used to identify substrings quickly and efficiently.

## Columnar Databases
Traditionally, databases store data in rows, which is incredibly efficient when writing data. This is typically important in transactional systems.

But, when databases get larger, the advantages of row level data start to wane.


The alternative is a columnar database. In columnar databases, the data is stored in columns. Writing the data takes additional time, as multiple passes through the database are required to populate the individual columns. However, columnar databases perform much faster when it comes to reading larger amounts of data for analytics, because columnar data allows the computer to bypass irrelevant information to get to the data relevant to your request.


Examples of columnar databases include Druid, HBase, Kudu, MonetDB, and Clickhouse.


## Processing Order
Resources designated for storing data are kept separate from resources devoted to computations, indexing, and aggregation, which means database maintenance actions do not interfere with the performance of read actions used for analysis.

### Bitmap Indexes: Making Data for Computers

### Shards
This is where the database is broken down into chunks associated with specific dimensions or rows. Partitioning the data into shards allows transactional systems to write data to multiple shards simultaneously.

Breaking the database into shards facilitates horizontal expansion.


## Case Studies

### Technology-Driven Video Advertising
A global leader in cable and video advertising collects data from more than six billion devices. This data is accurate, rich, and valuable as part of its strategy for providing customized, targeted advertising. The problem was that this data was huge, and the resources required to provide near-real-time targeted advertising were immense. To meet the need, the company established several hundred Hadoop servers and used them to batch process and pre-aggregate the data. Still, with this huge investment in hardware and tools, the process took one to three days to send a targeted ad to a customer.


#### Solution
1. The company went from over 1,000 nodes to only 11.

1. Its virtual CPUs were cut by more than half from 3,400 to only 1,400.

1. Its data went from being 1–3 days old to only 20 minutes old.

1. eIts queries dropped from 12 hours to less than a minute.

### Digital Advertising

#### Solution
By integrating ideas like bitmap indexing, columnar databases, and sharding, the large aggregation table was no longer required. What’s more, the time it took to query the data went from days to about 45 milliseconds.


### Marketing Campaign Performance
This company struggled with 200 million contacts in its CRM system, combined with over a terabyte of daily data updates.

#### Solutoin


## Author
Christopher Gardner
Christopher James Gardner
Title
Business Intelligence Analyst Lead
Affiliation
Alumni
ITS DISC Data Innov Sys & Cld - Faculty and Staff
