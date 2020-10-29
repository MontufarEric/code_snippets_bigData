%sql
DROP TABLE IF EXIST data_base.table_table;
CREATE TABLE data_base.table_table 
(
column1     type    comment "comment"
column2     type    comment "comment"
column3     type    comment "comment"
column4     type    comment "comment"
)
USING DELTA OPTIONS
(path 's3a://bucket/folder')
PARTITIONED BY (partition_key);
