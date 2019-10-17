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

    def test_get_machine_coordinates_reward_coordinates_in_the_rectangle(self):
        coordinates = [86.12, 25.22]
        reward = sum([abs(x) for x in coordinates])/optimization.MAX_COORDINATES_SUM

        machine_coordinates_reward = optimization.get_machine_coordinates_reward(coordinates)
        self.assertEqual(machine_coordinates_reward, reward)

    def test_get_machine_coordinates_reward_coordinates_not_in_the_rectangle(self):
        coordinates = [86.12, 35.22]
        machine_coordinates_reward = optimization.get_machine_coordinates_reward(coordinates)
        self.assertEqual(machine_coordinates_reward, 5)
    

if __name__ == '__main__':
    unittest.main()

