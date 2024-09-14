import asyncio
from fastapi import FastAPI, HTTPException, Query, Response
from fastapi.middleware.cors import CORSMiddleware

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

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,  # Allow cookies to be sent with requests
    allow_methods=["*"],  # List of allowed HTTP methods (e.g., GET, POST). Use ["*"] to allow all methods.
    allow_headers=["*"],  # List of allowed headers. Use ["*"] to allow all headers.
)

@app.get("/")
async def read_root():
    robot = await connect()
    print(robot.resource_names)
    return {
        "status": "Robot connected",
        "resource_names": [resource.name for resource in robot.resource_names]
        }

@app.post("/fire_cannon")
async def fire_cannon(key: str = Query(...)):
    if key != "confetti":
        raise HTTPException(status_code=400, detail="Invalid key")
    
    robot = await connect()
    print("Connected!")

    start: Motor = Motor.from_robot(robot, "motor")

    try:
        await start.set_power(1)
        await asyncio.sleep(2)
    except:
        pass

    # Stop the motor
    await start.set_power(0)

    # return {"message": "Confetti fired!"}
    
    headers = {
        "Access-Control-Allow-Origin": "*", # Required for CORS support to work
        "Access-Control-Allow-Credentials": "true", # Required for cookies, authorization headers with HTTPS
        "Access-Control-Allow-Headers": "Origin,Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,locale",
        "Access-Control-Allow-Methods": "POST, OPTIONS"
    }
    return Response(content='{"message": "Confetti fired!"}', media_type="application/json", headers=headers)
