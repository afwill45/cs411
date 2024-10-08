
from typing import Optional, Dict, Any, List
from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.animal_management.animal_manager import AnimalManager
from wildlife_tracker.animal_management.animal import Animal

class HabitatManager:
    def __init__(self, animal_manager: AnimalManager) -> None:
        self.habitats: Dict[int, Habitat] = {}
        self.animal_manager = animal_manager

    def create_habitat(
        self,
        habitat_id: int,
        geographic_area: str,
        size: int,
        environment_type: str,
        animals: Optional[List[int]] = None
    ) -> Habitat:
        habitat = Habitat(
            habitat_id,
            geographic_area,
            size,
            environment_type,
            animals
        )
        self.habitats[habitat_id] = habitat
        print(f"Habitat {habitat_id} created.")
        return habitat

    def remove_habitat(self, habitat_id: int) -> None:
        if habitat_id in self.habitats:
            del self.habitats[habitat_id]
            print(f"Habitat {habitat_id} removed.")
        else:
            print(f"Habitat {habitat_id} not found.")

    def get_habitat_by_id(self, habitat_id: int) -> Optional[Habitat]:
        return self.habitats.get(habitat_id)

    def update_habitat_details(self, habitat_id: int, **kwargs: Dict[str, Any]) -> None:
        habitat = self.get_habitat_by_id(habitat_id)
        if habitat:
            habitat.update_habitat_details(**kwargs)
        else:
            print(f"Habitat {habitat_id} not found.")

    def assign_animals_to_habitat(self, habitat_id: int, animal_ids: List[int]) -> None:
        habitat = self.get_habitat_by_id(habitat_id)
        if habitat:
            animals = []
            for animal_id in animal_ids:
                animal = self.animal_manager.get_animal_by_id(animal_id)
                if animal:
                    animals.append(animal)
                else:
                    print(f"Animal {animal_id} not found.")
            habitat.assign_animals_to_habitat(animals)
        else:
            print(f"Habitat {habitat_id} not found.")

    def get_animals_in_habitat(self, habitat_id: int) -> List[Animal]:
        habitat = self.get_habitat_by_id(habitat_id)
        if habitat:
            animal_ids = habitat.get_animals_in_habitat()
            animals = []
            for animal_id in animal_ids:
                animal = self.animal_manager.get_animal_by_id(animal_id)
                if animal:
                    animals.append(animal)
                else:
                    print(f"Animal {animal_id} not found in system.")
            return animals
        else:
            print(f"Habitat {habitat_id} not found.")
            return []

    def get_habitat_details(self, habitat_id: int) -> Dict[str, Any]:
        habitat = self.get_habitat_by_id(habitat_id)
        if habitat:
            return habitat.get_habitat_details()
        else:
            print(f"Habitat {habitat_id} not found.")
            return {}
