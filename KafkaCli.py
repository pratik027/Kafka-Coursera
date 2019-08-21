# ## Kafka CLI
# 
# This is the Kafka environment where you should implement the tasks described below. Each task should be solved using a shell script or a single shell command. Please write the tasks in the required cells, without changing any other cells. Some tasks require kernel interruption so don't be afraid to interrupt the kernel if you see that the tasks don't stop for a long time.
# 
# The following urls of the Kafka infrastructure will be useful for the tasks:
# 
# |Service|URL|
# |------|----|
# |Zookeeper server|localhost:2181|
# |Kafka broker|localhost:9092|
# |Bootstrap server|localhost:9092|
# <br>
# 
# You must use only the following commands for the task completion:
# 
# |Command|Command description|
# |------|----|
# |`kafka-topics.sh`|creates, deletes, describes, or changes a topic|
# |`kafka-console-producer.sh`|reads data from standard input and publish it to certain topic|
# |`kafka-console-consumer.sh`|reads data from the topic and outputs it to standard output|
# |`kafka-run-class.sh`|the tool for executing third-party Java classes in Kafka (e.g. you can run `kafka.tools.GetOffsetShell` with this tool)|
# |`kafka.tools.GetOffsetShell`|an interactive shell for getting consumer offsets from `kafka-run-class.sh` entry point |
# 
# <br>
# 
# The name of the topic must be `"my-topic"`

# **Task 1** Create a topic with the name `"my-topic"` with *N partitons* and *M replications*. E.g. *N = 5, M = 2*.

get_ipython().run_cell_magic('bash', '', '\nZOOKEEPERS=localhost:2181\nkafka-topics.sh --zookeeper $ZOOKEEPERS --create --topic "my-topic" --partitions 5 --replication-factor 2')

# **Task 2.** List all the available topics.

get_ipython().run_cell_magic('bash', '', 'ZOOKEEPERS=localhost:2181\nkafka-topics.sh --zookeeper $ZOOKEEPERS --list')

# **Task 3.**  Get the description of the topic created in task 1.

get_ipython().run_cell_magic('bash', '', 'ZOOKEEPERS=localhost:2181\nkafka-topics.sh --zookeeper $ZOOKEEPERS --describe "my-topic"')

# **Task 4.** Push the numbers from 1 to 20 into the topic created in task 1. Each number should be pushed as an independent action.

get_ipython().run_cell_magic('bash', '', 'broker=localhost:9092\nseq 20 40 | kafka-console-producer.sh --broker-list $broker --topic "my-topic"')

# **Task 5.** Fetch all the data from the topic. Make sure that Kafka doesn't store the order of messages (in this case message is a number passed to the topic).

get_ipython().run_cell_magic('bash', '', 'ZOOKEEPERS=localhost:2181\nkafka-console-consumer.sh --topic "my-topic" --zookeeper $ZOOKEEPERS --from-beginning')

# **Task 6.** Fetch the data from any partition *k, k < N*

get_ipython().run_cell_magic('bash', '', 'broker=localhost:9092\n$KAFKA_HOME/bin/kafka-simple-consumer-shell.sh --broker-list $broker --topic "my-topic" --partition 3 --offset -2')

# **Task 7.** Get the latest offset from all the partitions.

get_ipython().run_cell_magic('bash', '', 'broker=localhost:9092\nkafka-run-class.sh kafka.tools.GetOffsetShell --broker-list $broker --topic "my-topic" --time -2')
