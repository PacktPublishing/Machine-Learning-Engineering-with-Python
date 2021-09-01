# Machine-Learning-Engineering-with-Python
Machine Learning Engineering with Python


* **Chapter 1** - Introduction to Machine Learning Engineering
* **Chapter 2** - The Machine Learning Development Process
* **Chapter 3** - From Model To Model Factory
* **Chapter 4** - User Defined Libraries
* **Chapter 5** - Deployment Architecture and Tools
* **Chapter 6** - Scaling Up
* **Chapter 7** - ML Microservice Use Case
* **Chapter 8** - Extract Transform Machine Learn (ETML) Use Case

Chapter progress (last updated 25th August 2021)

| Chapter | Prelim Draft Complete | Draft Reviewed | TR Feedback Received | Final Draft Accepted |
| --- | --- | --- | --- | -- |
| 1 | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark:  |
| 2 | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark:  |
| 3 | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | |
| 4 | :heavy_check_mark: |  :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| 5 | :heavy_check_mark: |  :heavy_check_mark:|:heavy_check_mark:  | |
| 6 | :heavy_check_mark: |  :heavy_check_mark:| :heavy_check_mark: | |
| 7 | :heavy_check_mark:| :heavy_check_mark: | :heavy_check_mark: | |
| 8 | :heavy_check_mark:|  :heavy_check_mark: | :heavy_check_mark:| |


## Setting Up


### PySpark
```bash
 conda install -c conda-forge pyspark 
```
### Spark
I suggest following an online tutorial like [this](https://dltlabs.medium.com/how-to-install-pyspark-13a07da0c75f) or [this](https://phoenixnap.com/kb/install-spark-on-ubuntu).

If on Ubuntu you may have to install Java and Scala if not already installed, I did this by

```bash
sudo apt install default-jre
sudo apt install default-jdk
sudo apt install scala
```

Ended up running this [tutorial](https://www.liquidweb.com/kb/how-to-install-apache-spark-on-ubuntu/) with the following changes

1. Extracted spark standalone in /usr/local/spark
2. Used my conda python dist for PYSPARK_PYTHON
```bash
(base) andrew@andrew-ThinkStation-P300:/home$ echo $SPARK_HOME
/usr/local/spark

(base) andrew@andrew-ThinkStation-P300:/home$ echo $PYSPARK_PYTHON
/home/andrew/anaconda3/bin/python

(base) andrew@andrew-ThinkStation-P300:/home$ echo $PATH
/home/andrew/anaconda3/bin:/home/andrew/anaconda3/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/bin:/sbin:/usr/local/spark/bin:/usr/local/spark/sbin
```

I also had to perform this [hack](https://www.programmersought.com/article/82621638955/)

### Some potential gotchas

1. It is relatively common to get your AWS config credentials mixed up, especially if you have multiple accounts (for example root and user accounts). Make sure you are using the correct account credentials when using the aws cli.
2. AWS Forecast (used in chapter 7) only works on certain regions, so if your account has a default region that is different to this you will need to specify another region upon calling the Forecast service through the cli or API.
