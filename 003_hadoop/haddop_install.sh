#!/usr/bin/env bash

""""
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys
wget http://mirror.cc.columbia.edu/pub/software/apache/hadoop/common/hadoop-3.1.3/hadoop-3.1.3.tar.gz

""""


ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys
cd /opt
wget http://mirror.cc.columbia.edu/pub/software/apache/hadoop/common/hadoop-3.1.3/hadoop-3.1.3.tar.gz
ssh localhost
exit
cd
sudo gedit .bash_profile.sh
echo "export HADOOP_HOME=/home/fieldengineer/opt/hadoop-3.1.3" >> .bash_profile.sh
echo "export HADOOP_INSTALL=$HADOOP_HOME" >> .bash_profile.sh
echo "export HADOOP_MAPRED_HOME=$HADOOP_HOME" >> .bash_profile.sh
echo "export HADOOP_COMMON_HOME=$HADOOP_HOME" >> .bash_profile.sh
echo "export HADOOP_HDFS_HOME=$HADOOP_HOME" >> .bash_profile.sh
echo "export YARN_HOME=$HADOOP_HOME" >> .bash_profile.sh
echo "export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native" >> .bash_profile.sh
echo "export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin" >> .bash_profile.sh
source .bash_profile

cd hadoop-3.1.3/etc/hadoop
sudo gedit hadoop-env.sh
echo "export JAVA_HOME=/home/fieldengineer/opt/jdk1.8.0_221" >> hadoop-env.sh
sudo gedit core-site.xml
echo "<configuration>
<property>
  <name>fs.default.name</name>
    <value>hdfs://localhost:9000</value>
</property>
</configuration>" >> core-site.xml
sudo gedit hdfs-site.xml
echo "<configuration>
<property>
 <name>dfs.replication</name>
 <value>1</value>
</property>

<property>
  <name>dfs.name.dir</name>
    <value>file:///home/fieldengineer/temp/namenode</value>
</property>

<property>
  <name>dfs.data.dir</name>
    <value>file:///home/fieldengineer/temp/datanode</value>
</property>
</configuration>" >> hdfs-site.xml
sudo gedit mapred-site.xml
echo "<configuration>
 <property>
  <name>mapreduce.framework.name</name>
   <value>yarn</value>
 </property>
</configuration>" >> mapred-site.xml
sudo gedit yarn-site.xml
echo "<configuration>
 <property>
  <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
 </property>
</configuration>" >> yarn-site.xml
hdfs namenode -format
cd $HADOOP_HOME/sbin/
./start-all.sh
hdfs dfs -mkdir /fieldengineer
hdfs dfs -mkdir /fieldengineer/hadoop
hdfs dfs -put /Downloads/Shakespeare.txt /fieldengineer/hadoop

### chech for the hdfs at http://localhost:9870/