/*GitHub Devs: Algorithm designed by @qwainaina, python by @henchhing-limbu, cpp & c by @ajazayeri72*/

#include "real.h"
#include <stdlib.h>

//Main function
int main() {
    define_coordinates();

    int timezone_reward = get_time_zone_reward();

    int location_reward = 0; //forcing location reward 40% Africa, 20% Carribean, 20% SouthEastAsia, 10% Middle-east, 10% South America, 0% Europe, 0% Asia, 0% America

	int process_reward = get_processor_reward();

	//Float total_percentage_reward = ((location_reward * (0.6)) + (process_reward * (0.4)));
	//Float total_percentage_reward = ((location_reward * 3 / 6) + (timezone_reward * 1 / 6) + (process_reward * 2 / 6)); //Add when Coordinates data is available
	float total_percentage_reward = ((timezone_reward * 3 / 6) + (process_reward * 3 / 6));

    int o = (int)total_percentage_reward; //Generating optimization score o as an integer
	printf("Total Percentage Reward: %d \n", o);


	//Integrate optimizer to ensure people randomly to set hash from o score
	//Get o Score from function
	if (o > 14)
		{
		//Use rand function to generate random number between (0 and total_percentage_reward);
		int randomNumber;
		srand((unsigned) time(NULL)); //Make number random each time
		randomNumber = (rand() % 45) + 1; //Made the max 45 instead of 100 % more forgiving
		printf("Randomizer: %d", randomNumber);
		if (randomNumber <= o)
			{
			//printf("Create YP Hash: Success");

			/* Success! */
			return 0;
			}
		else
			{
			//printf("Create YP Hash: Failure");
			/* Success! */
			return -1;
			}
		}
}
