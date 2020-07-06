/* GitHub Devs: Algorthim designed by @qwainaina, python by @henchhing-limbu, cpp & c by @ajazayeri72, locator code structure audit @xephy @LwandaMagere */
#include <stdio.h>
#include <time.h>

#ifdef _WIN32
#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#else
#include <unistd.h>
#endif

#include <stdlib.h>
#include <string.h>
#include <errno.h>

//locator definitions
#include "locator.h"
#include "define.c"

//Define Time Zones
#define EARLIEST_AFRICAN_TIMEZONE -1
#define LATEST_AFRICAN_TIMEZONE 4
#define EARLIEST_ASIAN_TIMEZONE 5
#define EARLIEST_EUROPEAN_TIMEZONE 0


//Define Regional Rewards
#define CARRIBEAN_REGION_REWARD 10
#define SOUTH_AMERICAN_REGION_REWARD 10
#define AFRICAN_REGION_REWARD 70
#define ASIAN_REGION_REWARD 10
#define OTHER_REGION_REWARD 0


//Define TOTAL_YESPOWER_REWARD 103.125 - NOT NEEDED ANY MORE

//Define Machine Processor
#define OS_ARM 0
#define OS_WINDOWS 0
#define OS_X86 0


struct coordinate
{
  int top_left_x;
	int top_left_y;
	int bottom_right_x;
	int bottom_right_y;
};

struct coordinate RegionCoordiantes(int x1, int x2, int x3, int x4) {
	struct coordinate result;
	result.top_left_x = x1;
	result.top_left_y = x2;
	result.bottom_right_x = x3;
	result.bottom_right_y = x4;
	return result;
}

struct coordinate CARRIBEAN_REGION;
struct coordinate SOUTH_AMERICAN_REGION;
struct coordinate AFRICAN_REGION;
struct coordinate ASIAN_REGION;

#ifdef __arm__
#define OS_ARM 1
#elif defined(_WIN32) || defined(WIN32) || defined(_WIN64) || defined(WIN64)
#define OS_WINDOWS 1
#elif defined(_X86_) || defined(__X86_64__) || defined(__x86_64__) || defined(__amd64__)
#define OS_X86 1
#endif


//Get Processor Reward %
int get_processor_reward() {
	if (OS_WINDOWS) {
		return 10;
	}
	else if (OS_ARM) {
		return 70;
	}
	else if (OS_X86) {
		return 15;
	}
	else {
		return 5;
	}
}


//Get Machine Timezone
int get_timezone() {
	time_t now = time(NULL);
    time_t tmp = time(&tmp);
    struct tm *utc = gmtime(&tmp);
    int diff = (now - mktime(utc)) / 3600;
	return diff;
}

//Set timezone score
int get_time_zone_reward() {
	int timezone = get_timezone();
	if ((EARLIEST_AFRICAN_TIMEZONE < timezone) && (timezone <= EARLIEST_EUROPEAN_TIMEZONE)) {

		return 30;

	}
	else
	{
		if ((EARLIEST_EUROPEAN_TIMEZONE < timezone) && (timezone <= LATEST_AFRICAN_TIMEZONE)) {
			return 40;
		}
		else
		{
			if ((LATEST_AFRICAN_TIMEZONE < timezone) && (timezone <= EARLIEST_ASIAN_TIMEZONE)) {
				return 20;
			}
			else
			{
				return 10;
			}
		}
	}
}


//Get timezone score
int get_machine_coordinates_reward(double latitude, double longitude)
{
	if ((CARRIBEAN_REGION.top_left_x <= longitude) && (longitude < CARRIBEAN_REGION.bottom_right_x) && (CARRIBEAN_REGION.bottom_right_y <= latitude) && (latitude < CARRIBEAN_REGION.top_left_y)) {
		return CARRIBEAN_REGION_REWARD;
	}
	else if ((SOUTH_AMERICAN_REGION.top_left_x <= longitude) && (longitude < SOUTH_AMERICAN_REGION.bottom_right_x) && (SOUTH_AMERICAN_REGION.bottom_right_y <= latitude) && (latitude < SOUTH_AMERICAN_REGION.top_left_y)) {
		return SOUTH_AMERICAN_REGION_REWARD;
	}
	else if ((AFRICAN_REGION.top_left_x <= longitude) && (longitude < AFRICAN_REGION.bottom_right_x) && (AFRICAN_REGION.bottom_right_y <= latitude) && (latitude < AFRICAN_REGION.top_left_y)) {
		return AFRICAN_REGION_REWARD;
	}
	else if ((ASIAN_REGION.top_left_x <= longitude) && (longitude < ASIAN_REGION.bottom_right_x) && (ASIAN_REGION.bottom_right_y <= latitude) && (latitude < ASIAN_REGION.top_left_y)) {
		return ASIAN_REGION_REWARD;
	}
	else {
		return OTHER_REGION_REWARD;
	}
}


