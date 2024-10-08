# migration_management/migration_path.py

from typing import Optional
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:
    def __init__(
        self,
        path_id: int,
        species: str,
        start_location: Habitat,
        destination: Habitat,
        duration: Optional[int] = None
    ):
        self.path_id = path_id
        self.species = species
        self.start_location = start_location
        self.destination = destination
        self.duration = duration

    def __repr__(self):
        return (
            f"MigrationPath(path_id={self.path_id}, species='{self.species}', "
            f"start_location={self.start_location.habitat_id}, "
            f"destination={self.destination.habitat_id}, duration={self.duration})"
        )
