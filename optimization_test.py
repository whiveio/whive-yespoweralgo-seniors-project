"""Unit Test Cases for optimization."""
import datetime
import mock
import os
import optimization
import unittest

class TestOptimzation(unittest.TestCase):

    @mock.patch.object(os, 'uname')
    def test_get_processor_reward_x86_architecture(self, mock_uname):
        mock_uname.return_value.machine = 'x86_64'
        processor_reward = optimization.get_processor_reward()
        self.assertEqual(processor_reward, 35)

    @mock.patch.object(os, 'uname')
    def test_get_processor_reward_arm_architecture(self, mock_uname):
        mock_uname.return_value.machine = 'arm'
        processor_reward = optimization.get_processor_reward()
        self.assertEqual(processor_reward, 55)

    @mock.patch.object(os, 'uname')
    def test_get_processor_reward_other_architecture(self, mock_uname):
        mock_uname.return_value.machine = 'mips'
        processor_reward = optimization.get_processor_reward()
        self.assertEqual(processor_reward, 10)

    def test_get_machine_coordinates_reward_coordinates_carribean_region(self):
        """Tests the reward received by node in Carribean region."""
        longitude, latitude = -80.12, 25.22
        self.assertEqual(
                optimization.get_machine_coordinates_reward(
                    latitude, longitude),
                optimization.CARRIBEAN_REGION_REWARD)

    def test_get_machine_coordinates_reward_coordinates_sa_region(self):
        """Tests the reward received by node in South American region."""
        longitude, latitude = -65.12, -5.01
        self.assertEqual(
                optimization.get_machine_coordinates_reward(
                    latitude, longitude),
                optimization.SOUTH_AMERICAN_REGION_REWARD)

    def test_get_machine_coordinates_reward_coordinates_african_region(self):
        """Tests the reward received by node in African region."""
        longitude, latitude = 0, -15.01
        self.assertEqual(
                optimization.get_machine_coordinates_reward(
                    latitude, longitude),
                optimization.AFRICAN_REGION_REWARD)

    def test_get_machine_coordinates_reward_coordinates_asian_region(self):
        """Tests the reward received by node in Asian region."""
        longitude, latitude = 60, 0
        self.assertEqual(
                optimization.get_machine_coordinates_reward(
                    latitude, longitude),
                optimization.ASIAN_REGION_REWARD)

    def test_get_machine_coordinates_reward_coordinates_other_region(self):
        """Tests the reward received by node in Other region."""
        longitude, latitude = -89, 78
        self.assertEqual(
                optimization.get_machine_coordinates_reward(
                    latitude, longitude),
                optimization.OTHER_REGION_REWARD)
    
    @mock.patch.object(optimization, 'get_timezone')
    def test_get_timezone_reward_earliest_europe_and_earliest_africa_timezone(
            self, mock_get_timezone):
        mock_get_timezone.return_value = -0.5
        self.assertEqual(optimization.get_timezone_reward(), 35)

        mock_get_timezone.return_value = -1
        self.assertEqual(optimization.get_timezone_reward(), 5)

    @mock.patch.object(optimization, 'get_timezone')
    def test_get_timezone_reward_earliest_europe_and_latest_africa_timezone(
            self, mock_get_timezone):
        mock_get_timezone.return_value = 4
        self.assertEqual(optimization.get_timezone_reward(), 45)
        
        mock_get_timezone.return_value = 0
        self.assertEqual(optimization.get_timezone_reward(), 35)

    @mock.patch.object(optimization, 'get_timezone')
    def test_get_timezone_reward_earliest_asia_and_latest_africa_timezone(
            self, mock_get_timezone):
        mock_get_timezone.return_value = 4.5
        self.assertEqual(optimization.get_timezone_reward(), 15)
        
        mock_get_timezone.return_value = 5.1
        self.assertEqual(optimization.get_timezone_reward(), 5)

    @mock.patch.object(optimization, 'get_timezone')
    def test_get_timezone_reward_other_timezone(
            self, mock_get_timezone):
        mock_get_timezone.return_value = 8
        self.assertEqual(optimization.get_timezone_reward(), 5)
    
    @mock.patch.object(optimization, 'datetime')
    def test_get_timezone(self, mock_datetime):
        mock_datetime.datetime.utcnow.return_value = datetime.datetime(
                2019, 10, 27, 10)
        mock_datetime.datetime.now.return_value = datetime.datetime(
                2019, 10, 26, 23)

        timezone = optimization.get_timezone()
        # get_timezone subtracts utc timezone from device's current timezone.
        # As such, difference must be negative as device's timezone is behind
        # utc timezone.
        self.assertEqual(timezone, -11)

if __name__ == '__main__':
    unittest.main()