//Main function
int main() {

    //Cores Code 26/03/2020

    	int nprocs = -1;
	int nprocs_max = -1;

#ifdef _WIN32
#ifndef _SC_NPROCESSORS_ONLN
	SYSTEM_INFO info;
	GetSystemInfo(&info);
#define sysconf(a) info.dwNumberOfProcessors
#define _SC_NPROCESSORS_ONLN
#endif
#endif
#ifdef _SC_NPROCESSORS_ONLN

	nprocs = sysconf(_SC_NPROCESSORS_ONLN);
	if (nprocs < 1)

	{
		printf(stderr, "Could not determine number of CPUs online:\n%s\n");

	}

	nprocs_max = sysconf(_SC_NPROCESSORS_CONF);
	if (nprocs_max < 1)
	{

		printf(stderr, "Could not determine number of CPUs configured:\n%s\n");

	}
	printf("%ld of %ld processors online\n", nprocs, nprocs_max);

#else
	printf(stderr, "Could not determine number of CPUs");
#endif

    //End of Cores


		//locator Code
		CURL* curl;
		CURLcode res;
		char csv_field[BUFSIZE];
		struct location url;
		struct web_data curl_data;

		/* initialize structure */
		/* curl_data and url structures must be kept separate or the
			 call the curl makes to write_mem() screws up */

		curl_data.buffer =  (char *) malloc(1);
		curl_data.size = 0;
		url.latitude = 0.0;
		url.longitude = 0.0;

		/* initialize locations */
		strcpy(url.address, "http://ip-api.com/csv/");

		/* initialuze curl */
		/* I use the same curl handle for all of the calls,
			 so only only statement is needed here */
		curl = curl_easy_init();

		/*---------------- FIRST READ ----------------*/
		/* set options */
			/* url to read */
		curl_easy_setopt(curl, CURLOPT_URL, url.address);
		/* The function to read in data chunks */
		curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_mem);
		/* The structure to use for reading */
		curl_easy_setopt(curl, CURLOPT_WRITEDATA, &curl_data);
		/* make the call */
		res = curl_easy_perform(curl);
		/* confirm that the call was successful, bail if not */
		if (res != CURLE_OK)
		{
			fprintf(stderr, "Curl read failed: %s\n",
				curl_easy_strerror(res)
				);
			exit(1);
		}

		/* At this point, the size of the data read is stored in curl_data.size
			 and the string read is in curl_data.buffer. The data is in CSV format,
			 which the fetch() function can read */
			 /* was the call successful? Fetch the first CSV item from the buffer and
				store it in buffer 'csv_field' */
		fetch(1, curl_data.buffer, csv_field);
		/* if the string csv_field isn't 'success' then the call failed */
		if (strncmp(csv_field, "success", 7) != 0)
		{
			fprintf(stderr, "Failed request from server: %s\n", url.address);
			fprintf(stderr, "Retried status: %s\n", csv_field);
			exit(1);
		}

		/* Get the latitude value & convert to double */
		fetch(8, curl_data.buffer, csv_field);
		url.latitude = strtod(csv_field, NULL);

		/* Get the longitude value & convert to double */
		fetch(9, curl_data.buffer, csv_field);
		url.longitude = strtod(csv_field, NULL);

		printf("Latitude: %lf\n", url.latitude);
		printf("Longitude: %lf\n", url.longitude);

		/*
		printf("\nPress Any Key to Continue...\n");
		getchar();
		*/

    CARRIBEAN_REGION = RegionCoordiantes(-90, 30, -45, 15);
    SOUTH_AMERICAN_REGION = RegionCoordiantes(-90, 15, -30, -60);
    AFRICAN_REGION = RegionCoordiantes(-20, 30, 50, -45);
    ASIAN_REGION = RegionCoordiantes(50, 30, 90, -30);


    //Integrate optimizer to ensure people randomly to set hash from o score; Contributions by whive devs in optimizer.h
    //define_coordinates();
    int timezone_reward = get_time_zone_reward();
  	//int location_reward = get_machine_coordinates_reward(-1.4073685,37.8169209); //forcing location reward 40% Africa, 20% Carribean, 20% SouthEastAsia, 10% Middle-east, 10% South America, 0% Europe, 0% Asia, 0% America
		int location_reward = get_machine_coordinates_reward(url.latitude,url.longitude); //forcing location reward 40% Africa, 20% Carribean, 20% SouthEastAsia, 10% Middle-east, 10% South America, 0% Europe, 0% Asia, 0% America
		int process_reward = get_processor_reward();
    printf("Original Process Reward: %d \n", process_reward);

	/*if (nprocs > 4)
    {*/
       process_reward = process_reward * 4 / (nprocs * 2); //this penalizes machines using more than 2 cores by twice the number of cores they are using.
    //}

    printf("Timezone Reward: %d \n", timezone_reward);
    printf("Location Reward: %d \n", location_reward);
    printf("Process Reward: %d \n", process_reward);



    float total_percentage_reward = ((location_reward * 2 / 6) + (timezone_reward * 2 / 6) + (process_reward * 2 / 6)); //Add when Coordinates data is available

    //float total_percentage_reward = ((timezone_reward * 3 / 6) + (process_reward * 3 / 6));
    /*
    if (location_reward == 0)
    {
    total_percentage_reward=total_percentage_reward-5; //Penalize a CPU by 5% if it can't be geo-located
    }
    */
    int opt = (int)total_percentage_reward; //Generating optimization score o as an integer
    printf("Total Percentage Reward: %d \n", opt);

    //Integrate optimizer to ensure people randomly to set hash from opt score
    //Get randomizer score and compare to opt score
    int randomNumber;
  	srand((unsigned) time(NULL)); //Make number random each time
  	randomNumber = (rand() % 75) + 1; //Made the max 55 instead of 100 % more forgiving
  	printf("Randomizer: %d \n", randomNumber);
    /* Sanity check using O score & Randomizer added by @qwainaina*/

    if (opt  > 14)
    {
      if (randomNumber <= opt)
        {
        printf("Create YP Hash: Success\n");

        }
    else
        {
        printf("Create YP Hash: Failure\n");

        }
    }
}
