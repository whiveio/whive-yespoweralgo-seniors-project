# YesPowerAlgo_Seniors_Project
The objective of this project is to build the rewarding mechanism or module optimized for solar energy access in Africa. To achieve this we must solve the following tasks. The tasks can be solved using the following programming languages: C, C++ and Python

## Multi-Tier Rewards Architecture Algorithm
The pseudocode below provides a framework for our multi-tier algorithm that will reward nodes on our network. You are expected to turn this pseudocode into software code. The code will be tested through simulations on multiple devices across multiple time zones to ensure it satisfies our optimization criteria. The last step would be to integrate working code into the Yespower module ahead of the launch of the protocol on main-net. 
>Grading: Students will be graded on successful running of simulations of all optimization models, with bonus points for successful integration on blockchain module.

### Note
**1 block = 150 token**

**% = percent of the 150 tokens**

### Task 1
Use the given pseudocode to write a program using any of the above mentioned languages. The goal is to reward a node based on the architecture (CPU type or type of operating system) its running.

#### Architecture rewarding (YesPower) 
(numbers represent percent of total block amount)
```sh  
   If platform >= ARM Then
      reward = "40%" 
   ElseIf platform >= windows Then
       reward = "10%" 
   ElseIf platform >= MacOs Then
       reward = "20%" 
   ElseIf platform >= linux Then
       reward = "30%" 
   Else
      reward = "0"
   End If

```

### Task 2
Use the given pseudocode to write a program. This task unlike task one uses **Timezones** in the rewarding of nodes.

####  Rewards based on Timezone(UTC(GMT)) 
(numbers given represents  token rewarded each time a block is produced)

```sh
   If Timezone >= 0 && <=4 Then
      reward = "80" 
   ElseIf Timezone >=5 && <= 12 Then
      reward = "40" 
   Else
      reward = "30"
   End If

```

### Task 3
Use the given pseudocode to write a program. This task combines **task 1 & 2**, goal is to have a program that rewards nodes based on architecture(CPU type or type of operating system)

####  Split Rewards 
(numbers given represents  token rewarded each time a block is produced)

```sh
If platform >= ARM 
 {
     If Timezone >= 0 && <=4 Then
         reward = "80" 
     Else Timezone >=5 && <= 12 Then
      reward = "40" 
    } 
ElseIf platform >= windows or MacOs
{
     If Timezone >= 0 && <=4 Then
         reward = "20" 
      Else Timezone >=5 && <= 12 Then
      reward = "10"
    }
Else
    reward = "10"

```

## Working on the Exercise

1.Fork the code challenge repository provided.

2.Make a topic branch. In your github form, keep the master branch clean. When you create a branch, it essentially will be a copy of the master.

>Pull all changes, make sure your repository is up to date

```sh
$ cd YesPowerAlgo_Seniors_Project
$ git pull origin master
```

>Create a new branch as follows-> git checkout -b [your_email], e.g.

```sh
$ git checkout -b youremail@gmail.com master
```

>See all branches created

```sh
$ git branch
* youremail@gmail.com
  master
```

>Push the new branch to github

```sh
$ git push origin -u youremail@gmail.com
```

3.**Remember to only make changes to the fork!**
    
Put your files in **task1**, **task2** and **task3** directories in the repository folder and solve the set out exercises. The files naming is as shown below respectively

eg. 
```sh
reward_arch.cpp 
```
```sh
reward_tz.cpp
```
```sh
reward_split.cpp
```

4.Commit the changes to your fork.

5.Make a pull request to the **YesPowerAlgo_Seniors_Project** Repo.
