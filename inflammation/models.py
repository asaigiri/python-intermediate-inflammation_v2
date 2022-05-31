"""
Module containing models representing patients and their data.

The Model layer is responsible for the
'business logic' part of the software.

Patients' data is held in an inflammation table (2D array)
where each row contains inflammation data for a single patient
taken over a number of days and each column represents a
single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """
    Load a Numpy array from a CSV.

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=",")


def daily_mean(data):
    """Calculate the daily mean of a 2d inflammation data array."""
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2d inflammation data array."""
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2d inflammation data array."""
    return np.min(data, axis=0)


def patient_normalise(data):
    """Normalise patient data from a 2D inflammation data array."""
    max = np.max(data, axis=1)
    return data / max[:, np.newaxis]


class Observation:
    """
    Class representing a medical observation.

    Arguments
    ---------
    day: int
        Integer indicating the day the observation relative to the
        start of the experiment.
    value: float
        Observation.
    """

    def __init__(self, day: int, value: float):
        """Initialise an Observation object."""
        self.day = day
        self.value = value

    def __str__(self):
        """Print method definition."""
        return str(self.value)


class Person:
    """
    Class representing a person.

    Argument
    --------
    name: str
        Name of the person
    """

    def __init__(self, name: str):
        """Initialise a Person object."""
        self.name = name

    def __str__(self):
        """Print method definition."""
        return self.name


class Patient(Person):
    """
    Class representing a patient in an inflammation study.

    This class inherit from the Person class.

    Arguments
    ---------
    name: str
        Name of the patient.
    observations: [Observation]
    """

    def __init__(self, name: str, observations: Observation = None):
        """Initialise a Person object."""
        super().__init__(name)
        self.observations = observations or []

    def add_observation(self, value, day=None):
        """Add an observation to the Observation list."""
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = Observation(day, value)

        self.observations.append(new_observation)
        return new_observation
