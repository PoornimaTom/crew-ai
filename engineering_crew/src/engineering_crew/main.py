#!/usr/bin/env python
import sys
import warnings
import os

from datetime import datetime

from engineering_crew.crew import EngineeringCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

requirements = """
A simple audio ingestion pipeline for a surveillance platform.
The system should allow users to upload audio files for analysis.
The system should extract metadata from the audio files, including duration, sample rate, and channels.
The system should allow users to search for specific events within the audio files.
The system should provide a way to visualize the extracted metadata.
The system should be able to generate reports based on the analyzed audio files.
The system should be able to handle large audio files efficiently.
The system should be able to integrate with existing surveillance systems.
The system should be able to handle multiple audio formats, including WAV, MP3, and FLAC.
The system should be able to handle audio files with different sample rates and channels.
The system should be able to handle audio files with different bit depths.
The system should be able to handle audio files with different compression formats.
The system should be able to handle audio files with different metadata formats.
The system should be able to handle audio files with different encoding formats.
The system should be able to handle audio files with different sampling rates.
The system should be able to handle audio files with different bit rates.
The system should be able to handle audio files with different channel configurations.
The system should be able to handle audio files with different audio codecs.
The system should be able to handle audio files with different audio formats.
The system should be able to handle audio files with different audio qualities.
"""
module_name = "audio_surveillance.py"
class_name = "AudioSurveillance"


def run():
    """
    Run the crew.
    """
    inputs = {
        'requirements': requirements,
        'module_name': module_name,
        'class_name': class_name
    }
    
    # Initialize the EngineeringCrew and kickoff the crew
    result = EngineeringCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
