"""
Robot Control Module

This module provides functionality to control a robot using the Viam SDK.
It establishes a connection to a remote robot, monitors a button press
on a GPIO pin, and controls a motor based on the button state.

The module uses environment variables for authentication and connection details:
- ROBOT_API_KEY: The API key for authenticating with the robot
- ROBOT_API_KEY_ID: The ID of the API key
- ROBOT_ADDRESS: The address of the robot (defaults to a specific cloud address if not provided)
"""
import asyncio
import os
from dotenv import load_dotenv

from viam.robot.client import RobotClient
from viam.components.motor import Motor

# Load the environment variables from the .env file
load_dotenv()

robot_api_key = os.getenv("ROBOT_API_KEY")
robot_api_key_id = os.getenv("ROBOT_API_KEY_ID")
robot_address = os.getenv("ROBOT_ADDRESS")


async def connect() -> RobotClient:
    """
    Establishes a connection to the robot client.

    This function creates a RobotClient instance using the provided API credentials
    and connects to a specific robot address.

    Returns:
        RobotClient: An instance of the RobotClient connected to the specified robot.

    Raises:
        Potential exceptions from RobotClient.at_address() if connection fails.
    """
    print(f"Connecting to robot {robot_address}")
    # Create options for the RobotClient using API key authentication
    options = RobotClient.Options.with_api_key(api_key=robot_api_key, api_key_id=robot_api_key_id)

    # Connect to the robot at the specified address using the created options
    return await RobotClient.at_address(robot_address, options)


async def main():
    """
    Main asynchronous function to control a robot based on button presses.
    """
    robot = await connect()
    print("Connected!")

    # Initialize the 'start' motor from the robot
    start: Motor = Motor.from_robot(robot, "motor")
    start.set_rpm(150)

    # Spin the motor for 1 second

    try:
        # Set the motor power to 100%
        await start.set_power(1)

        # Small delay to prevent rapid toggling
        await asyncio.sleep(2)
    except:
        pass

    # Stop the motor
    await start.set_power(0)


if __name__ == "__main__":
    asyncio.run(main())
