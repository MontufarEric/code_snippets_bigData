#!/usr/bin/env bash

echo "INSTALLING JAVA"

sudo apt update
mkdir /opt
cd /opt
wget -O jdk-8u221-linux-x64.tar.gz \
-c --content-disposition \
"https://javadl.oracle.com/webapps/download/AutoDL?BundleId=239835_230deb18db3e4014bb8e3e8324f81b43"
tar -zxf jdk-8u221-linux-x64.tar.gz
rm jdk-8u221-linux-x64.tar.gz
cd
sudo touch .bash_profile.sh
echo "JAVA_HOME=/opt/jdk1.8.0_221" >> .bash_profile.sh
echo "export PATH=$PATH:$JAVA_HOME/bin" >> .bash_profile.sh

echo "JAVA READY"
echo "DOWNLOADING PYTHON"

cd /opt
wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz
tar –xf Python-3.7.5.tgz

echo "PYTHON READY"

echo "INSTALLING HADOOP"

cd
apt-get install openssh-server -y 
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys


echo "export HADOOP_HOME=/opt/hadoop-3.1.3" >> .bash_profile.sh
echo "export HADOOP_INSTALL=$HADOOP_HOME" >> .bash_profile.sh
echo "export HADOOP_MAPRED_HOME=$HADOOP_HOME" >> .bash_profile.sh
echo "export HADOOP_COMMON_HOME=$HADOOP_HOME" >> .bash_profile.sh
echo "export HADOOP_HDFS_HOME=$HADOOP_HOME" >> .bash_profile.sh
echo "export YARN_HOME=$HADOOP_HOME" >> .bash_profile.sh
echo "export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native" >> .bash_profile.sh
echo "export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin" >> .bash_profile.sh
source .bash_profile

echo "JAVA HOME READy"
echo "SETTING UP HADOOP FILES"

cd /opt/hadoop/temp
mkdir namenode
mkdir datanode

cd /opt/hadoop-3.1.3/etc/hadoop
echo "export JAVA_HOME=/home/fieldengineer/opt/jdk1.8.0_221" >> hadoop-env.sh

echo "<configuration>
<property>
  <name>fs.default.name</name>
    <value>hdfs://localhost:9000</value>
</property>
</configuration>" >> core-site.xml


echo "<configuration>
<property>
 <name>dfs.replication</name>
 <value>1</value>
</property>

<property>
  <name>dfs.name.dir</name>
    <value>file:///opt/hadoop-3.1.3/temp/namenode</value>
</property>

<property>
  <name>dfs.data.dir</name>
    <value>file:///opt/hadoop-3.1.3/temp/datanode</value>
</property>
</configuration>" >> hdfs-site.xml

echo "<configuration>
 <property>
  <name>mapreduce.framework.name</name>
   <value>yarn</value>
 </property>
</configuration>" >> mapred-site.xml

echo "<configuration>
 <property>
  <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
 </property>


hdfs namenode -format
cd $HADOOP_HOME/sbin/
./start-all.sh