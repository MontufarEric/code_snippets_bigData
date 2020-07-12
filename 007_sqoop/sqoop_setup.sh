## SQOOP SETUP AND TEST



## dowload sqoop

wget http://mirrors.estointernet.in/apache/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz

#rename it 

mv sqoop-1.4.7.bin__hadoop-2.6.0/* sqoop-1.4.7


## ADD SQOOP HOME to bash_profile
## SQOOP HOME

echo "export SQOOP_HOME=/home/fieldengineer/opt/sqoop-1.4.7" >> bash_profile.sh
echo "export PATH=$PATH:$SQOOP_HOME/bin" >> bash_profile.sh

### go to sqoop/conf
## sqoop-env-template  ---> sqoop-env.sh
cd ~/opt/sqoop-1.4.7/conf
mv sqoop-env-template.sh sqoop-env.sh
echo  "export HADOOP_MAPRED_HOME=/home/fieldengineer/opt/hadoop-3.1.3" >> sqoop-env.sh
echo  "export HADOOP_COMMON_HOME=/home/fieldengineer/opt/hadoop-3.1.3" >> sqoop-env.sh




## https://medium.com/@nitingupta.bciit/setup-sqoop-to-import-mysql-data-to-hdfs-on-ubuntu-16-04-5243d9eef560



CREATE USER 'sqoop_user'@'localhost' IDENTIFIED BY 'Password1234!';
GRANT ALL PRIVILEGES ON dp.* TO 'sqoop_user'@'localhost';
FLUSH PRIVILEGES
